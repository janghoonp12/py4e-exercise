name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if not line.startswith('From '):
        continue
    words = line.split()
    time = words[5].split(':')
    counts[time[0]] = counts.get(time[0],0) + 1

for k,v in sorted(counts.items()):
    print(k, v)
