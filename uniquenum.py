i = 1
while(i <= 3):
    j = 1
    while(j <= 3):
        k = 1
        while(k <= 3):
            k += 1
            if(i == k or k == j or j == i):
                continue
            else:
                print(i, j, k)
            k += 1
        j += 1
    i += 1
