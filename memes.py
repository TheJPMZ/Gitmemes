from mimetypes import guess_all_extensions, guess_extension
import random

status = []
guesses = []

bank = ["Apple","Banana","Cherry","Date","Elderberry","Fig","Grape","Huckleberry","Jackfruit","Kiwi","Lemon","Mango","Nectarine","Orange","Peach","Pineapple","Quince","Raspberry","Strawberry","Tangerine","Ugliberry","Watermelon"]

word = random.choice(bank).upper()

def show_memes(status: list):
    print("\t |")
    print(f"\t {'O' if len(status) >= 1 else ''}")
    print(f"\t{'/' if len(status) >= 2 else ''}{'|' if len(status) >= 3 else ''}{'7' if len(status) >= 4 else ' '} ")
    print(f"""\t{'/' if len(status) >= 5 else ''} {'''7 ''' if len(status) >= 6 else ''} """)
    
def guess():
    x = input("Guess a letter: ").upper()
    if x in guesses:
        print("You have already guessed that letter")
        return
    if x not in word:
        status.append(x)
        guesses.append(x)
        print("Wrong")
        return
    if x in word:
        guesses.append(x)
        print("Correct")
    


def menu():
    

    done = True
    show_memes(status)
    strin = ""
    for x in word:
        if x in guesses:
            strin += " " + x
        else:
            strin += " _"
            done = False
    print(strin)
    
    if len(status) == 6:
        print("Has perdido")
        print("La palabra era: ", word.title())
        exit()
    
    
    if not done:
        guess()
        done = True
        menu()
        return
    else:
        print("You Won")
        exit()

    


def main():
    print("Welcome to the program")
    while True:
        menu()

if __name__ == '__main__':
    main()