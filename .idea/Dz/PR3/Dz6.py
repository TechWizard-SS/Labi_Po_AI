import chemlib
from chemlib import Compound
Fe2SO43 = Compound("Fe2(SO4)3")
Fe_mass = 8

print(f"m(Fe2(SO4)3)={'%.0f'% (Fe_mass / (Fe2SO43.percentage_by_mass('Fe')/100))} г")
