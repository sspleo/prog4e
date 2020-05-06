hrs = input('Enter hours:')
rate = input('Enter rate per hour:')
try:
    h = float(hrs)
    r = float(rate)
except:
    print('Error, please enter nummeric number')
    quit()
pay = 0

print(h, r)

if h <= 40.0:
    pay = h * r
else:
    pay = 40 * r + (h - 40) * r * 1.5

print(float(pay))
