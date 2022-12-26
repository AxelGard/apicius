# you might need to add a "." to the .application so that the import becomes correct. 
from .application import Application 

class Template(Application): 
    def __init__(self) -> None:
        super().__init__()
        self.name = "template_application"

    def install(self) -> bool: 
        return self.install_success
