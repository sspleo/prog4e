hrs = input('Enter hours:')
h = float(hrs)

rate = input('Enter rate per hour:')
r = float(rate)

pay = 0

if h <= 40.0:
    pay = h * r
else:
    pay = 40 * r + (h - 40) * r * 1.5

print(float(pay))
