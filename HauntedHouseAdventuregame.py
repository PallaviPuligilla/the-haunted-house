import time

def introduction():
    print("Welcome to the Haunted House Adventure!")
    print("The gang - Doraemon, Nobita, Shizuka, Suniyo, and Ziyan - have decided to explore a haunted house.")
    print("Inside, they will encounter spooky challenges, puzzles, and ghostly apparitions.")
    print("Their objective is to uncover the truth behind the haunting and bring peace to the restless spirits.")
    print("\nLet's meet the brave explorers!")
    print("Doraemon - The fearless leader who always has a gadget up his sleeve.")
    print("Nobita - The lovable but clumsy friend who provides comic relief.")
    print("Shizuka - The kind-hearted companion who brings warmth to the group.")
    print("Suniyo - The tech-savvy whiz kid who can crack any code.")   
    print("Ziyan - The fearless daredevil who loves taking risks.")
    input("Press Enter to begin...")


def explore_haunted_house():
    print("\nEntering the haunted house...")
    time.sleep(2)
    print("The gang encounters ghostly apparitions and spooky challenges.")
    time.sleep(2)


def solve_puzzle():
    print("\nOh no! Doraemon and his friends are trapped in a mysterious dimension.")
    print("They need to find a way back home. What should they do?")
    print("1. Look for clues")

    print("2. Ask for help")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        print("\nDoraemon: Let's split up, everyone. Search for clues in the surrounding area!")
        print("Nobita: Yeah, we might find something that leads us back home!")
        
    elif choice == "2":
        print("\nDoraemon: Hey, I see a friendly villager nearby. Let's ask for their help!")
        print("Shizuka: Good idea, Doraemon. They might know how to get us out of here!")
        
    else:
        print("Invalid choice. Please enter 1 or 2.")
    print("\nYou come across a mysterious puzzle.")
    print("Doraemon: 'We need to solve this puzzle to proceed.'")
    
    # Add your puzzle-solving logic here
    answer = input("Enter the answer to the puzzle: ").lower()
    
    if answer == "ghost":
        print("Correct! The gang can move forward.")
    else:
        print("Incorrect! The puzzle seems unsolvable.")


def confront_ghosts():
    print("\nWhile searching, they stumble upon an old book with strange symbols.")
    print("To decipher the symbols, they need a translator device.")
    print("What should they do?")
    print("1. Use Doraemon's gadgets")
    print("2. Ask Ziyan for help")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        print("\nDoraemon: Don't worry, I have just the gadget for this situation!")
        print("Nobita: Great! Let's use Doraemon's gadgets to decode the symbols.")
        print("They decode the symbols and discover a hidden portal.")
        print("Doraemon: We've found it! Let's enter the portal and find our way back home!")
        
    elif choice == "2":
        print("\nZiyan: I'm good at solving puzzles. Let me help you decode the symbols!")
        print("Shizuka: That's a brilliant idea! You're really good at this stuff, Ziyan.")
        print("They decode the symbols and discover a hidden portal.")
        print("Shizuka: Yay! Finally, a way back home. Let's go through the portal, everyone!")
        
    else:
        print("Invalid choice. Please enter 1 or 2.")
    
def main():
    introduction()
    explore_haunted_house()
    solve_puzzle()
    confront_ghosts()

if __name__== "__main__":
    main()

