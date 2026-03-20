def DisplayFactors(iNo):

  iSum = 0
  iSumFactors=0

  for i in range(1,iNo+1):

    if(int(iNo % i) != 0):

      iSum = iSum + i

  
  for i in range(1,iNo):               

    if(int(iNo % i) == 0):

      iSumFactors = iSumFactors + i

  return (iSumFactors - iSum)



def main():

    print("Enter the number:")

    No = int(input())

    Ret = DisplayFactors(No)

    print("The sum will be",Ret)


main()