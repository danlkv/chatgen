from path import Path
import os
from word_encode.word_encode import GoogleNews
from prep_text import preprocessing_text


def get_path(cur_path, paths):
    if str(cur_path.name) != "":
        if ".txt" in str(cur_path.name):
            paths.append(cur_path)
        elif "." not in str(cur_path.name):
            for item in os.listdir(cur_path):
                    get_path(cur_path.joinpath(item), paths)
    else :
        for item in os.listdir(cur_path):
                    get_path(cur_path.joinpath(item), paths)



class Dataset:
    
    def __init__(self, path_to_dir = Path("../data/")):
        self.paths = []
        self.path_to_dir = path_to_dir
        get_path(self.path_to_dir, self.paths)
        self.prep = preprocessing_text()
        self.enc = GoogleNews()

    def __getitem__(self, idx):
        with open(self.paths[idx], "r") as f:
            text = f.read()
        return self.enc.encode(self.prep.clear_text(text))
        
    def get_text(self, idx):
        with open(self.paths[idx], "r") as f:
            text = f.read()
        return text
 
    def __len__(self):
        return  len(self.paths)