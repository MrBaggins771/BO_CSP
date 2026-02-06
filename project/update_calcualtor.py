# BO 3 Updated Finacial Calculator

def question(bill):
    cost = float(input(f"What is your monthly {bill}? $"))
    return cost

def percent(bill, income):
    cash_percent = round((bill/income)*100, 2)
    return cash_percent

def tell(cost, cash, percent):
    print(f"Your monthly {cost} is ${cash}, which is %{percent} of your income.")

income = question("income")
m_housing = question("housing cost")
m_utilities = question("utilities bill")
m_groceries = question("grocery bill")
m_transit = question("transit cost")

saving = income * .15
spending = income - (saving + m_housing + m_utilities + m_groceries + m_transit)

h_percent = percent(m_housing, income)
u_percent = percent(m_utilities, income)
g_percent = percent(m_groceries, income)
t_percent = percent(m_transit, income)

tell("housing cost", m_housing, h_percent)
tell("utilities bill", m_utilities, u_percent)
tell("grocery bill", m_groceries, g_percent)
tell("transit cost", m_transit, t_percent)
print(f"You should save ${saving}, which is 15% of you income.")

if spending < 0:
    print(f"You're in debt ${spending}... sad")
else:
    print(f"You have ${spending} left to spend")