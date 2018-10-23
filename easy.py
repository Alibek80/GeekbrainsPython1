import os

def go_to_folder (folder):
    new_path = os.path.join(os.getcwd(), folder)
    try:
        os.chdir (new_path)
        print ("Успешно перешел в директорию ", new_path)
    except FileNotFoundError:
        print("Невозможно перейти в указанную директорию ", new_path)



def list_folder ():
    print (os.listdir())


def remove_folder (folder):
    new_path = os.path.join(os.getcwd(), folder)
    try:
        os.rmdir (new_path)
        print ("Успешно удалил директорию ", new_path)
    except FileNotFoundError:
        print("Невозможно удалить указанную директорию ", new_path)


def create_folder (folder):
    new_path = os.path.join(os.getcwd(), folder)
    try:
        os.mkdir (new_path)
        print ("Успешно создал директорию ", new_path)
    except FileExistsError:
        print("Невозможно создать указанную директорию ", new_path)
