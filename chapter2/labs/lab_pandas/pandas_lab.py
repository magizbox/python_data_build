from pandas import DataFrame, Series
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json

path_usa = 'data/usa_gov_data.txt'
records = [json.loads(line) for line in open(path_usa)]

frame = DataFrame(records)
tz_counts = frame['tz'].value_counts()

clean_tz = frame['tz'].fillna('missing')
clean_tz[clean_tz == ''] = 'unknown'

clean_tz = clean_tz.value_counts()

clean_tz[:10].plot(kind='barh', rot=0)
# plt.show()

results1 = [x.split()[0] for x in frame.a.dropna()]
results2 = Series([x.split()[0] for x in frame.a.dropna()])

cframe = frame[frame.a.notnull()]
os = np.where(cframe['a'].str.contains('Windows'), 'Windows', "Not Windows")
by_tz_os =  cframe.groupby(['tz', os])
agg_counts = by_tz_os.size().unstack().fillna(0)

indexer = agg_counts.sum(1).argsort()
count_subset = agg_counts.take(indexer)[-10:]
count_subset.plot(kind='barh', stacked='True')
plt.show()
print 0


