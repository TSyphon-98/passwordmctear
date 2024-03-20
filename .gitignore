def main():  # Nathan McTear
    menuChoice = 0
    while menuChoice != 3:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit \n")
        print("Please enter an option: ", end='')
        menuChoice = int(input())
        if 0 >= menuChoice or menuChoice > 3:
            menuChoice = wrongChoice(menuChoice) # Loops menuChoice into a function to ensure within 1-3
        if menuChoice == 1:
            encode()
        if menuChoice == 2:
            decode()  # needs a parameter


def encode():  # Nathan McTear
    print("please enter your password to encode: ", end='')
    decodedPassword = input()
    password = ''
    for num in decodedPassword:
        num = int(num)
        num += 3
        if num >= 10:
            num -= 10
        password = password + str(num)
    print("Your password has been encoded and stored! \n")


def decode():  # Needs to accept a parameter
    "Here"


def wrongChoice(menuChoice): # Nathan McTear
    while 0 >= menuChoice or menuChoice > 3:
        print("The choice you selected was incorrect! Please enter a correct number! \n")
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit \n")
        print("Please enter an option: ", end='')
        menuChoice = int(input())
    return menuChoice


if __name__ == '__main__':
    main()
