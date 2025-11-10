import os
import re
import hashlib
import shutil

MD_DIR = "ULB - Sciences Informatiques"
IMG_DIR = "Images"

IMG_LINK = re.compile(r'!\[\[([^\]]+)\]\]')

def md5(path):
    f = open(path, "rb")  # Needs to error if any
    h = hashlib.md5()
    for chunk in iter(lambda: f.read(8192), b""): h.update(chunk)
    return h.hexdigest()


def repl(m):
    global changed
    link_path = m.group(1).strip()
    basename = os.path.basename(link_path)
    img_path = os.path.join(IMG_DIR, basename)
    if not os.path.exists(img_path): return m.group(0)

    print(f'Found "{link_path}" in "{md_path}"')

    if img_path in hash_map: new_name = hash_map[img_path]
    else:
        h = md5(img_path)
        _, ext = os.path.splitext(basename)
        new_name = f"{h}{ext}"
        new_path = os.path.join(IMG_DIR, new_name)

        if os.path.exists(new_path):
            if md5(new_path) == h and os.path.samefile(img_path, new_path): os.remove(img_path)
            else: raise RuntimeError(f"Name collision: {basename}")
        else: os.rename(img_path, new_path)

        hash_map[img_path] = new_name
        rename_map[basename] = new_name

    changed = True
    return f"![[{new_name}]]"

hash_map = {}
rename_map = {}

for root, _, files in os.walk(MD_DIR):
    for fn in files:
        if not fn.lower().endswith(".md"):
            continue
        md_path = os.path.join(root, fn)

        with open(md_path, "r", encoding = "utf-8") as f:
            text = f.read()

            changed = False
            new_text = IMG_LINK.sub(repl, text)

            if changed:
                with open(md_path, "w", encoding="utf-8") as f:
                    f.write(new_text)
                    print(f'Updated "{md_path}"')
