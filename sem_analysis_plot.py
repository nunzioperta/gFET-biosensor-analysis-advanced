from scipy.stats import ttest_rel
import statistics
import matplotlib.pyplot as plt
import numpy as np
import sys
from scipy import stats

# Open the file
with open('BLANK.txt', 'r') as file:
    # Create an empty variable to store column data
    column_vgate = []
    column_ch1 = []
    column_ch2 = []
    column_ch3 = []
    column_ch4 = []
    column_ch5 = []
    column_ch6 = []
    column_ch7 = [] 
    column_ch8 = []
    column_ch9 = []
    column_ch10 = []
    column_ch11 = []
    column_ch12 = []

    # Read the file line by line
    for line in file:
        # Check if row starts with "#"
        if line.startswith('#'):
	    # Skip the row
            continue
        # Remove "\\n""
        line = line.replace('\n', '')
        # Split the line by the delimiter (e.g. comma)
        line_data = line.split('\t')
        # Get the column you want to read
        column = line_data[0]
        column_1 = line_data[1]
        column_2 = line_data[2]
        column_3 = line_data[3]
        column_4 = line_data[4]
        column_5 = line_data[5]
        column_6 = line_data[6]
        column_7 = line_data[7]
        column_8 = line_data[8]
        column_9 = line_data[9]
        column_10 = line_data[10]
        column_11 = line_data[11]
        column_12 = line_data[12]

        # Append the column data into the variable
        column_vgate.append(column)
        column_ch1.append(column_1)
        column_ch2.append(column_2)
        column_ch3.append(column_3)
        column_ch4.append(column_4)
        column_ch5.append(column_5)
        column_ch6.append(column_6)
        column_ch7.append(column_7)
        column_ch8.append(column_8)
        column_ch9.append(column_9)
        column_ch10.append(column_10)
        column_ch11.append(column_11)
        column_ch12.append(column_12)

        # Do something with the column data
        # print(column_vgate)
        # print(column_ch1)

#print(column_ch12)

# Pick the first value from column_data
first_value_ch1 = float(column_ch1[0])
first_value_ch2 = float(column_ch2[0])
first_value_ch3 = float(column_ch3[0])
first_value_ch4 = float(column_ch4[0])
first_value_ch5 = float(column_ch5[0])
first_value_ch6 = float(column_ch6[0])
first_value_ch7 = float(column_ch7[0])
first_value_ch8 = float(column_ch8[0])
first_value_ch9 = float(column_ch9[0])
first_value_ch10 = float(column_ch10[0])
first_value_ch11 = float(column_ch11[0])
first_value_ch12 = float(column_ch12[0])
#print(first_value_ch1)

# Pick the last value from column_data
last_value_ch1 = float(column_ch1[120])
last_value_ch2 = float(column_ch2[120])
last_value_ch3 = float(column_ch3[120])
last_value_ch4 = float(column_ch4[120])
last_value_ch5 = float(column_ch5[120])
last_value_ch6 = float(column_ch6[120])
last_value_ch7 = float(column_ch7[120])
last_value_ch8 = float(column_ch8[120])
last_value_ch9 = float(column_ch9[120])
last_value_ch10 = float(column_ch10[120])
last_value_ch11 = float(column_ch11[120])
last_value_ch12 = float(column_ch12[120])

# Pick the mid value from column_data
mid_value_ch1 = float(column_ch1[70])
mid_value_ch2 = float(column_ch2[70])
mid_value_ch3 = float(column_ch3[70])
mid_value_ch4 = float(column_ch4[70])
mid_value_ch5 = float(column_ch5[70])
mid_value_ch6 = float(column_ch6[70])
mid_value_ch7 = float(column_ch7[70])
mid_value_ch8 = float(column_ch8[70])
mid_value_ch9 = float(column_ch9[70])
mid_value_ch10 = float(column_ch10[70])
mid_value_ch11 = float(column_ch11[70])
mid_value_ch12 = float(column_ch12[70])

###################

