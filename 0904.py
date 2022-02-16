name = input('Enter file name: ')
try:
    handle = open(name)
except:
    print('bad file')
    quit()
counts = dict()
for line in handle:
    #line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    counts[words[1]] = counts.get(words[1],0)+1
#print(counts)
bigword = None
bigcount = None
for key, value in counts.items():
    if bigcount == None or value > bigcount:
        bigword = key
        bigcount = value
print(bigword, bigcount)    
