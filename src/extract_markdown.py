import re

def extract_markdown_images(text):
    output = []
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    for match in matches:
        output.append(match)
    return output

def extract_markdown_links(text):
    output = []
    matches = re.findall(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    for match in matches:
        output.append(match)
    return output

def extract_title(markdown):
    match = re.search(r"^# .*$", markdown, re.M)
    if match == None:
        raise Exception("no header")
    else:
        return match.group().strip("#").strip()