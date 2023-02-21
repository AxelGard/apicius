import glob
import os 
from .application import Application
from .logo import print_logo
    
def select_programs(app_dir= "apicius/applications/") -> list:
    result = []
    for file_path in glob.iglob(app_dir + '**/*.json', recursive=True):
        os.system('clear')
        print_logo()    
        print("\n")
        app = Application(file_path)
        app.info()
        if app.ask():
            result.append(app)
    return result 

