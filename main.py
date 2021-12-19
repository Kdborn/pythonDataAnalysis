import pandas

data = pandas.read_csv("reviews.csv",parse_dates=['Timestamp'])
print(data[data['Comment'].str.contains('accent',na=False)]['Rating'].mean())
print(data['Comment'].str.upper(na=False))
s = "Test"
print(s.upper())
