'''
def total(no):
    print("Finding total")
    t=no+10
    print('Totla no',t)
    return None
def main():
    num=eval(input("Enter a number"))
    total(num)
    return None
main()
'''

#add ,subtract

def main():
    a=eval(input("Enter First Number :"))
    b=eval(input("Enter Second Number :"))
    add(a,b)
    sub(a,b)
    return None
def add(x,y):
    total=x+y
    print(f"ADDITION OF {x} , {y} is : {total}")
def sub(x,y):
    total=x-y
    print(f"Subtraction OF {x} , {y} is : {total}")

main()