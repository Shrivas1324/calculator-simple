def add(num1,num2):
    return num1 + num2

def sub(num1,num2): 
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

def avg(num1,num2):
    return (num1+num2)/2

#user input 
print("please seclect a operation:\n" \
     "1.Addition\n"\
     "2.Subtraction\n"\
     "3.Multiplication\n"\
     "4.Divison\n"\
     "5.Average\n")

select = int(input("select a operation from 1,2,3,4,5: "))
number1 = int(input("Enter First number: "))
number2 = int(input("Enter Second number: "))

if select == 1:
    print(number1,"+",number2, "= " ,add(number1,number2)) 

elif select == 2:
    print(number1,"-",number2, "=",sub(number1,number2))    

elif select == 3:
    print(number1,"*",number2, "=", multiply(number1,number2))    
    
elif select == 4:
    print(number1,"+",number2, "=", divide(number1,number2))
    
elif select == 5:
    print("(",number1,"+",number2,")" "/","2","=", avg(number1,number2))

else:
    print("invalid operation...!,please select again...!")