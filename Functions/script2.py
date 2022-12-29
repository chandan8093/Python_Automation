import script1
def mul(x,y):
    print(f"Multiply = {x*y}")

def main():
    a=eval(input("Enter first number : "))
    b=eval(input("Enter second number : "))
    mul(a,b)
    script1.add(a,b)
    script1.sub(a,b)

if __name__=='__main__':
    main()