# Open the file
with open('SAMPLE.txt', 'r') as file:
    # Create an empty variable to store column data
    column_vgateS = []
    column_ch1S = []
    column_ch2S = []
    column_ch3S = []
    column_ch4S = []
    column_ch5S = []
    column_ch6S = []
    column_ch7S = [] 
    column_ch8S = []
    column_ch9S = []
    column_ch10S = []
    column_ch11S = []
    column_ch12S = []

    # Read the file line by line
    for line in file:
        # Check if row starts with "#"
        if line.startswith('#'):
	    # Skip the row
            continue
        # Remove "\\n""
        line = line.replace('\n', '')
        # Split the line by the delimiter (e.g. comma)
        line_data = line.split('\t')
        # Get the column you want to read
        columnS = line_data[0]
        column_1S = line_data[1]
        column_2S = line_data[2]
        column_3S = line_data[3]
        column_4S = line_data[4]
        column_5S = line_data[5]
        column_6S = line_data[6]
        column_7S = line_data[7]
        column_8S = line_data[8]
        column_9S = line_data[9]
        column_10S = line_data[10]
        column_11S = line_data[11]
        column_12S = line_data[12]

        # Append the column data into the variable
        column_vgateS.append(columnS)
        column_ch1S.append(column_1S)
        column_ch2S.append(column_2S)
        column_ch3S.append(column_3S)
        column_ch4S.append(column_4S)
        column_ch5S.append(column_5S)
        column_ch6S.append(column_6S)
        column_ch7S.append(column_7S)
        column_ch8S.append(column_8S)
        column_ch9S.append(column_9S)
        column_ch10S.append(column_10S)
        column_ch11S.append(column_11S)
        column_ch12S.append(column_12S)

        # print(column_vgate)
        # print(column_ch1S)

#print(column_ch1S)

# Pick the first value from column_data
first_value_ch1S = float(column_ch1S[0])
first_value_ch2S = float(column_ch2S[0])
first_value_ch3S = float(column_ch3S[0])
first_value_ch4S = float(column_ch4S[0])
first_value_ch5S = float(column_ch5S[0])
first_value_ch6S = float(column_ch6S[0])
first_value_ch7S = float(column_ch7S[0])
first_value_ch8S = float(column_ch8S[0])
first_value_ch9S = float(column_ch9S[0])
first_value_ch10S = float(column_ch10S[0])
first_value_ch11S = float(column_ch11S[0])
first_value_ch12S = float(column_ch12S[0])
#print(first_value_ch1S)

# Pick the last value from column_data
last_value_ch1S = float(column_ch1S[120])
last_value_ch2S = float(column_ch2S[120])
last_value_ch3S = float(column_ch3S[120])
last_value_ch4S = float(column_ch4S[120])
last_value_ch5S = float(column_ch5S[120])
last_value_ch6S = float(column_ch6S[120])
last_value_ch7S = float(column_ch7S[120])
last_value_ch8S = float(column_ch8S[120])
last_value_ch9S = float(column_ch9S[120])
last_value_ch10S = float(column_ch10S[120])
last_value_ch11S = float(column_ch11S[120])
last_value_ch12S = float(column_ch12S[120])

# Pick the mid value from column_data
mid_value_ch1S = float(column_ch1S[70])
mid_value_ch2S = float(column_ch2S[70])
mid_value_ch3S = float(column_ch3S[70])
mid_value_ch4S = float(column_ch4S[70])
mid_value_ch5S = float(column_ch5S[70])
mid_value_ch6S = float(column_ch6S[70])
mid_value_ch7S = float(column_ch7S[70])
mid_value_ch8S = float(column_ch8S[70])
mid_value_ch9S = float(column_ch9S[70])
mid_value_ch10S = float(column_ch10S[70])
mid_value_ch11S = float(column_ch11S[70])
mid_value_ch12S = float(column_ch12S[70])

#print(mid_value_ch1S)
#print(mid_value_ch2S)
#print(mid_value_ch3S)
#print(mid_value_ch4S)

# Calculate the mean of all first_value_ch without the outliers values
first_value_ch_list = [first_value_ch1, first_value_ch2, first_value_ch3, first_value_ch4, first_value_ch5, first_value_ch6, first_value_ch7, first_value_ch8, first_value_ch9, first_value_ch10, first_value_ch11, first_value_ch12]

first_value_chxS_list = [first_value_ch1S, first_value_ch2S, first_value_ch3S, first_value_ch4S, first_value_ch5S, first_value_ch6S, first_value_ch7S, first_value_ch8S, first_value_ch9S, first_value_ch10S, first_value_ch11S, first_value_ch12S]

