def factorial(x):
    if(x > 1):
        return x * factorial(x-1)
    else:
        return 1

num = input("Enter number: ");
print(num+"! = "+str(factorial(int(num))))
