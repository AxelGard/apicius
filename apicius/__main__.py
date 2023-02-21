from . import distrobution
from . import logo
import json 

def load_config():
    f = open("./config.json")
    data = json.load(f)
    f.close()
    return data



def main() -> None: 
    logo.print_logo()
    if distrobution.SET_DISTRIBUTION == "":
        distrobution.set_distribution()
    if distrobution.SET_DISTRIBUTION == "Exit":
        return 
    """
    for app in config.programs_to_install: 
        answer = app.ask()
        if answer:
            installed = app.install()
            if not installed:
                app.install_error()
    """
    
if __name__ == "__main__":
    main()
