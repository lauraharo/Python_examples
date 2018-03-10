#Program reads the lines of textfile 'numbers.txt' and ignores the lines that don't have number values.
import re
lines = []
with open("numbers.txt") as f:
    for line in f:
        if re.match('\d', line):
            lines.append(line)
            
data = [float(x) for x in lines] #parses the data from string to float
s = sum(data) #count the sum
av = s/len(data) #count the average

print(data)
print('Sum:')
print(s)
print('Average:')
print(av)
