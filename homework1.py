n = 50
sum = 0
f1 = 1
f2 = 1

for i in range(n):
    sum = f1 + f2
    f2 = f1  
    f1 = sum
    
    print(sum)
