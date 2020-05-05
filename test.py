for n in range(2,200):
    for d in range(2,n):
        if n % d == 0:
            break
    else:
        print(n)