import re
fname = input("Enter file name: " )
handle = open(fname)
add = 0
for line in handle:
	num = re.findall('[0-9]+', line)
	for n in num:
		n = int(n)
		add = add + n
	
print(add)
