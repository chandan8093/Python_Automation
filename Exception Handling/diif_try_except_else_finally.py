try:
    data=[1,23,34]
    print(data[0])
except NameError:
    print("Value of a must be defined")
except Exception as e:
    print("Error: ",e)
else:
    print("This will executed if there is no exception in try block")
finally:
    print("Always Executed")