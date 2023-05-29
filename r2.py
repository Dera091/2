a = (10,-3,4,9,12,-6,0)

min = a[0]
max = a[0]

for i in a:
    if i < min:
        min = i
    if i > max:
        max = i

print("Najmniejsza liczba-",min,)
print("Największa liczba-",max,)