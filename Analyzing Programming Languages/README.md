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
