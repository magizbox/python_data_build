import pandas as pd
import numpy as np

columns = ['name', 'sex', 'births']

years = range(1880, 1890)
pieces = []
for year in years:
  path = 'data/names/yob%d.txt' % year
  df = pd.read_csv(path, names=columns)
  df['year'] = year
  pieces.append(df)
  print 0

names = pd.concat(pieces, ignore_index=False)
def add_prop(group):
  # Integer  Division floors
  births = group.births.astype(float)
  group['prop'] = births / births.sum()
  return group
names = names.groupby(['year', 'sex'])
names = names.apply(add_prop)

def get_top1000(group):
  group_sort_index = group.sort_index(by='births', ascending=False)[:1000]
  return group_sort_index
top1000 = names.groupby(['year', 'sex']).apply(get_top1000)


def get_quantile_count(group, q=0.5):
  group = group.sort_values(by='prop', ascending=False)
  return group.prop.cumsum().searchsorted(q) + 1
diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')
diversity.head()
print 0

