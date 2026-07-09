def Product_Factors(No):
	i = No // 2

	while(i >= 1):
		if No % i == 0:
			print(i)
		i = i-1
			
	
def main():
	
	print("Enter the numbr:")
	No = int(input())
	
	Product_Factors(No)
	
	
if __name__ == "__main__":
	main()
