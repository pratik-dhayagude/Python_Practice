class Arithematic:

    #constructor
    def __init__(self,A=0,B=0):
        #characteristics
        self.No1 = A
        self.No2 = B

    
    def Addition(self):

        Ans = self.No1+self.No2

        return Ans


    def Substraction(self):

        Ans = self.No1-self.No2

        return Ans

    def Multiplication(self):

        Ans = self.No1*self.No2

        return Ans

    def Division(self):

        Ans = self.No1/self.No2

        return int(Ans)


def main():

    obj = Arithematic(10,5)

    Ret = obj.Addition()

    print("Addition will be:",Ret)


    Ret = obj.Substraction()

    print("The Substraction will be :",Ret)


    Ret = obj.Multiplication()

    print("The Multiplication will be :",Ret)


    Ret = obj.Division()

    print("The divion will be :",Ret)
  


main()



