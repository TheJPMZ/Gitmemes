status = []
word = ""

def show_memes(status: list):
    print("\t |")
    print(f"\t {'O' if len(status) == 1 else ''}")
    print(f"\t {'/' if len(status) == 3 else ''}{'|' if len(status) == 3 else ''}{'7' if len(status) == 4 else ' '} ")
    print(f"""\t{'/' if len(status) == 6 else ''} {'''7 ''' if len(status) == 7 else ''} """)
    

def menu():
    show_memes([])


def main():
    print("Welcome to the program")

if __name__ == '__main__':
    main()