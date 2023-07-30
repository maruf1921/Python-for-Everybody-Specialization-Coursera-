import re

handle = open("Actual_data.txt")
count = 0
y= list()
for line in handle:
    line = line.rstrip()
    y = re.findall('[0-9]+', line)
    for i in y:
        count = count+int(i)
    
print(count)