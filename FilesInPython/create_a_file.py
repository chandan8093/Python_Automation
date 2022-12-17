#working with files in python 
'''
fo=open("my_python_file.py","w")
print("The file mOde <w,r,a>: ",fo.mode)
print('Reable or not',fo.readable())
print('Writeable or not',fo.writable())
fo.write("First Line\bSecond Line")
fo.close()
'''

#Working with for loop files
'''
fo=open("test.txt","a")
my_content=["chandan","sakshi","Neeraj","Hi ALL","append added"]
for i in my_content:
    fo.write(i+"\n")
print("File Saved")
fo.close()

'''
# Read the content
fo=open("test.txt","r")
data=fo.readlines()
for i in range(3):
    print(data[-1])
fo.close()