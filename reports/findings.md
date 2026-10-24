
# Customer Churn Analysis — Initial Findings

## 1. Project Overview

The objective of this project is to analyze customer churn patterns and identify customer segments that may benefit from retention strategies.

Dataset: IBM Telco Customer Churn  
Initial dataset size: 7,043 customers and 21 columns.

## 2. Data Quality

- Converted `TotalCharges` to a numeric data type.
- Identified 11 missing `TotalCharges` values.
- Replaced these values with zero for customers whose tenure was zero, based on an explicit assumption.
- Preserved all 7,043 customer records.
- No duplicate rows were identified.
- The original raw dataset remains unchanged.

## 3. Key Findings

### Contract Type

| Contract | Churn Rate |
|---|---:|
| Month-to-month | 42.71% |
| One year | 11.27% |
| Two year | 2.83% |

Month-to-month customers have the highest churn rate. Their churn rate is approximately 15 times that of two-year contract customers.

### Payment Method

| Payment Method | Churn Rate |
|---|---:|
| Electronic check | 45.29% |
| Mailed check | 19.11% |
| Bank transfer (automatic) | 16.71% |
| Credit card (automatic) | 15.24% |

Electronic-check customers have the highest observed churn rate. Further analysis is needed to determine whether this pattern is associated with contract type, tenure, or other customer characteristics.

### Monthly Charges

| Metric | Stayed | Churned |
|---|---:|---:|
| Mean | 61.27 | 74.44 |
| Median | 64.43 | 79.65 |

Customers who churned had higher average and median monthly charges than customers who stayed. This association warrants further investigation.

## 4. Business Recommendations

1. Investigate retention opportunities for month-to-month customers.
2. Explore optional automatic-payment enrollment incentives for electronic-check customers.
3. Investigate whether higher monthly charges are associated with particular service packages or customer segments.
4. Test retention interventions and measure their impact before making broad policy changes.

## 5. Limitations

- These findings describe associations and do not establish causation.
- Differences in customer tenure, contract type, and services may influence the observed patterns.
- The zero-charge treatment for zero-tenure customers is an assumption that should be documented and validated.
- No predictive model or financial impact estimate has been evaluated yet.

## 6. Next Steps

- Perform additional segment-level analysis.
- Use SQL to answer business questions.
- Build a churn dashboard.
- Compare predictive models using appropriate evaluation metrics.
- Develop and evaluate targeted retention recommendations.


## 7. SQL Analysis Results

SQL was used to validate the overall churn rate and compare churn across contract types, payment methods, and tenure groups.

### Overall Churn
- Total customers: 7,043
- Customers churned: 1,869
- Overall churn rate: 26.54%

### Tenure Analysis
Customers with 0–12 months of tenure had the highest churn rate at 47.44%. Churn declined across longer-tenure groups, reaching 9.51% among customers with 49 or more months of tenure.

### Contract Analysis
Month-to-month customers had a churn rate of 42.71%, compared with 11.27% for one-year contracts and 2.83% for two-year contracts.

### Payment Method Analysis
Electronic-check customers had the highest churn rate at 45.29%. Automatic credit-card customers had the lowest rate among the four payment methods at 15.24%.

### Customer Profile Comparison
Churned customers had average monthly charges of 74.44 and average tenure of 17.98 months. Retained customers had average monthly charges of 61.27 and average tenure of 37.57 months.

### Recommended Next Steps
1. Investigate early-tenure customer churn and onboarding experience.
2. Evaluate retention offers for month-to-month customers.
3. Investigate payment-method and service-package differences.
4. Validate these associations through deeper analysis and controlled retention experiments.

These findings are descriptive. They do not establish that any single factor causes churn.
