from ...application import Application
import os 

class Brave(Application): 
    def __init__(self) -> None:
        super().__init__()
        self.name = "Brave webbrowser"

    def install(self): 
        self.debian_install()
        self.install_success = True
        return self.install_success

    def debian_install(self):
        """ instructions and cmd from 
        https://brave.com/linux/ """
        os.system("sudo apt install curl")
        os.system("sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg")
        os.system('echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list')
        os.system('sudo apt update')
        os.system('sudo apt install brave-browser -y')
