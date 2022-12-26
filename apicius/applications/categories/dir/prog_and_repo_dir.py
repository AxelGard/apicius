from ...application import Application
import os 

class ProgAndRepoDir(Application): 
    def __init__(self) -> None:
        super().__init__()
        self.name = "Programs and repositories directories "

    def install(self) -> bool:
        path= "~/Programs"
        os.mkdir(path)
        path= "~/Programs/repositories"
        os.mkdir(path)
        self.install_success = True  
        return self.install_success
