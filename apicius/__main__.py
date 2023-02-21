from . import distribution
from . import logo
from . import selector
import json 
import os 

CONFIG = {}

def load_config():
    f = open("./config.json")
    data = json.load(f)
    f.close()
    global CONFIG
    CONFIG = data
    return CONFIG



def main() -> None: 
    os.system('clear')
    logo.print_logo()
    if distribution.SET_DISTRIBUTION == "":
        distribution.set_distribution()
    if distribution.SET_DISTRIBUTION == "Exit":
        return 
    apps = selector.select_programs()
    for app in apps: 
        app.install()
    
if __name__ == "__main__":
    main()
