import chempy
from chempy import Substance

pyrite = Substance.from_formula('FeS2')
sulfuric_acid = Substance.from_formula('H2SO4')

print(f"Молярная масса пирита: {pyrite.mass:.1f} г/моль")
print(f"Молярная масса серной кислоты: {sulfuric_acid.mass:.1f} г/моль")

pyrite_weight = 40

sulfuric_acid_mass = round((pyrite_weight * 2 * sulfuric_acid.mass) / pyrite.mass, 1)

print(f"Масса серной кислоты: {sulfuric_acid_mass} тонн")