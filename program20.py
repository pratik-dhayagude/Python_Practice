def Display(No):

    if(No == "A" or No == "a" or No == "E"or No == "e"or No == "I"or No == "i"or No == "O"or No == "o"or No == "U"or No == "u"):

        print("The Character is vowel")

    else:
        print("The character is not a vowel")

def main():

    print("Enter they character :")
    i = input()

    Display(i)

    

main()