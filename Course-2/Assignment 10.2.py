name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = dict()

for line in handle:
    line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    
    hour = words[5].split(":")
    hours[hour[0]] = hours.get(hour[0], 0) + 1

lst = list()    
for a,b in hours.items():
    lst.append((a,b))
lst = sorted(lst)

for a,b in lst:
    print(a,b)
