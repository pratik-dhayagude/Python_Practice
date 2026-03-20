def DisplayFactors(iNo):

  for i in range(1,iNo):

    if(int(iNo % i) != 0):

        print(i)



def main():

    print("Enter the number:")

    No = int(input())

    DisplayFactors(No)


main()