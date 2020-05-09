def computepay(h, r):
    if h > 40:
        reg = h * r
        adt = (h-40)*r * 0.5
    else:
        reg = h * r
        adt = 0
    return reg + adt


hrs = input("Enter Hours:")
rate = input("Enter rate per hour:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric number")
    quit()

p = computepay(h, r)
print("Pay", p)
