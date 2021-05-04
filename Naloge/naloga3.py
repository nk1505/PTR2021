i = int(input('Vpisi stevilo: '))
stevec = 2
true = 0

while(i == stevec):
    
    if(i % stevec == 0):
        true = 1
        
        if(true == 0):
            print('Prastevila so: ')

        print(i + '\n') 
    
    stevec = stevec + 1
if(true == 1):
    print('Stevilo je prastevilo.')