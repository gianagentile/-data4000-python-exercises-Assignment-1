# Prompt the user for revenue (float) and cost (float)
revenue = float(input("What's the revenue: "))
cost = float(input("What's the cost: "))

# Calculate profit = revenue - cost
profit = revenue - cost

# calculate margin = (profit / revenue) * 100, if reveue > 0 else print "Invalid revenue"
if revenue > 0:
    margin = (profit / revenue) * 100
    # Print the profit and margin
    print(f"Profit: {profit}")
    print(f"Margin: {margin}%")
else:
    print("Invalid revenue")    