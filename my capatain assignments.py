def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
print("Select operation.")
print("1.Add")
print("2.Subtract")

while True:
    choice= input("Enter choice(1/2):")
    if choicein('1','2'):
        num1 =float(input("Enter first number:"))
        num2 =float(input("Enter second number:"))
        if choice =='1':
            print(num1, "+",num2, "=", add(num1,num2))
            elif choice =='2':
                print(num1,"-",num2,"=",subtract(num1,num2))
                next calculation =input("Let's do next calculation?(yes/no):")
                if next_ calucation =="no":
                break
            else:
                print("invalid Input")
    