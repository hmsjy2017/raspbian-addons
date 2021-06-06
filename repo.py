#!/usr/bin/env python3
print('1.Africa')
print('2.Asia')
option = input('\nChoose your continent:')
if int(option) == 1:
    print('\n1.Kenya')
    option = input('\nChoose your contry:')
    try int(option) == 1:
        print('\n1.Liquid Telecom')
        break
    except:
        print('Invaid input!')
        
elif int (option) == 2:
    print('\n1.China')
    print('2.Japan')
