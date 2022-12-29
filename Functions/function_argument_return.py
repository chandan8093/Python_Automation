def main():
    a=eval(input("Enter value of a : "))
    b=eval(input("Enter value of b : "))
    r=add(a,b)
    print(f'total {a} {b} ==> {r}')
    return None
def add(x,y):
    result=x+y
    return result
main()

# default argument
def display(a=99):
    print(a*a)
    return None
display(8)