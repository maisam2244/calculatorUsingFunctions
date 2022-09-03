def add(x,z):
    return x+z
def sub(x,z):
    return x-z
def divide(x,z):
    return x/z
def multiply(x,z):
    return x*z

print("\tChoose any [+ , - , / , x ]")
x = int(input("Enter first num"))
z = int(input("Enter second num"))
y = str(input("Choose any operator"))

if y == '+':
    print("The answer is :")
    print(add(x,z))
elif y == '-':
    print(sub(x,z))
elif y == '/':
    print(divide(x,z))
elif y == 'x':
    print(multiply(x,z))
else:
    print("Invalid operator")



    



