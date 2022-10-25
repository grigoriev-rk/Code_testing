
import os
import pathlib
from pathlib import Path
import yadisk

data_2 = os.path.abspath("data_folder/999.txt")
yandex_token = os.path.abspath("token_folder/ya_token.txt")
folder_name = '/folder for files'

def create_folder(): 
    with open (yandex_token, 'r') as token_file:
        ya_token = token_file.read().strip()
    y = yadisk.YaDisk(token=ya_token)
    print(y.check_token()) 
    try:
        y.mkdir(folder_name)
        return ('ok')
    except:
        return ('not ok')

if __name__ == '__main__':
    create_folder()


