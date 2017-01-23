import  json
path = 'data/data_facebook_sample.json'
path_usa = 'data/usa_gov_data.txt'
path_out = 'data/data_out_sample.json'

# Read json from file
## Read a line
data_usa = open(path_usa).readline()
data = open(path_usa).read()

# Read line by line
records = [json.loads(line) for line in open(path_usa)]

# Convert json to dictionary
# records = json.loads(data)

# Write data to file
def write_file():
  file = open(path_out, "w")
  file.write(str(records))
  file.close()

# list comprehension
timezones = [rec['tz'] for rec in records if 'tz' in rec]

# count with pure python
def get_counts(sequence):
  counts = {}
  for x in sequence:
    if (x in counts):
      counts[x] = counts[x] + 1
    else:
      counts[x] = 1
  return counts
# counts = get_counts(timezones)

# count with standart python lib
from collections import  defaultdict
def get_counts2(sequence):
  counts = defaultdict(int)
  for x in timezones:
    counts[x] = counts[x] + 1
  return counts

counts = get_counts(timezones)

# Get 10 timezones
def top_counts(count_dict, n = 10):
  # for count, tz in count_dict.items():
  #   print 0
  value_key = [(count, tz) for tz, count in count_dict.items()]
  value_key.sort()
  return value_key[-n:]

# count_top = top_counts(counts)

# Get 10 most sequence timezones using standard lib
def top_counts2(count_dict, n = 10):
  from collections import  Counter
  counts = Counter(count_dict)
  return counts.most_common(10)
# count_top = top_counts2(timezones)
print 0

