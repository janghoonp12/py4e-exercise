# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
ln = 0
sc = None
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    ln = ln + 1
    po = line.find('0')
    nu = line[po:]
    num = float(nu)
    if sc == None:
        sc = num
    else :
        sc = sc + num
print("Average spam confidence:", sc/ln)
