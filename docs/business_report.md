# Business Report

## Dataset Summary

Dataset: Olist Brazilian E-Commerce Dataset

Period:
2016 - 2018

Orders:
99,441

Customers:
99,441

Products:
32,951

---

## KPI Summary

Total Revenue:
15397738.61

Average Order Value:
136.6865389258766

Total Customers:
99441

Total Products Sold:
134936

---

## Top Customers By Revenue

Paste top 10 rows from gold_customer_revenue.csv

customer_id  total_orders  total_revenue
8475   1617b1357756262bfa56ab541c47bc16             1        13440.0
91284  ec5b2ba62e574342386871631fafd3fc             1         7160.0
76948  c6e2731c5b391845f6800c97401a43a9             1         6735.0
94398  f48d464a0baaea338cb25f816991ab1f             1         6729.0
24603  3fd6777bbce08a352fddd04e4a7cc8f6             1         6499.0
2049   05455dfa7cd02f13d132aa7a6a9729c6             1         5934.6
86248  df55c14d1476a9a3467f131269c2477f             1         4799.0
14182  24bbf5fd2f2e1b359ee7de94defc4a15             1         4690.0
86733  e0a2412720e9ea4f26c1ac985f6a7358             1         4599.9
23771  3d979689f636322c62418b6346b1c6d2             1         4590.0

## Top Products By Revenue

Paste top 10 rows from gold_product_revenue.csv

product_id   product_category_name  total_revenue
0  bb50f2e236e5eea0100680137654686c            beleza_saude       63885.00
1  6cdd53843498f92890544667809f1595            beleza_saude       54730.20
2  d6160fb7873f184099d9bc95e30376af                     pcs       48899.34
3  d1c427060a0f73f6b889a5c7c61f2ac4  informatica_acessorios       47214.51
4  99a4788cb24856965c36a24e339b6058         cama_mesa_banho       43025.56
5  3dd2a17168ec895c781a9191c1e95ad7  informatica_acessorios       41082.60
6  25c38557cf793876c5abdd5931f922db                   bebes       38907.32
7  5f504b3a1c75b73d6151be81eb05bdc9              cool_stuff       37733.90
8  53b36df67ebb7c41585e8d54d6772e08      relogios_presentes       37683.42
9  aca2eb7d00ea1a7b8ebd4e68314663af        moveis_decoracao       37608.90

## Revenue By State

Paste top 10 states from gold_state_revenue.csv

customer_state  total_revenue
0             SP     5202955.05
1             RJ     1824092.67
2             MG     1585308.03
3             RS      750304.02
4             PR      683083.76
5             SC      520553.34
6             BA      511349.99
7             DF      302603.94
8             GO      294591.95
9             ES      275037.31

## Monthly Revenue Trend

Paste monthly revenue summary from gold_monthly_revenue.csv

month_year  total_revenue
0    2017-11     1010271.37
1    2018-04      996647.75
2    2018-05      996517.68
3    2018-03      983213.44
4    2018-01      950030.36
5    2018-07      895507.22
6    2018-06      865124.31
7    2018-08      854686.33
8    2018-02      844178.71
9    2017-12      743914.17

## Conclusion

The Medallion Architecture successfully transformed raw e-commerce data into business-ready datasets.

The Gold layer enables customer analytics, product analytics, revenue analysis, and operational reporting.