# Remove outliers
first_value_ch_list_no_outliers = [x for x in first_value_ch_list if x > 1]
first_value_chxS_list_no_outliers = [x for x in first_value_chxS_list if x > 1]

# Calculate the mean
mean_first_value_ch = sum(first_value_ch_list_no_outliers)/len(first_value_ch_list_no_outliers)
mean_first_value_chxS = sum(first_value_chxS_list_no_outliers)/len(first_value_chxS_list_no_outliers)

print('The mean of all first_value_ch values is', mean_first_value_ch)
print('The mean of all first_value_chxS values is', mean_first_value_chxS)



# Calculate the standard deviation of the first_value_ch_list

stdev_first_value_ch = statistics.stdev(first_value_ch_list_no_outliers)
stdev_first_value_chxS = statistics.stdev(first_value_chxS_list_no_outliers)

print('The calculated SD of the first_value_ch is', stdev_first_value_ch)
print('The calculated SD of the first_value_chxS is', stdev_first_value_chxS)

# Calculate the upper and lower bounds of the standard deviation

#CHANGE HERE TO CHANGE STRINGENCY

upper_bound_first_value_ch = mean_first_value_ch + (stdev_first_value_ch * 1.5)
lower_bound_first_value_ch = mean_first_value_ch - (stdev_first_value_ch * 1.5)

upper_bound_first_value_chxS = mean_first_value_chxS + (stdev_first_value_chxS * 1.5)
lower_bound_first_value_chxS = mean_first_value_chxS - (stdev_first_value_chxS * 1.5)

print('The calculated lower bound of the first_value_ch is', abs(lower_bound_first_value_ch))
print('The calculated upper bound of the first_value_ch is', abs(upper_bound_first_value_ch))
print('The calculated lower bound of the first_value_chxS is', abs(lower_bound_first_value_chxS))
print('The calculated upper bound of the first_value_chxS is', abs(upper_bound_first_value_chxS))

# Create a list of all first_value_ch that are within the bounds
first_value_ch_list_in_bounds = [x for x in first_value_ch_list if x > lower_bound_first_value_ch and x < upper_bound_first_value_ch]
first_value_chxS_list_in_bounds = [x for x in first_value_chxS_list if x > lower_bound_first_value_chxS and x < upper_bound_first_value_chxS]

# Calculate the mean of all first_value_ch without the statistically significant outliers
mean_first_value_ch_no_outliers = sum(first_value_ch_list_in_bounds)/len(first_value_ch_list_in_bounds)
mean_first_value_chxS_no_outliers = sum(first_value_chxS_list_in_bounds)/len(first_value_chxS_list_in_bounds)

print('The mean of all first_value_ch without the statistically significant outliers is', mean_first_value_ch_no_outliers)
print('The mean of all first_value_chxS without the statistically significant outliers is', mean_first_value_chxS_no_outliers)








# Calculate the mean of all mid_value_chxS without the outliers values
mid_value_chxS_list = [mid_value_ch1S, mid_value_ch2S, mid_value_ch3S, mid_value_ch4S, mid_value_ch5S, mid_value_ch6S, mid_value_ch7S, mid_value_ch8S, mid_value_ch9S, mid_value_ch10S, mid_value_ch11S, mid_value_ch12S]

# Remove outliers
mid_value_chxS_list_no_outliers = [x for x in mid_value_chxS_list if x > 0]

# Calculate the mean
mean_mid_value_chxS = sum(mid_value_chxS_list_no_outliers)/len(mid_value_chxS_list_no_outliers)



# Calculate the standard deviation of the mid_value_chxS_list

stdev_mid_value_chxS = statistics.stdev(mid_value_chxS_list_no_outliers)



#CHANGE HERE TO CHANGE STRINGENCY

# Calculate the upper and lower bounds of the standard deviation
upper_bound_mid_value_chxS = mean_mid_value_chxS + (stdev_mid_value_chxS * 1.5)
lower_bound_mid_value_chxS = mean_mid_value_chxS - (stdev_mid_value_chxS * 1.5)


