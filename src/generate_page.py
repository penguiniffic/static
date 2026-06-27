import os
from pathlib import Path
from markdown_blocks import (
    markdown_to_html_node,
    extract_title
)
from htmlnode import ParentNode


def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str) -> None:
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)


def generate_page(from_path: str, template_path: str, dest_path: str):
    print(
        f"Generating page from {from_path} to {dest_path} using {template_path}")
    validate_path(from_path, True)
    validate_path(template_path, True)

    from_markdown_file = get_file_contents(from_path)
    template_file = get_file_contents(template_path)

    from_markdown_html = markdown_to_html_node(from_markdown_file).to_html()
    h1 = extract_title(from_markdown_file)

    replace_header_template_file = template_file.replace("{{ Title }}", h1)
    final_template_file = replace_header_template_file.replace(
        "{{ Content }}", from_markdown_html)

    dest_path_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_path_dir):
        os.makedirs(dest_path_dir)

    write_file(final_template_file, dest_path)


def validate_path(path: str, check_file: bool):
    if not os.path.exists(path):
        raise Exception(f"{path} is not a valid path!")
    if check_file:
        if not os.path.isfile(path):
            raise Exception(f"{path} does not exist!")


def get_file_contents(file: str) -> str:
    try:
        with open(file, "r") as f:
            file_contents = f.read()
        return file_contents
    except Exception as e:
        return f'Error reading file "{file}": {e}'


def write_file(content: str, destination: str):
    try:
        with open(destination, "w") as f:
            write_file_contents = f.write(content)
            print(
                f'Successfully wrote {len(content)} characters to "{destination}"')
    except Exception as e:
        print(f'Error: Error writing file "{destination}": {e}')
