from block_markdown import *
from static_to_public import *


def main():
    path_public = "./public"
    path_static = "./static"
    files_copied = static_to_public(path_public, path_static, [])
    #print(files_copied)

main()