# Create a list of all mid_value_chxS that are within the bounds
mid_value_chxS_list_in_bounds = [x for x in mid_value_chxS_list if x > lower_bound_mid_value_chxS and x < upper_bound_mid_value_chxS]

# Calculate the mean of all mid_value_chxS without the statistically significant outliers
mean_mid_value_chxS_no_outliers = sum(mid_value_chxS_list_in_bounds)/len(mid_value_chxS_list_in_bounds)





# Calculate the mean of all mid_value_chh without the outliers values
mid_value_ch_list = [mid_value_ch1, mid_value_ch2, mid_value_ch3, mid_value_ch4, mid_value_ch5, mid_value_ch6, mid_value_ch7, mid_value_ch8, mid_value_ch9, mid_value_ch10, mid_value_ch11, mid_value_ch12]

# Remove outliers
mid_value_ch_list_no_outliers = [x for x in mid_value_ch_list if x > 0]

# Calculate the mean
mean_mid_value_ch = sum(mid_value_ch_list_no_outliers)/len(mid_value_ch_list_no_outliers)

# Calculate the standard deviation of the mid_value_ch_list

stdev_mid_value_ch = statistics.stdev(mid_value_ch_list_no_outliers)

#CHANGE HERE TO CHANGE THE STRINGENCY


# Calculate the upper and lower bounds of the standard deviation
upper_bound_mid_value_ch = mean_mid_value_ch + (stdev_mid_value_ch * 1.5)
lower_bound_mid_value_ch = mean_mid_value_ch - (stdev_mid_value_ch * 1.5)


# Create a list of all mid_value_ch that are within the bounds
mid_value_ch_list_in_bounds = [x for x in mid_value_ch_list if x > lower_bound_mid_value_ch and x < upper_bound_mid_value_ch]

# Calculate the mean of all mid_value_ch without the statistically significant outliers
mean_mid_value_ch_no_outliers = sum(mid_value_ch_list_in_bounds)/len(mid_value_ch_list_in_bounds)



print('The mean of all mid_value_ch values is', mean_mid_value_ch)
print('The mean of all mid_value_chxS values is', mean_mid_value_chxS)

print('The calculated SD of the mid_value_ch is', stdev_mid_value_ch)
print('The calculated SD of the mid_value_chxS is', stdev_mid_value_chxS)


print('The calculated lower bound of the mid_value_ch is', abs(lower_bound_mid_value_ch))
print('The calculated upper bound of the mid_value_ch is', abs(upper_bound_mid_value_ch))
print('The calculated lower bound of the mid_value_chxS is', abs(lower_bound_mid_value_chxS))
print('The calculated upper bound of the mid_value_chxS is', abs(upper_bound_mid_value_chxS))

print('The mean of all mid_value_ch without the statistically significant outliers is', mean_mid_value_ch_no_outliers)
print('The mean of all mid_value_chxS without the statistically significant outliers is', mean_mid_value_chxS_no_outliers)



# Check if first_value is Greater than 50

min_value_listS = []
min_value_list = []

transfer_blank = []
transfer_sample = []


# Check if first_value is Greater than 50
if first_value_ch1 < abs(upper_bound_first_value_ch) and first_value_ch1S < abs(upper_bound_first_value_chxS) and (first_value_ch1 > abs(lower_bound_first_value_ch) and last_value_ch1 > abs(lower_bound_first_value_ch)) and (first_value_ch1S > abs(lower_bound_first_value_chxS) and last_value_ch1S > abs(lower_bound_first_value_chxS)) and (mid_value_ch1S > lower_bound_mid_value_chxS and mid_value_ch1S < upper_bound_mid_value_chxS) and (mid_value_ch1 > lower_bound_mid_value_ch and mid_value_ch1 < upper_bound_mid_value_ch):
    print('Chanel 1 activated')
    min_value_ch1 = min(column_ch1)
    min_value_ch1S = min(column_ch1S)
    min_value_vg1 = column_vgate[column_ch1.index(min_value_ch1)]
    min_value_vg1S = column_vgateS[column_ch1S.index(min_value_ch1S)]
    min_value_list.append(min_value_vg1)
    min_value_listS.append(min_value_vg1S)
    transfer_blank.append(list(map(float, column_ch1)))
    transfer_sample.append(list(map(float, column_ch1S)))

