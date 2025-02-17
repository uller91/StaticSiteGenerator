import os
import os.path
import shutil

from block_markdown import *
from static_to_public import *


def generate_page(path_from, path_template, path_dest):
    print(f"Generating page from {path_from} to {path_dest} using {path_template}")

    if not os.path.exists(path_from):
        raise Exception("no markdown is found")
    md = open(path_from)
    md_content = md.read()
    md.close()

    if not os.path.exists(path_template):
        raise Exception("no template is found")
    template = open(path_template)
    template_content = template.read()
    template.close()

    html_node = markdown_to_html_node(md_content)
    html_string = html_node.to_html()
    title = extract_title(md_content)
    main_html_string = (template_content.replace("{{ Title }}", title)).replace("{{ Content }}", html_string)

    #not needed due to static_to_public()
    #if not os.path.exists(path_dest):
    #    os.mkdir(path_dest)
    #path_dest_full = os.path.join(path_dest, "index.html")

    html = open(path_dest, 'w+')
    html.write(main_html_string)
    html.close()
    return


def main():
    path_public = "./public"
    path_static = "./static"
    files_copied = static_to_public(path_public, path_static, []) #files_copied is a list of copied files

    path_dest = "./public/index.html"
    path_from = "./content/index.md"
    path_template = "./template.html"
    generate_page(path_from, path_template, path_dest)


main()
