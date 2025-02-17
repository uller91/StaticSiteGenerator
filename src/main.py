from static_to_public import *
from generate_page import *


def main():
    path_public = "./public"
    path_static = "./static"
    files_copied = static_to_public(path_public, path_static, []) #files_copied is a list of copied files
    print("* Old public directory is deleted.")
    print("* New public directory is created and files from static directory are copied.")


    #legacy code for 1 page html
    '''
    path_dest = "./public/index.html"
    path_from = "./content/index.md"
    path_template = "./template.html"
    generate_page(path_from, path_template, path_dest)
    print("New HTML page is created.")
    '''
    
    print("* Generating new pages...")
    path_dest = "./public"
    path_from = "./content"
    path_template = "./template.html"
    generate_pages_recursive(path_from, path_template, path_dest)
    print("* All pages are successfully generated!.")

main()
