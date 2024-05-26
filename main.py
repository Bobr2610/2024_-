line = '8'*68
while ('222' in line) or ('888' in line):
    if ('222' in line):
        line=line.replace('222','8', 1)
else:
    line=line.replace('888','2', 1)
print(line)