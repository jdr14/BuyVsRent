import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

"""
Formula:
M = P * [ r(1+r)^n / ((1+r)^n - 1) ]

M = Total Monthly P & I Payment
P = Loan amount (principal)
r = Monthly interest rate - (APR % / 100) / 12 (months)
n = Number of payments total - 30 (years) * 12 (months)
"""


# ---- Inputs ----
P = 400000   # principal
APR = 0.06             # 6% interest
term_years = 30

# ---- Derived ----
r = APR / 12
n = term_years * 12

# Monthly payment formula
M = P * (r * (1+r)**n) / ((1+r)**n - 1)

print(f"Monthly Payment: ${M:.2f}\n")

# ---- Amortization Loop ----
balance = P
interest_paid = []
principal_paid = []
balances = []

for m in range(n):
    interest = P * r
    principal = M - interest
    balance -= principal
    
    interest_paid.append(interest)
    principal_paid.append(principal)
    balances.append(balance if balance > 0 else 0)

# ---- Plot ----
plt.figure(figsize=(12,6))
plt.plot(interest_paid, label="Interest Portion Per Month")
plt.plot(principal_paid, label="Principal Portion Per Month")
plt.title("Mortgage Payment Breakdown Over Time")
plt.xlabel("Month")
plt.ylabel("Dollar Amount ($)")
plt.legend()
plt.grid(True)
plt.show()
