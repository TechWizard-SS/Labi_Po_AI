import chemlib
from chemlib import Compound

octin = Compound("C8H14")
print('%.0f' % octin.get_amounts(moles=0.35)['grams'])
print(octin.get_amounts(moles=0.35)['molecules'])
ethelheptene = Compound("C9H18")
print(f"m(2-ethylheptene-3)={'%.0f' % ethelheptene.get_amounts(moles=0.15)['grams']} г")
print(f"N(2-ethylheptene-3)={'%.0f' % ethelheptene.get_amounts(moles=0.15)['molecules']} молекул")
