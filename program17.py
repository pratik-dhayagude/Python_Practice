def EvenFactor(no):

    for i in range(1,(no//2)+1):

        if(int(no % i) ==0 and int(i %2) ==0):

            print(i)

           





def main():


    print("Enter the number:")

    iNo = int(input())

    EvenFactor(iNo)


main()