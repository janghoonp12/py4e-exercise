text = "X-DSPAM-Confidence:    0.8475"
pos = text.find('0')
num = text[pos:]
nu = float(num)
print(nu)
