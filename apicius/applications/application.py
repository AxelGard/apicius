
class Application: 
    def __init__(self) -> None:
        self.name = ""
        self.install_success = False 

    def install(self) -> bool:
        raise NotImplemented

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
