sett = ['lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì', 'sabato', 'domenica']
giorni_ott = sett[3:7] + sett*3 + sett[0:6]

mese_ott = []
k = 0
for i in range(1,32):
  k = i
  mese_ott.append(k)


for i,j in zip(giorni_ott, mese_ott):
  calend_ott = {i:j}
  print(calend_ott)
