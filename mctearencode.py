
def main():  # Nathan McTear
  menuChoice = 0
  encodedpasskey = ''
  while menuChoice != 3:
      print("Menu")
      print("-------------")
      print("1. Encode")
      print("2. Decode")
      print("3. Quit \n")
      print("Please enter an option: ", end='')
      menuChoice = int(input())
      if menuChoice <= 0 or menuChoice > 3:
          menuChoice = wrongChoice(menuChoice) # Loops menuChoice into a function to ensure within 1-3
      if menuChoice == 1:
          encodedpasskey = encode()
      if menuChoice == 2:
          decode(encodedpasskey)


def encode():  # Nathan McTear
  print("Please enter your password to encode: ", end='')
  decodedPassword = input()
  encodedpasskey = ''
  for num in decodedPassword:
    num = int(num)
    num += 3
    if num >= 10:
        num -= 10
    encodedpasskey = encodedpasskey + str(num)
  print("Your password has been encoded and stored! \n")
  return encodedpasskey 
    
def decode(encodedpasskey):  # Jose Cisneros
  decodedpassword = ''
  for num in encodedpasskey:
      num = int(num)
      num -= 3
      if num < 0:
        num += 10
      decodedpassword = decodedpassword + str(num)
  print(f"The encoded password is {encodedpasskey} and the original password is {decodedpassword}.\n")

def wrongChoice(menuChoice): # Nathan McTear
  while menuChoice <= 0 or menuChoice > 3:
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
