import matplotlib.pyplot as plt
import pandas as pd

headings = 'date,actual mean,actual min,actual max,average min,average max,record low,record high,record low year,record high year,actual precipitation,average precipitation,record precipitation'
date = []
act_max = []
act_min = []
avg_max = []
avg_min = []
# 1.1
with open('NYCTempRecord.txt', 'r') as txt_file:
    # print(txt_file.readline())
    txt_file.readline()
    with open('NYCTemps.csv', 'w') as csv_file:
        csv_file.write(headings + '\n')
        for line in txt_file:
            # print(line)
            csv_file.write(line)
            info = line.split(',')
            date.append(info[0])
            act_min.append(info[2])
            act_max.append(info[3])
            avg_min.append(info[4])
            avg_max.append(info[5])

# 1.2
# a.
tempYearMaxAct = {}
# b.
tempYearMinAct = {}
# c.
tempYearMaxAvg = {}
# d.
tempYearMinAvg = {}

with open('NYCTemps.csv', 'r') as file:
    file.readline()
    #print(len(file.readlines()))
    for i in range(len(date)):
        # a.
        tempYearMaxAct[date[i]] = act_max[i]
        # b.
        tempYearMinAct[date[i]] = act_min[i]
        # c.
        tempYearMaxAvg[date[i]] = avg_max[i]
        # d.
        tempYearMinAvg[date[i]] = avg_min[i]

# 1.3

act_hottest_temp = pd.Series(tempYearMaxAct).max()
print("Actual temp for hottest day: " + act_hottest_temp)
avg_hottest_temp = pd.Series(tempYearMaxAvg).max()
print("Average temp for hottest day: " + avg_hottest_temp)
act_coldest_temp = pd.Series(tempYearMaxAct).min()
print("Actual temp for coldest day: " + act_coldest_temp)
avg_coldest_temp = pd.Series(tempYearMaxAvg).min()
print("Average temp for coldest day: " + avg_coldest_temp)

# 1.6
df = pd.read_csv('NYCTemps.csv')

# 1.4
precipYearMaxAct = df['actual precipitation']
precipYearMinAct = df['actual precipitation']
precipYearAvg = df['average precipitation']

# 1.5
print(precipYearMaxAct.max())
print(precipYearMinAct.min())
print(precipYearAvg.min())

# 1.7
'''
x_record_low_years = df['record low year'].sort_values().unique()
x_record_high_years = df['record high year'].sort_values().unique()
print(x_record_low_years[0])
print(x_record_high_years[0])
y_no_record_low_years = [] #count no, of time each year appears ie. x_record_low_years[i]
y_no_record_high_years = []

for i in range(len(date)):
    y_no_record_low_years[i] = df[df['record low year'] == x_record_low_years[i]].value_counts()
    y_no_record_high_years[i] = df[df['record high year']  == x_record_high_years[i]].value_counts()
print(y_no_record_low_years)
'''
x_record_low_years = df['record low year'].sort_values().unique()
x_record_high_years = df['record high year'].sort_values().unique()
y_no_record_low_years = []  # Count the number of times each year appears (x_record_low_years[i])
y_no_record_high_years = []
#print(x_record_low_years)
#print(x_record_high_years)
for i in range(len(x_record_low_years)):
    count_low = df[df['record low year'] == x_record_low_years[i]]['record low year'].count()
    y_no_record_low_years.append(count_low)

for i in range(len(x_record_high_years)):
    count_high = df[df['record high year'] == x_record_high_years[i]]['record high year'].count()
    y_no_record_high_years.append(count_high)

#print("Counts of record low years:", y_no_record_low_years)
#print("Counts of record high years:", y_no_record_high_years)


'''
# a.
plt.title('Frequency Diagram Showing Number of Record High Temperature Days per Year')
plt.xlabel('Year')
plt.ylabel('Number of Record High Temperature Days')
plt.bar(x_record_high_years, y_no_record_high_years)
plt.show()
# b.
plt.title('Frequency Diagram Showing Number of Record Low Temperature Days per Year')
plt.xlabel('Year')
plt.ylabel('Number of Record Low Temperature Days')
plt.bar(x_record_low_years, y_no_record_low_years)
plt.show()

'''
# 1.8
# a.
'''
x_months = []
y_highest_temps = []

df['date'] = pd.to_datetime(df['date'])
df['Year'] = df['date'].dt.year
df['Month'] = df['date'].dt.month
df['Day'] = df['date'].dt.day
# Extract month from 'Date' and create a new column 'Month'
df['Month'] = df['Date'].dt.month
# Group by 'Month' and find the maximum temperature for each month
max_temperatures_by_month = df.groupby('Month')['Temperature'].max()
# Display the maximum temperatures for each month
print(max_temperatures_by_month)


# Filter rows for a specific date range
df_filtered = df[(df['Date'] >= '2023-10-10') & (df['Date'] <= '2023-10-11')]

plt.title('Highest Temperature in Each Month')
plt.xlabel('Month')
plt.ylabel('Temperature')
plt.bar(x_months, y_highest_temps)
plt.show()
'''

# b.

# c.
#print(df[['record high year', 'record high']].sort_values(by=['record high year']))
record_low_year = df['record low year'].sort_values()
record_high_year = df['record high year'].sort_values()
record_high_temp = df.sort_values(by='record high year')['record high']
record_low_temp = df.sort_values(by='record low year')['record low']

#print(df['record high '].sort_values(by=['record high year']))
#print(df['record low '].sort_values(by=['record high year']))

plt.title('Record High and Low Temperatures')
plt.xlabel('Year')
plt.ylabel('Temperature')
plt.scatter(record_high_year, record_high_temp, color='r', label='Record High')
plt.scatter(record_low_year, record_low_temp, color='b', label='Record Low')
plt.legend()
plt.show()

# 1.9
# a.
# b.
# c.