import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(5), index=['a','b','c','d','e'])

df = pd.DataFrame({
  'A': pd.Series([1,2,3], index=['a','b','c'])
})

df1 = pd.DataFrame({
  'A': [1,2,3]
})



print 0