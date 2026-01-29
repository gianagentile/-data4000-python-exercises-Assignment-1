# Exercise 4 Tax Bracket Determiner (Conditionals & Functions Returning Bool/Values)
# Define  a function get_tax_bracket(income) that takes income (float) and returns the bracket as str
def get_tax_bracket(income):
    if income < 0:
        return "Invalid Income."
    
#bracket 
    if income < 50000:
        bracket = "Low (10%)"
        rate = 0.10
    elif income < 100000:
        bracket = "Medium (20%)"
        rate = 0.20
    else:
        bracket = "High (30%)"
        rate = 0.30

#bonus deduction calculation
    deduction_note = " (Deduction Eligible)" if income % 2 == 0 else ""
    return bracket + deduction_note, rate

# main prompt 
income = float(input("Whats's your annual income: "))
bracket_info = get_tax_bracket(income)
if bracket_info == "Invalid Income.":
    print(bracket_info)
else:
    bracket, rate = bracket_info
    estimated_tax = income * rate
    print(f"Your tax bracket is: {bracket}")
    print(f"Estimated tax owed: ${estimated_tax:.2f}")