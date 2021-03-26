#Create a dictionary and take input from the user and return the meaning of the word from dictionary


d1={"Array":"Collection of similar data types",
    "Variable":"Used to store some value",
    "Datatype":"Type of data",
    "Operator":"Used to perform operations"}

print("Enter the word you want to know the meaning of that word")
var=input()
print("Meaning:")
print(var,"=",d1[var])
#print(var,"=",d1.get(var))


# def Change(P,Q=30):
#     P = P + Q
#     Q = P - Q
#     print(P, "#", Q)
#     return (P)
#
# R = 150
# S = 100
# R = Change(R,S)
# print(R,"#", S)
# S = Change(S)