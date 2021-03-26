#Design a calculator which will correctly solve all the problem except the following once:
#45*3=555 , 56+9=77 , 56/6=4

print("Welcome to calculator:Developed by Kiran Lande")
print("Please type operator do you like to complete")
print("+ for addition")
print("- for substraction")
print("* for multiplication")
print("/ for division")
print("% for modulo")
print("** for power\n")
print("Enter your choice\n",end=" ")

op=input()


print("Enter the first number",end=" ")
num1=int(input())
print("Enter the second number",end=" ")
num2=int(input())

if op == "+":
    if num1==56 and num2==9:
        print("56+9=77")
    else:
        print(num1 + num2)

elif op=="-":
    print(num1-num2)

elif op=="*":
    if num1==45 and num2==3:
        print("45*3=555")
    else:
        print(num1 * num2)

elif op=="/":
    if num1==56 and num2==6:
        print("56/6=4")
    else:
        print(num1/num2)

elif op=="%":
    print(num1%num2)

elif op=="**":
    print(num1**num2)

else:
    print("Invalid operation........")
