import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('ExoplanetsPars_2025.csv', comment = '#')

print('colonne del file:')
print(df.columns)

T_p = df['pl_orbper']
m_p = df['pl_bmassj']
"""
plt.scatter(T_p, m_p, color = 'orange', s = 8)
plt.xlabel('periodo orbitale', fontsize = 10)
plt.ylabel('massa del pianeta', fontsize = 10)
plt.xscale('log')
plt.yscale('log')
plt.show()
"""
R_max = df['pl_orbsmax']
m_s = df['st_mass']
r = R_max/m_s
"""
plt.scatter(T_p, r, color = 'orange', s = 8)
plt.xlabel('periodo orbitale', fontsize = 10)
plt.ylabel('rapporto fra R_max e m_s', fontsize = 10)
plt.xscale('log', base = 100)
plt.yscale('log', base = 100)
plt.show()
"""
mydfv = df.loc[(df['discoverymethod'] == 'Radial Velocity')]
mydft = df.loc[(df['discoverymethod'] == 'Transit')]

mv = mydfv['pl_bmassj']
mt = mydft['pl_bmassj']
T_pv = mydfv['pl_orbper']
T_pt = mydft['pl_orbper']


plt.scatter(T_pv, mv, s = 8, color = 'orange', label = 'Radial Velocity')
plt.scatter(T_pt, mt, s = 8, color = 'grey', alpha = 0.3, label = 'Transit')
plt.xlabel('periodo orbitale', fontsize = 10)
plt.ylabel('massa del pianeta', fontsize = 10)
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()

min_value = min(mv.min(), mt.min())
max_value = max(mv.max(), mt.max())

b = 50
plt.hist(mv, bins = b, range = (min_value, max_value), color = 'orange', alpha = 0.8, label = 'Radial Velocity')
plt.hist(mt, bins = b, range = (min_value, max_value), color = 'grey', alpha = 0.45, label = 'Transit')
plt.xlabel('masse dei pianeti', fontsize = 10)
plt.legend()
plt.show()














