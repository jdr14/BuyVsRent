import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

"""
Formula:
M = P * [ r(1+r)^n / ((1+r)^n - 1) ]

M = Total Monthly P & I Payment
P = Loan amount (principal)
r = Monthly interest rate - (APR % / 100) / 12 (months)
n = Number of payments total - 30 (years) * 12 (months)
"""


# ---- Inputs ----
SALE_PRICE = 680000         # Dollars
ASSESSED_VALUE = SALE_PRICE # Assume it is sale price (for now)
DOWN_PAYMENT_PERCENT = 20   # %
DOWN_PAYMENT_USD = SALE_PRICE * (DOWN_PAYMENT_PERCENT / 100)
P = SALE_PRICE - DOWN_PAYMENT_USD   # principal
APR = 5.5        # % interest
term_years = 30  # For our purposes we are assuming fixed

# ---- Monthly Fixed Costs ($USD) ----
HOA_fees = 695
home_insurance = 250
# property_taxes = 406 (found on zillow)
# For property taxes, consider a Class 1B residential property for DC ($0.85 for first $2.5 million)
# We are also assuming that the sale price is the same as or close to 
# assessed real value which will land us a good approximate
property_tax_type_class_1b_washington_dc = 0.85
property_taxes_per_month = SALE_PRICE / 100 * property_tax_type_class_1b_washington_dc / 12
mortgage_insurance = 0

# ---- Derived ----
r = (APR / 100) / 12
n = term_years * 12

# Monthly payment formula
M = P * (r * (1+r)**n) / ((1+r)**n - 1)

# Factor in all other sunk costs/fees in to calculate actual monthly payment
fixed_monthly_costs = HOA_fees + home_insurance + property_taxes_per_month + mortgage_insurance
actual_monthly = M + fixed_monthly_costs

print(f"\nHome Sale Price: ${SALE_PRICE}\n")
print("===========================")
print(f"With a downpayment of {DOWN_PAYMENT_PERCENT}% or ${DOWN_PAYMENT_USD}")
print(f"Your Loan Amount (Principal) = {P}\n")

print("===========================")
print(f"Considering an {term_years} year fixed loan at an APR of {APR}%")
print(f"\nBase Monthly: ${M:.2f}\n")

print("===========================")
print("Considering the folloing fixed monthly sunk costs of")
print(f"HOA fees:     ${HOA_fees}")
print(f"Insurance:    ${home_insurance}")
print(f"Property Tax: ${property_taxes_per_month}")
# print("Excluding utilities, your actual monthly payment is")
print(f"\nActual Monthly: ${actual_monthly:.2f}\n")


# ---- Amortization Loop ----
balance = P
interest_paid = []
all_non_principal_payments = []
principal_paid = []
balances = []

for m in range(n):
    interest = P * r
    principal = M - interest
    P -= principal
    
    interest_paid.append(interest)
    principal_paid.append(principal)
    all_non_principal_payments.append(interest + fixed_monthly_costs)
    balances.append(P if P > 0 else 0)

# ---- Plot ----
plt.figure(figsize=(12,6))
plt.plot(all_non_principal_payments, label="Total Sunk Costs Per Month")
plt.plot(interest_paid, label="Interest Portion Per Month")
plt.plot(principal_paid, label="Principal Portion Per Month")
plt.plot([actual_monthly for i in range(n)], label="Total Monthly Payment")
plt.plot()
plt.title("Mortgage Payment Breakdown Over Time")
# plt.xlabel("Month")
plt.xlabel("Years")
x_ticks = np.arange(0, n+1, step=12)
xticks_label_years = range(0, term_years + 1)
plt.xticks(x_ticks, xticks_label_years)
# plt.xticks(range(0, n + 1, 12), range(0, term_years + 1))
plt.ylabel("Dollar Amount ($)")
y_ticks = np.arange(0, int(actual_monthly) + 1000, 200)
# yticks_label_years = range(0, 8000)
plt.yticks(y_ticks)
# plt.ylabel(range(0, actual_monthly + 500, 200), range(0, ))

plt.legend()
plt.grid(True)
plt.show()
