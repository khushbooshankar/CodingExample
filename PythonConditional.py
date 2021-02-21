#Practice: Python Conditional statement
#Tool: Pycharm Community Editor
#Plateform: Window 10
#Author:Khushboo 
#Script Start from here

# Program to check even or odd number
#Dynamically

#----We use keyword called if

'''#number is taken at runtime
number=int(input("Enter a number: "))
if(number%2==0):
    print(number, "Is Even")

#Global Statement
print("This statement doent belong to if")
print(" Though the condition true/false, This will prints")
'''


#Simple Calculator
number_one=int(input("Enter a number: "))
number_two=int(input("Enter a second number: "))
#Wht operation need to be perform
select=int(input("1.Addition\n2.Subsration\n 3. Multiplication\n 4.Division\n 5. Modulous\n 6.Exponentional\n 7.Flore Division\n"))
if(select==1):
    print(number_one+number_two)
elif(select==2):
    print(number_one-number)