# Python program to bild a simple calculater

# 3 step to bild a calculater
#   1. function for operation 
#   2. user input
#   3. print result

# Step 1 : to creat a function

# Functin for add the two number
def add(num1, num2):
    return num1 + num2

# Function for substraction the two number
def sub(num1,num2):
    return num1 - num2

# Function for Mltiplication of two number
def mul(num1 ,num2):
    return num1 * num2

# Function for Division of two number
def div(num1,num2):
    return num1 / num2

# Function for Average of two number
def avg(num1, num2):
    return (num1 + num2)/2

#Step 2 :User input

print("Please select the operation: \n" \
    "1.Addition\n" \
        "2.substraction\n" \
            "3.ltiplication\n" \
               "4.Division\n" \
                    "5.Average\n")

select=int(input("Select opertion form 1,2,3,4,5: "))

num1=float(input("Enter the first element: "))
num2=float(input("Enter the second number: "))

#step 3 : Print the result

if select==1:
    print(num1, "+", num2 , "=", \
        add(num1 , num2))
    
elif select==2:
    print(num1, "-", num2 ,"=" ,\
        sub(num1 , num2))
elif select==3:
    print(num1, "*", num2, "=" ,\
        mul(num1 , num2)) 
    
elif select==4:
    if num2==0:
     print("Error! Division by zero is not allowed .")
    else:
        print(num1 ,"/" ,num2, "=" ,\
         div(num1,num2))

elif select==5:
    print("(" ,num1 ,"+" ,num2 ,")", "/", "2" ,"=", \
        avg(num1, num2))
    
else:
    print("Invalid operation plse select again ")

