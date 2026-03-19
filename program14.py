def EvenNumber(no):

    if(no % 2 ==0):

        print("The number will be even number")
    else:
        print("The number is odd number")





def main():

    print("Enter the number:")

    iNo = int(input())

    EvenNumber(iNo)

main()