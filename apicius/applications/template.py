from .application import Application

class Template(Application): 
    def __init__(self) -> None:
        super().__init__()
        self.name = "template_application"

    def install(self): 
        return self.install_success
