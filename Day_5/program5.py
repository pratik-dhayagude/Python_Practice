def Cheak_Maiximum(No1,No2,No3):
	if No1 >No2 and No1>No3:
		return 1
	elif No2>No1 and No2>No3:
		return 2
	else:
		return 3


def main():

	print("Enter first number:")
	No1 = int(input())
	
	print("Enter Second number:")
	No2 = int(input())
	
	print("Enter third number:")
	No3 = int(input())
	
	
	Ret = Cheak_Maiximum(No1,No2,No3)
	
	if Ret == 1:print(No1,"Is Greater")
	elif Ret == 2:print(No2,"Is Greater")
	else:print(No3,"Is greater")
	
	

if __name__ == "__main__":
	main()
