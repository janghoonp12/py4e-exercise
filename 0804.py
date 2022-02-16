fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('bad file')
    quit()
fh = open(fname)
lst = list()
for line in fh:
    spl = line.split()
    for aaa in spl:
        if aaa not in lst:
            lst.append(aaa)
lst.sort()
print(lst)
