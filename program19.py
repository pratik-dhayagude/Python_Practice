def Display(No):


    if(No >= "A" and No <="Z"):

        print("The Case should be",chr(ord(No)+32))

    elif(No >= "a" and No <= "z"):

        print("The Case should be",chr(ord(No)-32))

    




def main():

    print("Enter they character :")
    i = input()

    Display(i)

    

main()