def computepay(hh, rr):
    if hh <= 40 :
        pp = hh*rr
    else :
        pp = 40*rr + (hh-40)*rr*1.5
    return pp

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate")
r = float(rate)
p = computepay(h, r)
print("Pay", p)
