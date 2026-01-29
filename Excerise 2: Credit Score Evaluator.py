# Excerise 2: Credit Score Evaluator 
# Prompt for a credit score (int, asssume 300-850 raneges)
score = int(input("What's your credit score (300-850): "))

# Use conditions to categorize 
if score < 300 or score > 850:
    category = "Invalid score"
else: 
    if score >= 750:
        result = "Excellent - Loan Approved"
        approved = True
    elif 700 <= score < 750:
        result = "Good - Loan Approved with Review"
        approved = True
    elif 600 <= score < 700:
        result = "Fair - Loan Conditional"
        approved = False
    else: 
        result = "Poor - Loan Denied"
        approved = False

# Loan Message
if approved:
    print(f"{result}. Intrest rate: Low")
else:
    print(f"{result}. Seek credit improvement.")