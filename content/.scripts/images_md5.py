import os
import re
import hashlib

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IMG_LINK = re.compile(r'!\[\[([^\]]+)\]\]')
IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.webp'}

def md5(path):
    f = open(path, "rb")  # Needs to error if any
    h = hashlib.md5()
    for chunk in iter(lambda: f.read(8192), b""): h.update(chunk)
    return h.hexdigest()


def find_all_images():
    """Find all image files recursively in the repository."""
    images = []
    for root, _, files in os.walk(REPO_ROOT):
        # Skip hidden directories and .git
        if '/.git' in root or '/.' in root:
            continue
        for fn in files:
            _, ext = os.path.splitext(fn)
            if ext.lower() in IMAGE_EXTENSIONS:
                img_path = os.path.join(root, fn)
                images.append(img_path)
    return images


def repl(m):
    global changed
    link_path = m.group(1).strip()
    basename = os.path.basename(link_path)

    # Find the image file in our images dictionary
    if basename not in images_by_name:
        print(f'Warning: Image "{basename}" referenced in "{md_path}" not found')
        return m.group(0)

    img_path = images_by_name[basename]
    print(f'Found "{link_path}" in "{md_path}"')

    if img_path in hash_map:
        new_name = hash_map[img_path]
    else:
        h = md5(img_path)
        _, ext = os.path.splitext(basename)
        new_name = f"{h}{ext}"
        img_dir = os.path.dirname(img_path)
        new_path = os.path.join(img_dir, new_name)

        if os.path.exists(new_path):
            try:
                if os.path.samefile(img_path, new_path):
                    # Same file, no need to do anything
                    pass
                elif md5(new_path) == h:
                    # Different file but same hash (duplicate content), remove the current one
                    print(f'Duplicate found: "{img_path}" same as "{new_path}", removing')
                    os.remove(img_path)
                else:
                    raise RuntimeError(f"Hash collision: {basename} -> {new_name} (different content)")
            except ValueError:
                # Files are on different filesystems, compare by hash
                if md5(new_path) == h:
                    print(f'Duplicate found: "{img_path}" same as "{new_path}", removing')
                    os.remove(img_path)
                else:
                    raise RuntimeError(f"Hash collision: {basename} -> {new_name} (different content)")
        else:
            os.rename(img_path, new_path)
            print(f'Renamed "{img_path}" to "{new_path}"')

        hash_map[img_path] = new_name
        # Update the images_by_name dictionary with the new name
        if basename in images_by_name:
            del images_by_name[basename]
        images_by_name[new_name] = new_path

    # Track used images (store full path)
    used_images.add(images_by_name.get(new_name, img_path))

    changed = True
    return f"![[{new_name}]]"


# Initialize data structures
hash_map = {}
used_images = set()

# Find all images in the repository
print("Finding all images in repository...")
all_images = find_all_images()
print(f"Found {len(all_images)} images")

# Create a mapping of basename to full path
images_by_name = {}
for img_path in all_images:
    basename = os.path.basename(img_path)
    if basename in images_by_name:
        print(f'Warning: Duplicate image name "{basename}" found at:')
        print(f'  - {images_by_name[basename]}')
        print(f'  - {img_path}')
    images_by_name[basename] = img_path

# Process all markdown files
print("\nProcessing markdown files...")
for root, _, files in os.walk(REPO_ROOT):
    # Skip hidden directories and .git
    if '/.git' in root or '/.' in root:
        continue

    for fn in files:
        if not fn.lower().endswith(".md"):
            continue
        md_path = os.path.join(root, fn)

        with open(md_path, "r", encoding="utf-8") as f:
            text = f.read()

            changed = False
            new_text = IMG_LINK.sub(repl, text)

            if changed:
                with open(md_path, "w", encoding="utf-8") as f:
                    f.write(new_text)
                    print(f'Updated "{md_path}"')

# Delete unused images
print("\nChecking for unused images...")
deleted_count = 0
for img_path in all_images:
    if img_path not in used_images:
        # Check if it was renamed
        if img_path not in hash_map:
            print(f'Deleting unused image: "{img_path}"')
            try:
                os.remove(img_path)
                deleted_count += 1
            except FileNotFoundError:
                # Image was already renamed/deleted
                pass

print(f"\nSummary:")
print(f"  - Total images found: {len(all_images)}")
print(f"  - Images used: {len(used_images)}")
print(f"  - Images deleted: {deleted_count}")
