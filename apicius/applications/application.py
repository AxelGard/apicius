import os 
class Application: 
    def __init__(self, app_dict:dict) -> None:
        self.name = app_dict["name"]
        
    def parse(self):
        pass

    def install(self, cmd:list[str]) -> None:
        for c in cmd: 
            os.system(c)

    def ask(self) -> bool:  
        """ asks the users if they want to install the app """
        print(f"Do you want to install {self.name}? [y/n]")
        answer = input().replace(" ", "");
        return answer == "y" or answer == "Y"

    def install_error(self) -> None:
        """ call if erros install proccess happends """
        print("#"*10)
        print(f"install error with {self.name}!")
        print("#"*10)
