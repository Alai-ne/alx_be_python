income = float(input("Enter your monthly income: "))
expense = float(input("Enter your total monthly expense: "))
monthly_saving = income  - expense
print(f"your  monthly savings are ${ monthly_saving:.2f}." )
interestrate = 0.05
annual_saving_without_interest = monthly_saving * 12
Projected Savings = annual_saving_without_interest + annual_saving_without_interest * interestrate
print(f"Projected savings after one year, with interest, is: ${Projected _savings:.2f}")
