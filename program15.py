def DisplayEven(no):

    i =1


    while(i <= no):

            print(i*2)
            i = i+1


def main():


    print("Enter the number of frequency to print even number:")

    iNo = int(input())

    DisplayEven(iNo)


main()