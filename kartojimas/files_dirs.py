#!/Users/nikitapajanok/Development/Teaching/teaching/kartojimas/env/bin/python
import os
import datetime

def get_current_directory():
    print(os.getcwd())

def change_directory(dirname):
    os.chdir(dirname)
    print(os.getcwd())

def get_files():
    print(os.listdir())

def make_dir():
    os.mkdir("Naujas katalogas")


def make_dirs():
    os.makedirs("new/new_subcat")

def getstats():
    print(os.stat("new"))

def get_weight():
    print(os.stat("data.csv").st_size/ 1_000_000) 

def get_last_modified(fname):
    print(datetime.datetime.fromtimestamp(os.stat(fname).st_mtime))


if __name__ == "__main__":
    # print("laba diena")
    # print(os.getlogin())
    # get_current_directory()
    # change_directory("/Users/nikitapajanok/Development/Teaching/teaching")
    # get_files()
    # make_dir()
    # make_dirs()
    # getstats()
    # get_weight()
    get_last_modified("data.csv")
