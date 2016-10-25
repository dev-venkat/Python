def sqrt(x): #function to calculate square root
    i=2
    while(i <= int(x/2)):
        if(i == int(x/i)):
          #  print(i)
            break
        i=i+1
    return i

def isPrime(x):  #function to check for primality
    i=2
    root=sqrt(x)
    while(i <= root):
        if((x%i)==0):
            return 1
        i=i+1
    return 0

def genPrime(x): #function to print prime numbers
    i=2
    print(2)
    while(i <= x):
        if(isPrime(int(i)) == 0):
            print(i)
        i=i+1
        
num = input("Enter number: ")
genPrime(int(num))   

