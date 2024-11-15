import mendeleev
from mendeleev import Cs, C, O, Cr, N
import pandas as pd


data = [[x.name, x.ec.unpaired_electrons()] for x in [Cs, C, O, Cr, N]]
columns = ['Название элемента', 'Количество неспаренных электронов']
df = pd.DataFrame(data, columns=columns)

print(df)
