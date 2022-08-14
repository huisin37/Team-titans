# Team-titans



# Sprint 2
## Missing Value Treatment
### Determine which column has missing values
print(df.isnull().sum())

### Remove the column as pproximately 70% are missing values
updated_df = df.dropna(axis=1)
print(updated_df.info())


## Outlier Analysis
from scipy import stats
import numpy as np

### Find Z-score for Duration
z1 = np.abs(stats.zscore(df['Duration']))
print(z1)

threshold = 3

### Position of the outlier for Duration
print(np.where(abs(z1) > 3))

### Find Z-score for Net Sales
z2 = np.abs(stats.zscore(df['Net Sales']))
print(z2)

threshold = 3

### Position of the outlier for Net Sales
print(np.where(abs(z2) > 3))

### Find Z-score for Commision
z3 = np.abs(stats.zscore(df['Commision (in value)']))
print(z3)

threshold = 3

### Position of the outlier for Commision
print(np.where(abs(z3) > 3))

### Find Z-score for Age
z4 = np.abs(stats.zscore(df['Age']))
print(z4)

threshold = 3

### Position of the outlier for Age
print(np.where(abs(z4) > 3))


# Sprint 5
## Pivot Tables
### Pivot Table 1 (Claim frequency of each agency)
![](Images/PivotTable1.png)

### Pivot Table 2 (Claim frequency of specific destinations with duration = 60)
![](Images/PivotTable2.png)


## One Way Analysis
### Airlines
![](Images/OneWay-Airlines.png)

### Travel Agency
![](Images/OneWay-TravelAgency.png)

### Destination
![](Images/OneWay-Destination.png)


## Two Way Analysis
### Airlines
![](Images/TwoWay-Airlines.png)

### Travel Agency
![](Images/TwoWay-TravelAgency.png)

### Destination
![](Images/TwoWay-Destination.png)
