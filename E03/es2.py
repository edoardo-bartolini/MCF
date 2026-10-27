a = input('inserisci un numero intero: ')
a = int(a)
n = input('inserisci il numero di bit cui applicare operazioni di bit shift: ')
n = int(n)

print('{:8>s} --- {:8>s} --- {:8>s}'.format('intero', 'binario', 'esadecimale'))
print('---------------------------------------------------------------------')
print('{:8} --- {:8} --- {:8}'.format(a, bin(a), hex(a)))

ba = int(bin(a), 2)
xa = int(hex(a), 16)
bs_plus = (ba << n)
bs_minus = (ba >> n)
print('{:8>s} --- {:8>s} --- {:8>s}'.format('...', 'binario', 'esadecimale'))
print('shift <<: {:>12}  {:>6}'.format(bin(bs_plus), hex(bs_plus)))
print('shift >>: {:>12}  {:>6}'.format(bin(bs_minus), hex(bs_minus)))








