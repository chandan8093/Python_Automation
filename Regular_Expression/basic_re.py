import re
my_str=input("Enter a sentence : ")
print(f'{my_str.split("is")}')
print(f'{re.split("i[st]",my_str)}')