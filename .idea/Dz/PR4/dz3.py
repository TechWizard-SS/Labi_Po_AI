from chempy import Substance

ethylene_mass = 8.4
ethylene = Substance.from_formula('C2H4')

ethylene_n1 = round(ethylene_mass / ethylene.mass, 1)
print('Количество этилена в первой реакции: ' + str(ethylene_n1) + ' моль')

ethylene_volume = 0.896
ethylene_n2 = ethylene_volume / 22.4
print('Количество этилена во второй реакции: ' + str(ethylene_n2) + ' моль')

Q1 = 423.3

Q2 = (ethylene_n2 * Q1) / ethylene_n1
print('Количество теплоты во второй реакции: ' + str(Q2) + ' кДж')
