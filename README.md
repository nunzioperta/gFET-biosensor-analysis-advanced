
# Overview

This script processes and analyzes experimental data from two input text files (`BLANK.txt` and `SAMPLE.txt`) containing transfer curve measurements. The goal is to evaluate and compare the performance metrics (e.g., mean, standard deviation, outliers, and normalized values) of blank and sample data using statistical analysis and visualization.

The output includes:

- Statistical insights, including means, standard deviations, and p-values.
- A plot of the transfer curves for both blank and sample data, with normalized values and annotations for statistical significance.

# Features

- **File Parsing**: Extracts and organizes data from tab-delimited text files.
- **Outlier Removal**: Filters statistically significant outliers using standard deviation bounds.
- **Statistical Analysis**:
  - Mean and standard deviation calculations.
  - Paired t-test to evaluate the statistical significance of differences between the blank and sample data.
  - Normalization and computation of Standard Error of the Mean (SEM).
- **Data Visualization**: Generates a plot of the transfer curves for blank and sample data, annotated with statistical p-values.

# Requirements

## Python Libraries

- `numpy`
- `matplotlib`
- `scipy`
- `statistics`
- `sys`

Install the required libraries using:

```bash
pip install numpy matplotlib scipy
```

# Input Files

## Format

The script expects two input files:

- `BLANK.txt`
- `SAMPLE.txt`

Both files should follow a tab-delimited format:

- The first line contains column headers (ignored during processing).
- Data rows should include values for multiple channels (Ch1, Ch2, ..., Ch12) and a corresponding `Vg` column.

## Example Content

```
# Example header row
Vg	Ch1	Ch2	Ch3	Ch4	Ch5	Ch6	Ch7	Ch8	Ch9	Ch10	Ch11	Ch12
0.1	12.5	13.2	...	...
0.2	11.3	12.8	...	...
...
```

# Outputs

- **Statistical Metrics**: Printed to the console, including:
  - Mean, standard deviation, upper and lower bounds for each channel.
  - Normalized values and standard error of the mean.
  - p-value from the paired t-test.
- **Visualization**: A PDF plot (`plot.pdf`) that includes:
  - Transfer curves for both blank and sample data.
  - Annotated p-value indicating statistical significance.
  - X-axis labels for `Vg` and Y-axis labels for current values.

# Usage

## Command Line Execution

1. Place the `BLANK.txt` and `SAMPLE.txt` files in the same directory as the script.
2. Run the script:

```bash
python transfer_curve_analysis.py
```

## Customization

- **Stringency Levels**: Modify the multiplier for the standard deviation to adjust outlier sensitivity:

```python
upper_bound = mean + (stdev * STRINGENCY_FACTOR)
lower_bound = mean - (stdev * STRINGENCY_FACTOR)
```

- **Channel Selection**: To analyze specific channels, adjust the conditions under `if` statements.

# Example Output

## Statistical Insights

```
The mean of all first_value_ch values is: 15.4
The mean of all first_value_chxS values is: 14.8
The calculated SD of the first_value_ch is: 1.2
...
T-Statistic: 2.35
P-Value: 0.02
```

## Visualization

The plot (`plot.pdf`) shows the transfer curves for blank and sample data, along with statistical significance annotations.

# License

This project is licensed under the MIT License.

# Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.
