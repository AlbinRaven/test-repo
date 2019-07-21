print("-"*10)
a = 3
primelist = [2]
while True:
    countn=0
    countp=0
    for n in primelist:
        if a%n == 0:
            countn += 1
        else:
            countn += 1
            countp += 1
    if countn == countp:
        primelist.append(a)
        print(a)
        a+=1
    else:
        a+=1
print("-"*10)
