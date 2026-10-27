n = input('inserisci un numero intero: ')
m = input('inserisci un numero intero: ')
n = int(n)
m = int(m)

print('{:8>s} --- {:8>s} --- {:8>s}'.format('decimale', 'binario', 'esadecimale'))
print('---------------------------------------------------------------------')
print('{:8} --- {:8} --- {:8}'.format(n, bin(n), hex(n)))
print('---------------------------------------------------------------------')
print('{:8} --- {:8} --- {:8}'.format(m, bin(m), hex(m)))
print('---------------------------------------------------------------------')
print('bitwise AND e OR in scrittura binaria...')
print('n : {:06b}'.format(n))
print('m : {:06b}'.format(m))
print('---------------------------------------------------------------------')
print('(n&m) : {:06b}'.format(n&m))
print('(n|m) : {:06b}'.format(n|m))
print('---------------------------------------------------------------------')
print('bitwise AND e OR in scrittura esadecimale...')
print('n : {:06x}'.format(n))
print('m : {:06x}'.format(m))
print('(n&m) : {:06x}'.format(n&m))
print('(n|m) : {:06x}'.format(n|m))















