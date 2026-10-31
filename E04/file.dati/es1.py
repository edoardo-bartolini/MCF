import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('kplr010666592-2011240104155_slc.csv')

print('colonne file: ')
print(df.columns)

time = df['TIME']
flux = df['SAP_FLUX']
flux_err = df['SAP_FLUX_ERR']

plt.figure(figsize = (7, 7))
plt.plot(time, flux, 'o', color = 'blue')
plt.errorbar(time, flux, yerr = flux_err)
plt.xlabel('tempo [BJD - 2454833]')
plt.ylabel('flusso [e/s]')
plt.title('flusso di elettroni in funzione del tempo')
plt.savefig('grafico flusso con errori', bbox_inches = 'tight')

time_min = 945.75
time_max = 946.05
df_zoom = df.loc[(df['TIME'] > time_min) & (df['TIME'] < time_max)]
time_loc = df_zoom['TIME']
flux_loc = df_zoom['SAP_FLUX']

fig, ax = plt.subplots(figsize = (12, 6))
ax.plot(time, flux, 'o')
ax.set_xlabel('Tempo [BJD - 2454833]')
ax.set_ylabel('Flusso [e-/s]')
ax.set_title('Flusso di elettroni in funzione del tempo')

ins_ax = ax.inset_axes([0.80, 0.80, 0.2, 0.2])
ins_ax.plot(time_loc, flux_loc, 'o')
ins_ax.set_xlabel('')
ins_ax.set_ylabel('')
ins_ax.set_title('Flusso localizzato in un minimo')
plt.show()










