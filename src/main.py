import shutil
import os
import re
from Block_to_HTML import markdown_to_html_node
from extract_markdown import extract_title

def main():
    delete_contents("./public")
    copy_contents("./static","./public")
    generate_page("./content/index.md","./template.html","./public/index.html")
    return

def delete_contents(pth):
    contents = os.listdir(pth)
    for content in contents:
        content_path = os.path.join(pth, content)
        if os.path.isfile(content_path) == True:
            os.remove(content_path)
        else:
            shutil.rmtree(content_path)

def copy_contents(source, target):
    contents = os.listdir(source)
    for content in contents:
        content_path = os.path.join(source, content)
        if os.path.isfile(content_path) == True:
            shutil.copy(content_path, target)
        else:
            target_dir = os.path.join(target, content)
            os.mkdir(target_dir)
            copy_contents(content_path, target_dir)

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    with open(from_path, 'r') as from_file: 
        markdown = from_file.read()
    with open(template_path, 'r') as template_file:
        template = template_file.read()
    html = markdown_to_html_node(markdown)
    header = extract_title(markdown)
    template = template.replace("{{ Title }}", header)
    template = template.replace("{{ Content }}", html.to_html())
    directory = os.path.dirname(dest_path)
    os.makedirs(directory, exist_ok=True)
    with open(dest_path, mode='x') as file:
        file.write(template)


main()