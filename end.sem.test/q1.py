"""
============================================================
Q1. August Sales Analysis
============================================================
You are analysing the daily sales of an e-commerce store for August.
The sales for the 31 days are provided in a list.

Program Requirements:
- Use the list:
  daily_sales = [1205, 986, 1354, 10535, 15741, 11200, 800, 
                 13056, 952, 1100, 1025, 8574, 14014, 9987, 
                 1238, 1458, 7803, 900, 13674, 14539, 13241, 
                 10886, 7541, 8743, 1482, 11523, 977, 12181, 
                 8903, 1008, 1530]

- Find the day with the highest sales
- Find the day with the lowest sales
- Calculate the average daily sales

Print the result exactly in this format:
    5 August has highest sales of $15741
    7 August has lowest sales of $800
    Average daily sales for August is $6714.71

Note:
- The first item in the list represents 1 August
- The average must be rounded to 2 decimal places

============================================================
"""

# ============================================================
# Step 1: Create the list
# ============================================================
daily_sales = [1205, 986, 1354, 10535, 15741, 11200, 800, 
                 13056, 952, 1100, 1025, 8574, 14014, 9987, 
                 1238, 1458, 7803, 900, 13674, 14539, 13241, 
                 10886, 7541, 8743, 1482, 11523, 977, 12181, 
                 8903, 1008, 1530]




# ============================================================
# Step 2: Find highest sales
# ============================================================
maximum=max(daily_sales)
print(daily_sales.index(maximum),"August has the highest sales at $",str(maximum))


# ============================================================
# Step 3: Find lowest sales
# ============================================================
minimum=min(daily_sales)
print(daily_sales.index(minimum),"August has the lowest sales at $",str(minimum))



# ============================================================
# Step 4: Calculate average sales (round to 2 decimal places)
# ============================================================

total=0
for smth in range(0,len(daily_sales)):
    val=int(daily_sales[smth])
    total+=val
avg=round(total/len(daily_sales),2)
print("The average of this months stocks were.. $",str(avg))