if first_value_ch2 < abs(upper_bound_first_value_ch) and first_value_ch2S < abs(upper_bound_first_value_chxS) and (first_value_ch2 > abs(lower_bound_first_value_ch) and last_value_ch2 > abs(lower_bound_first_value_ch)) and (first_value_ch2S > abs(lower_bound_first_value_chxS) and last_value_ch2S > abs(lower_bound_first_value_chxS)) and (mid_value_ch2S > lower_bound_mid_value_chxS and mid_value_ch2S < upper_bound_mid_value_chxS) and (mid_value_ch2 > lower_bound_mid_value_ch and mid_value_ch2 < upper_bound_mid_value_ch):
    print('Chanel 2 activated')
    min_value_ch2 = min(column_ch2)
    min_value_ch2S = min(column_ch2S)
    min_value_vg2 = column_vgate[column_ch2.index(min_value_ch2)]
    min_value_vg2S = column_vgateS[column_ch2S.index(min_value_ch2S)]
    min_value_list.append(min_value_vg2)
    min_value_listS.append(min_value_vg2S)
    transfer_blank.append(list(map(float, column_ch2)))
    transfer_sample.append(list(map(float, column_ch2S)))

if first_value_ch3 < abs(upper_bound_first_value_ch) and first_value_ch3S < abs(upper_bound_first_value_chxS) and (first_value_ch3 > abs(lower_bound_first_value_ch) and last_value_ch3 > abs(lower_bound_first_value_ch)) and (first_value_ch3S > abs(lower_bound_first_value_chxS) and last_value_ch3S > abs(lower_bound_first_value_chxS)) and (mid_value_ch3S > lower_bound_mid_value_chxS and mid_value_ch3S < upper_bound_mid_value_chxS) and (mid_value_ch3 > lower_bound_mid_value_ch and mid_value_ch3 < upper_bound_mid_value_ch):
    print('Chanel 3 activated')
    min_value_ch3 = min(column_ch3)
    min_value_ch3S = min(column_ch3S)
    min_value_vg3 = column_vgate[column_ch3.index(min_value_ch3)]
    min_value_vg3S = column_vgateS[column_ch3S.index(min_value_ch3S)]
    min_value_list.append(min_value_vg3)
    min_value_listS.append(min_value_vg3S)
    transfer_blank.append(list(map(float, column_ch3)))
    transfer_sample.append(list(map(float, column_ch3S)))

if first_value_ch4 < abs(upper_bound_first_value_ch) and first_value_ch4S < abs(upper_bound_first_value_chxS) and (first_value_ch4 > abs(lower_bound_first_value_ch) and last_value_ch4 > abs(lower_bound_first_value_ch)) and (first_value_ch4S > abs(lower_bound_first_value_chxS) and last_value_ch4S > abs(lower_bound_first_value_chxS)) and (mid_value_ch4S > lower_bound_mid_value_chxS and mid_value_ch4S < upper_bound_mid_value_chxS) and (mid_value_ch4 > lower_bound_mid_value_ch and mid_value_ch4 < upper_bound_mid_value_ch):
    print('Chanel 4 activated')
    min_value_ch4 = min(column_ch4)
    min_value_ch4S = min(column_ch4S)
    min_value_vg4 = column_vgate[column_ch4.index(min_value_ch4)]
    min_value_vg4S = column_vgateS[column_ch4S.index(min_value_ch4S)]
    min_value_list.append(min_value_vg4)
    min_value_listS.append(min_value_vg4S)
    transfer_blank.append(list(map(float, column_ch4)))
    transfer_sample.append(list(map(float, column_ch4S)))

if first_value_ch5 < abs(upper_bound_first_value_ch) and first_value_ch5S < abs(upper_bound_first_value_chxS) and (first_value_ch5 > abs(lower_bound_first_value_ch) and last_value_ch5 > abs(lower_bound_first_value_ch)) and (first_value_ch5S > abs(lower_bound_first_value_chxS) and last_value_ch5S > abs(lower_bound_first_value_chxS)) and (mid_value_ch5S > lower_bound_mid_value_chxS and mid_value_ch5S < upper_bound_mid_value_chxS) and (mid_value_ch5 > lower_bound_mid_value_ch and mid_value_ch5 < upper_bound_mid_value_ch):
    print('Chanel 5 activated')
    min_value_ch5 = min(column_ch5)
    min_value_ch5S = min(column_ch5S)
    min_value_vg5 = column_vgate[column_ch5.index(min_value_ch5)]
    min_value_vg5S = column_vgateS[column_ch5S.index(min_value_ch5S)]
    min_value_list.append(min_value_vg5)
    min_value_listS.append(min_value_vg5S)
    transfer_blank.append(list(map(float, column_ch5)))
    transfer_sample.append(list(map(float, column_ch5S)))

