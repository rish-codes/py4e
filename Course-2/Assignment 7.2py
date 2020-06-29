fname = input("Enter file name: ")
fh = open(fname)
add = 0
count = 0
for line in fh:
    line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    words = line.split()
    num = float(words[1])
    add = add + num
    count = count + 1
avg = add/count
print("Average spam confidence:", avg)
