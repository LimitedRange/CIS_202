# This program calculates how much a customer spends on coffee per week.

# Named Constant for 7 days in a week.
DAYS_PER_WEEK = 7

# Ask customer how much they spend on coffe.
price_per_cup = float(input("Enter the price of one cup of coffee: "))
cups_per_day = int(input("Enter the number of cups you buy per day: "))

# Calculate daily and weekly coffee costs
daily_coffee_cost = price_per_cup * cups_per_day
weekly_coffee_cost = daily_coffee_cost * DAYS_PER_WEEK

# Display the results for customer with 2 decimal places.
print(f"\nDaily Coffee Cost: ${daily_coffee_cost:.2f}")
print(f"Weekly Coffee Cost: ${weekly_coffee_cost:.2f}")
