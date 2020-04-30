# --------------
# Importing header files
import numpy as np
#Part - 1 --------------
# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

# Append new_record to data
census = np.concatenate((new_record, data), axis=0)
print(census)

#Part - 2 --------------
# Check the potential of a country based on the age distribution 
# that will decide whether the country classifies as 'Young' or 'Old.

# Create a new array by taking only ges from census
age = (census[:,0])
print(age)

# Find the max and min of given age
max_age , min_age = age.max(), age.min()

# Calculate the mean of age
age_mean = age.mean()
print(age_mean)

# Calculate the standard deviation of age
age_std = age.std()
print(age_std)

#Part - 3 --------------
# Check the harmoby of peoples of diffenrent races 

# Create diffrent arrays for diffrent races
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:, 2]==4]

# Check the length of each race 
len_0 =len(race_0)
len_1 =len(race_1)
len_2 =len(race_2)
len_3 =len(race_3)
len_4 =len(race_4)

# Print all the races
print (len_0 , len_1, len_2, len_3, len_4)

# Check the printed answer and decide what is the number of minority (for ex. for len_3 = 3)
minority_race = 3

#Part - 4 --------------
# Check the average of senior citizens are working more then 25 hours per week

# Create an array by filtering the census according to age
senior_citizens = census[census[:, 0] > 60]

# Add all working hours of senior citizens
working_hours_sum = np.sum(senior_citizens[:, 6])
#print(working_hours_sum)

# Check the length of senior citizens
senior_citizens_len = len(senior_citizens)
#print(senior_citizens_len)

# find the average working hours 
avg_working_hours = working_hours_sum /senior_citizens_len
print(avg_working_hours)

#Part - 5 --------------
# Check wheather higher educated peoples have better pay

# Create two arrays 'high' and 'low' by filtering census data
# 10 means the year of education 
high = census[census[:, 1] > 10]
low = census[census[:, 1] <= 10]

# Calculate the mean of both then compare and decide who gets better pay
avg_pay_high = np.mean(high[:, 7])
avg_pay_low = np.mean(low[:, 7])
print(avg_pay_high)
print(avg_pay_low)
