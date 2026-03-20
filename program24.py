def DisplayFactors(iNo):

  iSum = 0

  for i in range(1,iNo+1):

    if(int(iNo % i) != 0):

      iSum = iSum + i

  return iSum



def main():

    print("Enter the number:")

    No = int(input())

    Ret = DisplayFactors(No)

    print("The sum will be",Ret)


main()