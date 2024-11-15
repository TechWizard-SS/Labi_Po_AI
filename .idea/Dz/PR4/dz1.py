import chempy
from chempy import balance_stoichiometry

reac1, prod1 = balance_stoichiometry(('FeS2', 'O2'), ('Fe2O3', 'SO2'))
print(dict(reac1), dict(prod1))

reac2, prod2 = balance_stoichiometry(('SO2', 'O2'), ('SO3',))
print(dict(reac2), dict(prod2))

reac3, prod3 = balance_stoichiometry(('SO3', 'H2O'), ('H2SO4',))
print(dict(reac3), dict(prod3))