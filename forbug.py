# Finance Bug Testing File

# Bug 1: Already fixed - loop starts from 0 ✓
for i in range(0,10):
    print(i)

# Bug 2: Fixed - Changed to >= operator ✓
def calculate_tax(income):
    if income >= 50000:  # Fixed: changed from > to >=
        return income * 0.3
    else:
        return income * 0.2

# Bug 3: Fixed - Added f-string prefix ✓
def format_currency(amount):
    return f"Total: ${amount}"  # Fixed: added f prefix

print(calculate_tax(50000))
print(format_currency(1234.56))
