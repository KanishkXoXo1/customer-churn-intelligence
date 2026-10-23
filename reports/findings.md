
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
