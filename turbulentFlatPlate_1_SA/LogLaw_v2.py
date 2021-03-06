from matplotlib import rcParams
rcParams['font.family'] = ['serif']
rcParams['font.sans-serif'] = ['Tahoma']
import matplotlib.pyplot as plt
import numpy as np

# Auswertung von ux+ zu y+
# Ort von data muss entsprechend dem latestTime Step angepasst werden.
# Hier: Bereich 0 < y < 0.015m

# Log-Law: u+ = 1/k log(y+) + C
# Grenze: y+ = 11
yplus=11
C_p=5    # for a smooth wall
kappa=0.41 

y_visk = np.logspace(-1,1,20)
y_log = np.logspace(1,3, 20)
u_p1 = y_visk 
u_p2 = 1/kappa * np.log(y_log) + C_p


#---------------------------------------------------------------------------- # 
data = np.loadtxt("postProcessing/yLine/5000/data_U_wallShearStress.xy")
coordy = data[:,0]
Ux = data[:,1]
Uy = data[:,2]
Uz = data[:,3]

# Ux und y muss noch entdimensioniert werden.
# Dafuer wird wallShearStress gebraucht
# wallShearStress_x = -6.43976
tau_w_x = data[0,4]   # 6.495
rho = 1
u_tau = np.sqrt(abs(tau_w_x) / rho)
nu = 1.388e-5
#---------------------------------------------------------------------------- # 
Ux_plus = Ux/u_tau
coordy_plus = coordy * u_tau / nu
coordy_plus[0] = 0.1  # Damit logarithmische Darstellung gegen null geht
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(coordy_plus, Ux_plus, color='red', linewidth=1, label='of_SA')
ax.plot(y_visk, u_p1, color='black', marker='^',
                  markersize=5, linewidth=1, label='linear')  # analytisch: viscSublayer
ax.plot(y_log, u_p2, color='black', marker='*',
                  markersize=5, linewidth=1, label='log')   # analytisch: logLayer
ax.set(title='',
       xlabel='$y^+$',
       ylabel='$U_x^+$')
# ax.grid(which='both')
plt.xscale('log')
ax.legend()
plt.show()
fig.savefig("LogLaw.png", dpi=150)
