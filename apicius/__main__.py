from . import config

def main() -> None: 
    for app in config.programs_to_install: 
        answer = app.ask()
        if answer:
            installed = app.install()
            if not installed:
                app.install_error()

if __name__ == "__main__":
    main()
