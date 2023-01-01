# to copy file opertaion :--> 'copy', 'copy2', 'copyfile', 'copyfileobj', 'copymode', 'copystat', 'copytree'
import shutil
import time
#print(dir(shutil))

#copyfile
src="C:\\Users\\Admin\\Desktop\\Python Automation\\Shutil\\copy_file_shutil.py"
des="C:\\Users\\Admin\\Desktop\\Python Automation\Shutil\\copy_file_shutil_bkp.py"
print("Wait for file to copy . . ")
time.sleep(5)
#shutil.copyfile(src,des)


#to give same permission to destination file with source file use copy
#shutil.copy(src,des)

# same metadata for destination file as well
shutil.copy2(src,des)

#copymode-copy permission of source file to destination file
#shutil.copymode(src,des) 

#copystat - copy permission as well as timesatamp to destination file
#shutil.copystat(src,des) 
fo1=open("text1.txt","w")
fo2=open("C:\\Users\\Admin\\Desktop\\Python Automation\Shutil\\copy_file_shutil_bkp.py","r")
shutil.copyfileobj(fo1,fo2)
print("Files copied")