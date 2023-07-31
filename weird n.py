n = int(input().strip())
    
if n%2 != 0 and 1 < n < 101:
    print('Weird')
elif n%2 == 0 and 2 < n < 6:
    print("Not Weird")
elif n%2 == 0 and 6 < n < 21:
    print('Weird')
elif n%2 == 0 and n > 20:
    print('Not Weird')            