if first_value_ch6 < abs(upper_bound_first_value_ch) and first_value_ch6S < abs(upper_bound_first_value_chxS) and (first_value_ch6 > abs(lower_bound_first_value_ch) and last_value_ch6 > abs(lower_bound_first_value_ch)) and (first_value_ch6S > abs(lower_bound_first_value_chxS) and last_value_ch6S > abs(lower_bound_first_value_chxS)) and (mid_value_ch6S > lower_bound_mid_value_chxS and mid_value_ch6S < upper_bound_mid_value_chxS) and (mid_value_ch6 > lower_bound_mid_value_ch and mid_value_ch6 < upper_bound_mid_value_ch):
    print('Chanel 6 activated')
    min_value_ch6 = min(column_ch6)
    min_value_ch6S = min(column_ch6S)
    min_value_vg6 = column_vgate[column_ch6.index(min_value_ch6)]
    min_value_vg6S = column_vgateS[column_ch6S.index(min_value_ch6S)]
    min_value_list.append(min_value_vg6)
    min_value_listS.append(min_value_vg6S)
    transfer_blank.append(list(map(float, column_ch6)))
    transfer_sample.append(list(map(float, column_ch6S)))

if first_value_ch7 < abs(upper_bound_first_value_ch) and first_value_ch7S < abs(upper_bound_first_value_chxS) and (first_value_ch7 > abs(lower_bound_first_value_ch) and last_value_ch7 > abs(lower_bound_first_value_ch)) and (first_value_ch7S > abs(lower_bound_first_value_chxS) and last_value_ch7S > abs(lower_bound_first_value_chxS)) and (mid_value_ch7S > lower_bound_mid_value_chxS and mid_value_ch7S < upper_bound_mid_value_chxS) and (mid_value_ch7 > lower_bound_mid_value_ch and mid_value_ch7 < upper_bound_mid_value_ch):
    print('Chanel 7 activated')
    min_value_ch7 = min(column_ch7)
    min_value_ch7S = min(column_ch7S)
    min_value_vg7 = column_vgate[column_ch7.index(min_value_ch7)]
    min_value_vg7S = column_vgateS[column_ch7S.index(min_value_ch7S)]
    min_value_list.append(min_value_vg7)
    min_value_listS.append(min_value_vg7S)
    transfer_blank.append(list(map(float, column_ch7)))
    transfer_sample.append(list(map(float, column_ch7S)))

if first_value_ch8 < abs(upper_bound_first_value_ch) and first_value_ch8S < abs(upper_bound_first_value_chxS) and (first_value_ch8 > abs(lower_bound_first_value_ch) and last_value_ch8 > abs(lower_bound_first_value_ch)) and (first_value_ch8S > abs(lower_bound_first_value_chxS) and last_value_ch8S > abs(lower_bound_first_value_chxS)) and (mid_value_ch8S > lower_bound_mid_value_chxS and mid_value_ch8S < upper_bound_mid_value_chxS) and (mid_value_ch8 > lower_bound_mid_value_ch and mid_value_ch8 < upper_bound_mid_value_ch):
    print('Chanel 8 activated')
    min_value_ch8 = min(column_ch8)
    min_value_ch8S = min(column_ch8S)
    min_value_vg8 = column_vgate[column_ch8.index(min_value_ch8)]
    min_value_vg8S = column_vgateS[column_ch8S.index(min_value_ch8S)]
    min_value_list.append(min_value_vg8)
    min_value_listS.append(min_value_vg8S)
    transfer_blank.append(list(map(float, column_ch8)))
    transfer_sample.append(list(map(float, column_ch8S)))

