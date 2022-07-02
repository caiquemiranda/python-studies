'''

6. Quantas iterações os seguintes laços executam?
a. for i in range(1, 11) . . .
b. for i in range(10) . . .
c. for i in range(10, 0, −1) . . .
d. for i in range(−10, 11) . . .
e. for i in range(10, 0) . . .
f. for i in range(−10, 11, 2) . . .
g. for i in range(−10, 11, 3) . . .

'''


a = 0
for i in range(1, 11):
    a +=1
b = 0
for i in range(10):
    b +=1
c = 0
for i in range(10, 0, -1):
    c +=1
d = 0
for i in range(-10, 11):
    d +=1
e = 0
for i in range(10, 0):
    e +=1
f = 0
for i in range(-10, 11, 2):
    f +=1
j = 0
for i in range(-10, 11, 3):
    j +=1

print(a, b, c, d, e, f, j)