# Excersise 3: Customer Greeting Formatter 
# Define a function format_greeting(name, title="Customer") that takes a name (str), strips whitespace, titles it, splits to get first name if space-separated, and returns a formatted greeting like "Hello, FirstName (Title)!"
def format_greeting(name, title="Customer"):
    #cleaned extra spaces
    cleaned_name = name.strip()
    # handle empty input 
    if cleaned_name == "":
        return  "Hello Valued Customer"
    # capitalize each word in name 
    cleaned_name = cleaned_name.title()
    # split name into parts and get first name
    first_name = cleaned_name.split()[0]
    # return formatted greeting
    return f"Hello, {first_name} ({title})!"

# in main code prompt full name 
full_name = input("What's your full name: ")
greeting = format_greeting(full_name)
print(greeting)