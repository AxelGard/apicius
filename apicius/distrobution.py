
SET_DISTRIBUTION = ""

AVAILABLE_DISTRIBUTIONS = [
    "Exit", # to live and exit
    "Unix", # for non distribution specific 
    "Ubuntu",
    "Debian",
    "Mint",
    "Arch",
    "Manjaro",
]

def set_distribution():
    print("")
    for i, distro in enumerate(AVAILABLE_DISTRIBUTIONS):
        print(f"{i}. {distro}") 
    print("Type the number for the distribution that you are using")

    passed_int = False
    while not passed_int:
        try:
            distro_answer = int(input())
            AVAILABLE_DISTRIBUTIONS[distro_answer]
            passed_int = True 
        except Exception:
            print("try again, if you want to exit input 0 ")
    
    if distro_answer == 0:
        return 
    
    print(f"You have set {AVAILABLE_DISTRIBUTIONS[distro_answer]} as your distribution do you want to set it to something else? [y/n]")
    good_answer = input()
    if good_answer in ["y", "Y"]:
        return set_distribution()

    SET_DISTRIBUTION = AVAILABLE_DISTRIBUTIONS[distro_answer]
