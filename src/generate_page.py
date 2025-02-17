import os
import os.path
import shutil

from block_markdown import *


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
    
    return 0


def generate_pages_recursive(path_dir_content, path_template, path_dest_dir):

    #will work correctly only if inside the path_dir_content are only markdowns and folders

    if not os.path.exists(path_template):
        raise Exception("no template is found")
    template = open(path_template)
    template_content = template.read()
    template.close()

    for item in os.listdir(path_dir_content):
        path_item = os.path.join(path_dir_content, item)
        if os.path.isfile(path_item):
            print(f"Generating page from {path_item} to {path_dest_dir} using {path_template}")
            md = open(path_item)
            md_content = md.read()
            md.close()

            html_node = markdown_to_html_node(md_content)
            html_string = html_node.to_html()
            title = extract_title(md_content)
            main_html_string = (template_content.replace("{{ Title }}", title)).replace("{{ Content }}", html_string)

            past_dest_file = os.path.join(path_dest_dir, "index.html")
            html = open(past_dest_file, 'w+')
            html.write(main_html_string)
            html.close()

        else:
            path_new_folder_dest = os.path.join(path_dest_dir, item)
            path_current_floder_content = os.path.join(path_dir_content, item)
            os.mkdir(path_new_folder_dest)
            generate_pages_recursive(path_current_floder_content, path_template, path_new_folder_dest)

    return 0