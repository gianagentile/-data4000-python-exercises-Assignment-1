#Exercise 5: Product Category Matcher
#getting and cleaning input 
product = input("What's the product name: ").strip().lower()
# category matching
if product.startswith("tech"):
    category = "High Margin"
elif product in ("electronics", "gadget"):
    category = "High Margin"
elif product in ("clothing", "apparel"):
    category = "Medium Margin"
elif product in ("food", "grocery"):
    category = "Low Margin"
else:
    category = "Uncategorized - Review Needed"

# Result 
print(f"Product: {product} | Category: {category}")
    