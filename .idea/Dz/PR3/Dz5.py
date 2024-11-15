import chemlib
from chemlib import Compound
H3PO4=Compound("H3PO4")

print(f"w(H)={'%.0f'% H3PO4.percentage_by_mass('H')}" "%")
print(f"w(P)={'%.0f'% H3PO4.percentage_by_mass('P')}" "%")
print(f"w(O)={'%.0f'% H3PO4.percentage_by_mass('O')}" "%")
