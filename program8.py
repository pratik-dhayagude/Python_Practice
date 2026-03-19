def DivisibleNumber(iNo):

    if(iNo % 5 == 0):

        print("The number is divisible by 5")
    else:

        print("The number is not divisible by 5")



def main():


    print("Enter the number:")

    iNo1 = int(input())

    DivisibleNumber(iNo1)

main()