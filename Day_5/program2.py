def Cheak_Maximum(No1,No2):
	if No1>No2:return 1
	else:return 2

def main():

	print("Enter the first number:")
	No1 = int(input())
	print("Enter the Second number:")
	No2 = int(input())
	
	Ret = Cheak_Maximum(No1,No2)
	if Ret == 1:print(No1,"is greater")
	else:print(No2,"is greater")
	
	
	

if __name__ == "__main__":
	main()
