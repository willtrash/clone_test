import pandas as pd

print('mean:', pd.Series([1, 2, 3]).mean())

x = 10

if x % 2 == 0:
    print(f'{x} is even')
else:
    print(f'{x} is odd')