if first_value_ch9 < abs(upper_bound_first_value_ch) and first_value_ch9S < abs(upper_bound_first_value_chxS) and (first_value_ch9 > abs(lower_bound_first_value_ch) and last_value_ch9 > abs(lower_bound_first_value_ch)) and (first_value_ch9S > abs(lower_bound_first_value_chxS) and last_value_ch9S > abs(lower_bound_first_value_chxS)) and (mid_value_ch9S > lower_bound_mid_value_chxS and mid_value_ch9S < upper_bound_mid_value_chxS) and (mid_value_ch9 > lower_bound_mid_value_ch and mid_value_ch9 < upper_bound_mid_value_ch):
    print('Chanel 9 activated')
    min_value_ch9 = min(column_ch9)
    min_value_ch9S = min(column_ch9S)
    min_value_vg9 = column_vgate[column_ch9.index(min_value_ch9)]
    min_value_vg9S = column_vgateS[column_ch9S.index(min_value_ch9S)]
    min_value_list.append(min_value_vg9)
    min_value_listS.append(min_value_vg9S)
    transfer_blank.append(list(map(float, column_ch9)))
    transfer_sample.append(list(map(float, column_ch9S)))

if first_value_ch10 < abs(upper_bound_first_value_ch) and first_value_ch10S < abs(upper_bound_first_value_chxS) and (first_value_ch10 > abs(lower_bound_first_value_ch) and last_value_ch10 > abs(lower_bound_first_value_ch)) and (first_value_ch10S > abs(lower_bound_first_value_chxS) and last_value_ch10S > abs(lower_bound_first_value_chxS)) and (mid_value_ch10S > lower_bound_mid_value_chxS and mid_value_ch10S < upper_bound_mid_value_chxS) and (mid_value_ch10 > lower_bound_mid_value_ch and mid_value_ch10 < upper_bound_mid_value_ch):
    print('Chanel 10 activated')
    min_value_ch10 = min(column_ch10)
    min_value_ch10S = min(column_ch10S)
    min_value_vg10 = column_vgate[column_ch10.index(min_value_ch10)]
    min_value_vg10S = column_vgateS[column_ch10S.index(min_value_ch10S)]
    min_value_list.append(min_value_vg10)
    min_value_listS.append(min_value_vg10S)
    transfer_blank.append(list(map(float, column_ch10)))
    transfer_sample.append(list(map(float, column_ch10S)))

if first_value_ch11 < abs(upper_bound_first_value_ch) and first_value_ch11S < abs(upper_bound_first_value_chxS) and (first_value_ch11 > abs(lower_bound_first_value_ch) and last_value_ch11 > abs(lower_bound_first_value_ch)) and (first_value_ch11S > abs(lower_bound_first_value_chxS) and last_value_ch11S > abs(lower_bound_first_value_chxS)) and (mid_value_ch11S > lower_bound_mid_value_chxS and mid_value_ch11S < upper_bound_mid_value_chxS) and (mid_value_ch11 > lower_bound_mid_value_ch and mid_value_ch11 < upper_bound_mid_value_ch):
    print('Chanel 11 activated')
    min_value_ch11 = min(column_ch11)
    min_value_ch11S = min(column_ch11S)
    min_value_vg11 = column_vgate[column_ch11.index(min_value_ch11)]
    min_value_vg11S = column_vgateS[column_ch11S.index(min_value_ch11S)]
    min_value_list.append(min_value_vg11)
    min_value_listS.append(min_value_vg11S)
    transfer_blank.append(list(map(float, column_ch11)))
    transfer_sample.append(list(map(float, column_ch11S)))

if first_value_ch12 < abs(upper_bound_first_value_ch) and first_value_ch12S < abs(upper_bound_first_value_chxS) and (first_value_ch12 > abs(lower_bound_first_value_ch) and last_value_ch12 > abs(lower_bound_first_value_ch)) and (first_value_ch12S > abs(lower_bound_first_value_chxS) and last_value_ch12S > abs(lower_bound_first_value_chxS)) and (mid_value_ch12S > lower_bound_mid_value_chxS and mid_value_ch12S < upper_bound_mid_value_chxS) and (mid_value_ch12 > lower_bound_mid_value_ch and mid_value_ch12 < upper_bound_mid_value_ch):
    print('Chanel 12 activated')
    min_value_ch12 = min(column_ch12)
    min_value_ch12S = min(column_ch12S)
    min_value_vg12 = column_vgate[column_ch12.index(min_value_ch12)]
    min_value_vg12S = column_vgateS[column_ch12S.index(min_value_ch12S)]
    min_value_list.append(min_value_vg12)
    min_value_listS.append(min_value_vg12S)
    transfer_blank.append(list(map(float, column_ch12)))
    transfer_sample.append(list(map(float, column_ch12S)))


