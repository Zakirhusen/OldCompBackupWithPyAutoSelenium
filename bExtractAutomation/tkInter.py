import os
from firstFile import a
file_stat = os.stat("firstFile.py")
if file_stat.st_mode & 0o111:
    print("File has execute permission")
else:
    print("File does not have execute permission")
num=a[145]
# if num<10:
#     print("ss")

numbers = a
# numbers = ["1", "20", "10003"]
numbers = [str(x).rjust(4, '0') for x in numbers]
print(numbers[2]) # ['0001', '0002', '0003']