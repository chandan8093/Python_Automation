def function1(x):
    print("Hello ",x)
    function2(x)
    return None

def function2(y):
    print("hi ll")
    print("hi l2",y)
    return None 
def main():
    x=10
    print("main function")
    function1(x)
   

main()