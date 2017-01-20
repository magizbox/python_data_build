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
names1 = names.groupby(['year', 'sex'])
names1 = names1.apply(add_prop)

def get_top1000(group):
  return group.sort_index(by='births', ascending=False)[:1000]
top1000 = names.groupby(['year', 'sex']).apply(get_top1000)

print 0

