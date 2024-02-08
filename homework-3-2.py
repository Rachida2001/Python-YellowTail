user_input = input("Enter an integer number: ")
try:
    number = int(user_input)   
    print(f"Successfully converted to integer:", user_input, " to " , number)
except ValueError:
    print("Unsuccessfully converted to integer")
