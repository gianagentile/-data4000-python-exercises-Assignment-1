#Bonus Challenge: Integrated Decision Tool
# profit check function 
def is_profitable(revenue, cost):
    return revenue > cost
# main function 
def main():
    revenue = float(input("Enter business revenue: "))
    cost = float(input("Enter businesscost: "))
    category = input("Enter product category: ").strip().lower()
    profit = revenue - cost
    if is_profitable(revenue, cost):
        print(f"The business is profitable with a profit of ${profit:.2f}.")
        
        # Determine decision based on category
        if category == "high margin":
            decision = "Reinvest in growth."
        elif category == "medium margin":
            decision = "Maintain current strategy."
        elif category == "low margin":
            decision = "Consider cost-cutting measures."
        else:
            decision = "Review product category performance."
        
        print(f"Suggested Action: {decision}")

    # if not profitable
    else:
        print(f"Business is not profitable. Loss: ${abs(profit):.2f}. Consider strategic changes.")

if __name__ == "__main__":
    main()