#IndexError
#ZeroDivisionError
#ImportError
#ValueError
#TypeError
#NameError
#FileNotFoundError
#IOError



try:
    #IndexError
    '''
    data=[1,2,3]
    print(data[6])
    '''

    #ZeroDivisionError
    #print(10/0)

    #ImportError(ModuleNotFoundError)
    #import fabric

    #ValueError

    #TypeError
    print(4+"chandan")

    #NameError
    #print(a)

    #FileNotFoundError
    #open("text.txt")
   

except IndexError:
    print("Please select index within the range")
except ZeroDivisionError:
    print("Division with zero is not possible")

except ModuleNotFoundError:
    print("Install fabric module to install")
    
except NameError:
    print("provide varibale name")

except FileNotFoundError:
    print("Serached for file as file doesn't exists")
    
except TypeError:
    print("int and string concetenation is not possible")
except Exception as e:
    print("Error is : ",e)