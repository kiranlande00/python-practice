# Print patterns

print("Enter any number",end=" ")
num = int(input())

print("Enter 0 either 1 : ",end=" ")
b=int(input())

if bool(b):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
else:
    for i in range(num,0,-1):
        for j in range(0,i):
            print("*",end=" ")
        print()