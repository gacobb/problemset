#problem1
#open csv file
f = open('/ufrc/zoo6927/share/Class_Files/data/CO-OPS__8729108__wl.csv')
#read first line
line = f.readline()
#set max water level to 0
max = 0
#read and print each line and search for maximum water level
for line in f:
	print(line)
	line = f.readline()
	num = float(line.split(",")[1]) #This line produces error "could not convert string to float", but still produces correct answer
	if (max < num):
		max = num
		date = (line.split(",")[0])
#print maximum water level and date and time
print(max)
print(date)


#problem 2
import pandas as pd
#read csv as pandas dataframe 
df = pd.read_csv('/ufrc/zoo6927/share/Class_Files/data/CO-OPS__8729108__wl.csv', sep='\s*,\s*', header=0, encoding='ascii', engine='python')
#find the highest water level value and print entire line
df[df['Water Level']==df['Water Level'].max()]

#problem 3
import pandas as pd 
#read csv as pandas dataframe
df = pd.read_csv('/ufrc/zoo6927/share/Class_Files/data/CO-OPS__8729108__wl.csv', sep='\s*,\s*', header=0, encoding='ascii', engine='python')
#Add a column titled Water Difference that calculates the difference in water level between consecutive time points
df['Water Difference'] = \
	[str(n)
    for n in df['Water Level'].diff().fillna(0)]
#find the highest difference in water level between consecutive time points and print entire line
df[df['Water Difference']==df['Water Difference'].max()]

#problem 4
#completed in a jupyter notebook
import pandas as pd
import csv
import matplotlib.pyplot as plt
df = pd.read_csv('/ufrc/zoo6927/share/Class_Files/data/CO-OPS__8729108__wl.csv',sep='\s*,\s*', engine='python')
x = df['Date Time']
y = df['Water Level']
plt.plot(x,y)
plt.ylabel('Water Level')
plt.xlabel('Date')
plt.show()

