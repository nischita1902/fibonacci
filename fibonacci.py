[a,b]= [0,1]
print(b)
for i in range(2,50):
    c = a + b
    a = b
    b = c
    if c<= 50:
        print(c)
