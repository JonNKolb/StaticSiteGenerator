import shutil
import os
import sys
from Block_to_HTML import markdown_to_html_node
from extract_markdown import extract_title

def main():
    basepath = sys.argv[0]
    delete_contents("./docs")
    copy_contents("./static","./docs")
    generate_page("./content","./template.html","./docs", basepath)

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
    return

def identify_pages(source):
    md_files = []
    contents = os.listdir(source)
    for content in contents:
        content_path = os.path.join(source, content)
        if os.path.isfile(content_path) == True and os.path.splitext(content_path)[1] == ".md":
            md_files.append(content_path)
        elif os.path.isdir(content_path):
            md_files.extend(identify_pages(content_path))
    return md_files

def generate_page(from_path, template_path, dest_path, basepath="/"):
    md_files = identify_pages(from_path)
    for file_path in md_files:
        file_dest = file_path.replace(from_path, dest_path).replace(".md",".html")
        print(f'Generating page from {file_path} to {file_dest} using {template_path}')
        with open(file_path, 'r') as from_file: 
            markdown = from_file.read()
        with open(template_path, 'r') as template_file:
            template = template_file.read()
        html = markdown_to_html_node(markdown)
        header = extract_title(markdown)
        template = template.replace("{{ Title }}", header)
        template = template.replace("{{ Content }}", html.to_html())
        template = template.replace('href="/', f'href="{basepath}')
        template = template.replace('src="/', f'src="{basepath}')
        directory = os.path.dirname(file_dest)
        os.makedirs(directory, exist_ok=True)
        with open(file_dest, mode='x') as file:
            file.write(template)


main()