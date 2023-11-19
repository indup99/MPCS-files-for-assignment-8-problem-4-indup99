# Indumathi Prakash

# Input number from user
num_ele = input("Enter a number: ")

# Divisibility by eleven function
def divisibility_ele(num_ele):
    # Checking if the number inputted is infact a number
    if not num_ele.isdigit():
        return
    # Setting the sum of the alternating digits to 0 initially
    sum = 0
    # Getting the positive sum of the alternating digits starting from the first digit
    for index in range(0, len(num_ele), 2): 
       sum += int(num_ele[index])
    # Subtacting the sum of the alternating digits starting from the second digit
    for index in range(1, len(num_ele), 2):
       sum -= int(num_ele[index])

    # Printing if the sum is divisible by 11
    if sum % 11 == 0:
        print("This is divisible by 11")
    
    else:
        print("This is not divisible by 11")   
     
# Calling the function
divisibility_ele(num_ele)