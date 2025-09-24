max = int(input())
for i in range(max):
    if(2**i > max):
        print(2**(i-1))
        break