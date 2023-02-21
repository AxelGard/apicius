from typing import List, Set, Dict, Tuple
import os 
import json

from ..distrobution import SET_DISTRIBUTION

class Application: 
    def __init__(self, file_path):
        self.app_dict = self.load_program(file_path)
        self.name = self.app_dict["name"]
        self.cmd = [] # ["sudo apt install name", ...]
        self.info_dict = {}


    def parse(self):
        self.has_distro = False 
        for dist, info_dict in self.app_dict["distribution"].item(): 
            if SET_DISTRIBUTION.lower() in dist.lower():
                self.has_distro = True
                self.cmd = info_dict["cmd"]

    def ask(self):  
        """ asks the users if they want to install the app """
        print(f"Do you want to install {self.name}? [y/n]")
        answer = input().replace(" ", "");
        return answer == "y" or answer == "Y"

    def install(self):
        for c in self.cmd: 
            try:
                os.system(c)
            except Exception: 
                self.install_error()

    def load_file(path):
        f = open(path)
        data = json.load(f)
        f.close()
        return data

    def install_error(self):
        """ call if erros install proccess happends """
        print("#"*10)
        print(f"install error with {self.name}!")
        print("#"*10)
