print("Exception Handler")
print("Eroor occured")

print(10/2)


try:
    #Zeroerror
    #print(10/0)
    #fo=open("test1.txt")
    #print(fo.read())
    #fo.close()
    '''
    #indexError
    ar=[5,6,7]
    print(ar[4])

    '''
    
    #ImportError
    import fabric

except Exception as e:
    print("Error is :",e)