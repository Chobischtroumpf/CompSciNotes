from pathlib import Path
from typing import Generator, List

import click


@click.group()
def convert():
    pass


def find_files(starting_dir: Path) -> Generator[Path, None, None]:
    """
    searches for .md files in the current directory and its subdirectories.
    yields their paths one by one.
    returns:
    A generator yielding Path objects for each .md file found.
    """

    current_dir = Path(starting_dir)
    for file_path in current_dir.rglob("*.md"):
        yield file_path


def header_conversion_logic(file_path: Path, author_names: str | List[str]):
    """
    Converts the header of a markdown file to include author names and tags.
    Args:
        file_path (Path): Path to the markdown file.
        author_names (List[str]): List of author names to include in the header.
    """
    # first, we read the first line to check if tags are present, and extract them if they are
    with file_path.open("r", encoding="utf-8") as file:
        # only check first line, as that is where tags would be
        first_line = file.readline()
        while first_line and not first_line.strip():
            first_line = file.readline()

        tags = []
        if first_line.strip().startswith("#"):
            possible_tags = first_line.strip().split()
            tags = [
                tag.strip("#")
                for tag in possible_tags
                if tag.startswith("#") and len(tag.strip("#")) > 0
            ]
            print(f"tags: {tags}")
        elif first_line.startswith("---"):
            return  # already has a header, skip processing
        if not tags:
            file.seek(0)  # reset file pointer to the beginning if no tags found
        # read the rest of the file content
        content = file.read()
    # then, we add the filename as the title and both author names and the tags to the header template
    title = file_path.stem
    authors_formatted = (
        ", ".join(author_names)
        if isinstance(author_names, (list, tuple))
        else author_names
    )
    if tags:
        tags_formatted = "\n  - ".join(tags)
        new_header = f"---\ntitle: {title}\nauthors: {authors_formatted}\ntags:\n  - {tags_formatted}\n---\n"
    else:
        new_header = (
            f"---\ntitle: {title}\nauthors: {authors_formatted}\ntags: []\n---\n"
        )
    # finally, we write the new header back to the file
    with file_path.open("w", encoding="utf-8") as file:
        file.write(new_header + "\n" + content)


@click.command()
@click.argument("authors", nargs=-1, required=True)
@click.option(
    "--directory",
    "-d",
    type=click.Path(exists=True, file_okay=False),
    help="Directory to search for .md files.",
)
@click.option(
    "--file_path",
    "-f",
    type=click.Path(
        exists=True, file_okay=True, dir_okay=False, writable=True, readable=True
    ),
    help="Path to the file to work on",
)
def header_conversion(
    authors: str | List[str], directory: str | None, file_path: str | None
):
    if file_path:
        header_conversion_logic(file_path=Path(file_path), author_names=authors)
    else:
        starting_dir = Path(directory) if directory else Path(".")
        for md_file in find_files(starting_dir):
            header_conversion_logic(file_path=md_file, author_names=authors)


convert.add_command(header_conversion)
if __name__ == "__main__":
    convert()
