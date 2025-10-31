import shutil
import os

def main():
    delete_contents("./public")
    copy_contents("./static","./public")
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

main()