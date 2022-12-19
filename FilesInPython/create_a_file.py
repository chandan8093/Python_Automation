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

my_content=["chandan","sakshi","Neeraj","Hi ALL","append added","new append"]
fo=open("test.txt","a")
for i in my_content:
    fo.write(i+"\n")
fo.close()