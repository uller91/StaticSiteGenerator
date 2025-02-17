import os.path
import shutil


def static_to_public(path_public, path_static, files_list):
    public_dir_delete_create(path_public)
    new_files_list = copy_static_to_public(path_public, path_static, files_list)
    #print(f"in public: {os.listdir("./public")}")
    return new_files_list


def copy_static_to_public(path_public, path_current, files_list):
    
    for item in os.listdir(path_current):
        path_item = os.path.join(path_current, item)
        #print(item_path)
        if os.path.isfile(path_item):
            #print("file")
            shutil.copy(path_item, path_public)
            files_list.append(path_item)

        else:
            #print("folder")
            path_new_folder_public = os.path.join(path_public, item)
            path_current_floder_static = os.path.join(path_current, item)
            os.mkdir(path_new_folder_public)
            #print("forlder made")
            #files_list.extend(
            copy_static_to_public(path_new_folder_public, path_current_floder_static, files_list)

    return files_list


def public_dir_delete_create(path_public):
    if not os.path.exists(path_public):
        os.mkdir(path_public)
        #print("new public created")
    
    elif not os.path.isfile(path_public):
        shutil.rmtree(path_public)
        #print("old public deleted")
        os.mkdir(path_public)
        #print("old public created")
    return