import re 
s="it pyhton is laa language, which is used is aaaaautomation it is it stp isj03830003r0 22.56.78.99\n chandan"
#Rule of regex  : [a-d], [a-z A-Z 0-9], \w , \W(not part of \w) , \d , . , \. , ^, {number}
pat=r'a{3}'                                           
s_content=re.findall(pat,s)
if not s_content=="":
    print(f'{s_content}')
    print(f"Number of {pat} is {len(s_content)}")
else:
    print("The searched pattern not found")