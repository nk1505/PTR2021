i = int(input('Vpisi dolzino a stranice za kvadrat: '))
j = i
k = i
while(k > 0):
    while(j > 0):
        print('*', end = '   ')
        j = j - 1
    
    print('\n')
    k = k - 1
    j = i
