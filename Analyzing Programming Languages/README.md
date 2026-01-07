# Project 73 - Analyzing Programming Languages

This project explores trends in programming languages over time using data from StackOverflow. We focus on visualizing the popularity of various languages and applying techniques to smooth time series data for clearer trend analysis.

## Dataset

The dataset used in this project (`QueryResults (1).csv`) contains monthly counts of posts for different programming languages on StackOverflow. It has the following columns:

- `m`: Date of the month (converted to `datetime` for analysis)
- `TagName`: Programming language name
- `Unnamed: 2`: Number of posts in that month

## Setup

The project uses Python with the following libraries:

```python
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
````

## Steps

### 1. Data Loading

The CSV file is read into a Pandas DataFrame:

```python
data_frame = pd.read_csv("QueryResults (1).csv")
```

### 2. Data Exploration

* Check the first and last rows: `data_frame.head()`, `data_frame.tail()`
* Check DataFrame dimensions: `data_frame.shape`
* Count non-null entries per column: `data_frame.count()`
* Find total posts per language: use `data_frame.groupby("TagName")["Unnamed: 2"].sum()`
* Find languages with fewest months of data: use `data_frame.groupby("TagName").count().idxmin()`

### 3. Data Cleaning

Convert the `m` column to datetime for better plotting:

```python
data_frame['m'] = pd.to_datetime(data_frame['m'])
```

### 4. Data Visualization

Using Matplotlib to plot the number of posts per language over time:

```python
languages = []
for lang in data_frame['TagName']:
    if lang not in languages:
        languages.append(lang)

plt.figure(figsize=(12, 6))
for lang in languages:
    lang_data = data_frame[data_frame['TagName'] == lang]
    x = lang_data['m']
    y = lang_data['Unnamed: 2'].rolling(window=9).mean()  # rolling mean smoothing
    plt.plot(x, y, label=lang)

plt.xlabel('Date')
plt.ylabel('Number of Posts')
plt.title('Posts Over Time')
plt.legend()
plt.show()
```

### 5. Smoothing Time Series

To reduce noise in monthly post counts, a **rolling mean** is applied:

```python
y_smoothed = lang_data['Unnamed: 2'].rolling(window=6, min_periods=1).mean()
```

This helps reveal long-term trends without short-term fluctuations.

## Notes

* The rolling mean window can be adjusted (6, 9, 12 months) depending on how smooth you want the trend.
* Matplotlib styling (colors, markers, line styles) can be customized for better readability.

## References

* [Pandas `rolling()` documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html)
* [Pandas `mean()` documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.window.rolling.Rolling.mean.html)
* [Matplotlib `plot()` documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)

```

---

If you want, I can also **add a “Summary of Insights” section** with example findings from this data, so your README looks complete like a mini report.  

Do you want me to do that?
```
