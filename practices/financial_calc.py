# BO financial calculator

m_income = float(input("What is your monthly income: $"))
housing = float(input("what is your monthy housing cost (rent or mortgage): $"))
utilities = float(input("What is your monthly utility cost: $"))
groceries = float(input("What is your monthly grocery cost: $"))
transportation = float(input("What is your monthy transit cost (buses ot car payment): $"))

h_percent = round((housing/m_income)*100, 2)
u_percent = round((utilities/m_income)*100, 2)
g_percent = round((groceries/m_income)*100, 2)
t_percent = round((transportation/m_income)*100, 2)
invest = round(float(m_income*.15), 2)

print("Your housing is $", housing, "which is", h_percent, "%", "of your income")
print("Your utilities are $", utilities, "which is", u_percent, "%", "of your income")
print("Your groceries are $", groceries, "which is", g_percent, "%", "of your income")
print("Your transportation is $", transportation, "which is", t_percent, "%", "of your income")

print("You should invest $", invest, "which is 15% of your income.")