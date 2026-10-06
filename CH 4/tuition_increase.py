# This program calculates tuition yearly with a 3% increase per year.

# Named constant for tuition yearly percent increase.
INCREASE_RATE = 0.03

# Starting tuition cost
tuition = 8000.00

# Caluculate and display tuition for the next 5 years.
for year in range(1,6):
    tuition = tuition + (tuition * INCREASE_RATE)
    print(f"Year {year}: ${tuition:,.2f}")