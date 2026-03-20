def FactorsMultiplication(iNo):

    iSum = 1

    for i in range(1,iNo):

        if(int(iNo % i) == 0 ):

            iSum = iSum * i

    return iSum





def main():

    print("Enter the number:")

    No = int(input())

    Ret = FactorsMultiplication(No)

    print("The multiplication will be",Ret)

main()