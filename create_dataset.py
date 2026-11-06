import csv
import random

# Set random seed
random.seed(10)

# Product names and prices
products = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Keyboard": 1000,
    "Mouse": 500,
    "Headphones": 2000
}

rows = []

# Generate 99 sales records
for i in range(1, 100):

    product = random.choice(list(products.keys()))
    quantity = random.randint(1, 10)
    price = products[product]

    total_sales = quantity * price

    rows.append([
        i,
        product,
        quantity,
        price,
        total_sales
    ])

# Add missing values
rows[5][1] = ""
rows[10][2] = ""
rows[15][3] = ""

# Add duplicate record
rows.append(rows[0].copy())

# Create CSV file
with open("sales_data.csv", "w", newline="") as file:

    writer = csv.writer(file)

    # Column headings
    writer.writerow([
        "Order_ID",
        "Product",
        "Quantity",
        "Unit_Price",
        "Total_Sales"
    ])

    writer.writerows(rows)

print("Sales dataset created successfully!")
print("Total records:", len(rows))
print("Total columns: 5")