# Create a floating number array with min_value_listS
min_value_float_list = [float(x) for x in min_value_list]
min_value_float_listS = [float(x) for x in min_value_listS]

print("Vg min values for Blank", min_value_float_list)
print("Vg min values for Sample", min_value_float_listS)

#print(transfer_blank)

# Calculate a t-test paired between min_value_float_list and min_value_float_listS

t_stat, p_value = ttest_rel(min_value_float_list, min_value_float_listS)

print('T-Statistic:', t_stat)
print('P-Value:', p_value)

#print(transfer_blank)

print("BLANK Mean %6.4f" % (float(stats.tmean(min_value_float_list))))
print("SAMPLE Mean %6.4f" % (float(stats.tmean(min_value_float_listS))))



print("BLANK Mean Normalized %6.4f" % (float(stats.tmean(min_value_float_list))/(stats.tmean(min_value_float_list))))
print("SAMPLE Mean Normalized %6.4f" % (float(stats.tmean(min_value_float_listS))/(stats.tmean(min_value_float_list))))

BLANK_Normalized_Values = list(round(float(x/float(stats.tmean(min_value_float_list))), 4) for x in min_value_float_list)


print("Blank Normalised Values", BLANK_Normalized_Values)

SAMPLE_Normalized_Values = list(round(float(x/float(stats.tmean(min_value_float_list))), 4) for x in min_value_float_listS)

print("Sample Normalised Values", SAMPLE_Normalized_Values)


print("BLANK SEM %6.6f" %(stats.sem(BLANK_Normalized_Values)))
print("SAMPLE SEM %6.6f" %(stats.sem(SAMPLE_Normalized_Values)))


# Calculate the mean of every row in transfer_blank

transfer_blank_curve = []

#print(len(transfer_blank))

# Calculate the mean of every index in transfer_blank
for index in range(len(transfer_blank[0])):
    mean_value = 0
    for position in transfer_blank:
        mean_value += position[index]
    mean_value_index = mean_value / len(transfer_blank)
    transfer_blank_curve.append(mean_value_index)

#print(transfer_blank_curve) 

# Calculate the mean of every row in transfer_sample

transfer_sample_curve = []

#print(len(transfer_sample))

# Calculate the mean of every index in transfer_sample
for index in range(len(transfer_sample[0])):
    mean_value = 0
    for position in transfer_sample:
        mean_value += position[index]
    mean_value_index = mean_value / len(transfer_blank)
    transfer_sample_curve.append(mean_value_index)

#print(transfer_sample_curve) 
column_vgate = np.float64(column_vgate)
#print(column_vgate[::10])
rounded_column_vgate = np.round(column_vgate, decimals=2)


if p_value > 0.05:
    p_value = 'p-value = ns'
elif p_value <= 0.05 and not p_value <= 0.01:
    p_value = 'p-value = *'
elif p_value <= 0.01 and not p_value <= 0.001:
    p_value = 'p-value = **'
elif p_value <= 0.001 and not p_value <= 0.0001:
    p_value = 'p-value = ***'
elif p_value <= 0.0001:
    p_value = 'p-value = ****'



# Plot the results
rounded_vg = [round(float(s), 2) for s in column_vgate]
#print(rounded_vg)
string_vg = [str(x) for x in rounded_vg]



plt.plot(column_vgate, transfer_blank_curve, 'k-', label='Transfer Blank Curve')
plt.plot(column_vgate, transfer_sample_curve, 'r-', label='Transfer Sample Curve')
plt.xlabel('[Vg]')
plt.ylabel('Current [\u03BCA]')
plt.xticks(rounded_column_vgate[::30], rotation = 45)
plt.text(0.3, ((mean_first_value_ch_no_outliers)-10),  str(p_value))
plt.legend()
plt.savefig('plot.pdf')


