def DisplayFactors(iNo):

  for i in range(iNo,0,-1):

    if(int(iNo % i)==0):

        print(i)

   

    




def main():

    print("Enter the number:")

    No = int(input())

    DisplayFactors(No)


main()