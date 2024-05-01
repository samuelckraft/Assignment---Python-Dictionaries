#Task 1
weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

import copy

weekly_sales_copy = copy.deepcopy(weekly_sales)

weekly_sales_copy["Week 2"]["Electronics"] = 18000

print(weekly_sales_copy)