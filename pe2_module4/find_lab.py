import os

path = input('Enter a path to begin searching: ')
folder = input('Enter a folder to search for: ')

def search(search_path, search_folder):
    try:
        if search_path.split('/')[-1] == search_folder:
            print(search_path)
        curr_dir = os.listdir(search_path)
        if curr_dir == []:
            return
        for fldr in curr_dir:
            search(search_path + '/' + fldr, search_folder) 
    except NotADirectoryError:
        pass

search(path, folder)