# Team-titans



# Sprint 2
## Missing Value Treatment
### Determine which column has missing values
print(df.isnull().sum())

### Remove the column as pproximately 70% are missing values
updated_df = df.dropna(axis=1)
print(updated_df.info())


## Outlier Analysis



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
