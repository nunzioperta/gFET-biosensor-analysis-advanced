
from scipy.stats import ttest_rel
import statistics
import matplotlib.pyplot as plt
import numpy as np
import sys
from scipy import stats

# This script processes data from a graphene FET device, performs statistical analysis, 
# and plots relevant data curves for interpretation.

# Step 1: Open and Read Input Data
# The input file should contain tab-separated columns with voltage and current measurements.
with open('BLANK.txt', 'r') as file:
    # Initialize empty lists to store data for different channels
    column_vgate = []  # Gate voltage
    column_ch1 = []    # Channel 1 data
    column_ch2 = []    # Channel 2 data
    column_ch3 = []    # Channel 3 data
    column_ch4 = []    # Channel 4 data
    column_ch5 = []    # Channel 5 data
    column_ch6 = []    # Channel 6 data
    column_ch7 = []    # Channel 7 data
    column_ch8 = []    # Channel 8 data
    column_ch9 = []    # Channel 9 data
    column_ch10 = []   # Channel 10 data
    column_ch11 = []   # Channel 11 data
    column_ch12 = []   # Channel 12 data

    # Read the file line by line
    for line in file:
        # Skip lines starting with '#' as they are comments or metadata
        if line.startswith('#'):
            continue
        # Clean up the line by removing newline characters
        line = line.replace('\n', '')
        # Split the line into data fields using tab as the delimiter
        line_data = line.split('\t')
        
        # Append data to respective columns
        column_vgate.append(float(line_data[0]))
        column_ch1.append(float(line_data[1]))
        column_ch2.append(float(line_data[2]))
        column_ch3.append(float(line_data[3]))
        column_ch4.append(float(line_data[4]))
        column_ch5.append(float(line_data[5]))
        column_ch6.append(float(line_data[6]))
        column_ch7.append(float(line_data[7]))
        column_ch8.append(float(line_data[8]))
        column_ch9.append(float(line_data[9]))
        column_ch10.append(float(line_data[10]))
        column_ch11.append(float(line_data[11]))
        column_ch12.append(float(line_data[12]))

# Step 2: Data Processing and Analysis
# Example: Perform statistical tests to compare channels or calculate averages
# T-test compares means of two related channels to identify significant differences
t_stat, p_val = ttest_rel(column_ch1, column_ch2)

# Step 3: Data Visualization
# Plot the gate voltage vs current for all channels
plt.figure(figsize=(10, 6))

# Example plot for Channel 1
plt.plot(column_vgate, column_ch1, label="Channel 1 Current", linestyle='-', marker='o')

# Add labels and legend
plt.xlabel("Gate Voltage (V)")
plt.ylabel("Current (A)")
plt.title("Graphene FET - Gate Voltage vs Current")
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

# Step 4: Additional Calculations (if required)
# Example: Calculate mean and standard deviation for a specific channel
mean_ch1 = statistics.mean(column_ch1)
stddev_ch1 = statistics.stdev(column_ch1)

# Print the results for user interpretation
print(f"Mean Current (Channel 1): {mean_ch1} A")
print(f"Standard Deviation (Channel 1): {stddev_ch1} A")
print(f"T-statistic (Channel 1 vs Channel 2): {t_stat}")
print(f"P-value (Channel 1 vs Channel 2): {p_val}")
