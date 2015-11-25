import numpy as n
import matplotlib.pyplot as p
from scipy.optimize import curve_fit


def Modelo1(D, H):
    return D * H


def Modelo2(v, H):
    return v / H

Datos = n.loadtxt("data/SNIa.dat", usecols=(1, 2))

D = []
v = []

for a in Datos:
    D.append(a[1])
    v.append(a[0])

H1 = curve_fit(Modelo1, D, v, 2)[0]
H2 = curve_fit(Modelo2, v, D, 2)[0]

H0 = (H1 + H2) / 2
print ('H = '+str(H0[0]))

x = n.linspace(0, 500, 1000)
fig = p.figure()
p.scatter(D, v, label='$Datos$ $originales$')
p.plot(x, x * H0, 'k', label='$H_0 Promedio$')

Nsim = 100000
H0 = []
N = Datos.shape[0]
for i in range(Nsim):
    s = n.random.randint(low=0, high=N, size=N)
    D = []
    v = []
    for a in Datos[s][s]:
        D.append(a[1])
        v.append(a[0])
    H1 = curve_fit(Modelo1, D, v, 2)[0][0]
    H2 = curve_fit(Modelo2, v, D, 2)[0][0]
    H0.append(((H1 + H2) / 2))
H = n.sort(H0)
Hsup = round(H[Nsim * 0.975], 3)
Hinf = round(H[Nsim * 0.025], 3)
print ('El intervalo de confianza al 95% es: ['+str(Hinf)+', '+str(Hsup)+']')

p.plot(x, x * Hsup, 'k', linestyle='-.', label='$Intervalo$ $de$ $confianza$')
p.plot(x, x * Hinf, 'k', linestyle='-.')
p.title('$Datos$ $y$ $resultados$ $para$ $H_0$ $con$ $Supernovas$')
p.xlabel('$Distancia$ $[Mpc]$')
p.ylabel('$Velocidad$ $[km / s]$')
p.xlim(0, 500)
p.ylim(0, 40000)
p.legend(loc='upper left')
fig.savefig('GraficoP2.png')
p.show()