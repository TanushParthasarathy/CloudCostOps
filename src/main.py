import json

with open("src/data/resources.json", "r") as file:
    resources = json.load(file)

total_cost = 0
potential_savings = 0

print("Cloud Cost Optimization Report")
print("--------------------------------")

for resource in resources:
    name = resource["name"]
    cpu = resource["cpu_utilization"]
    monthly_cost = resource["monthly_cost"]

    total_cost += monthly_cost

    print(f"Resource: {name}")
    print(f"CPU Utilization: {cpu}%")
    print(f"Monthly Cost: ${monthly_cost}")

    if cpu < 5:
        potential_savings += monthly_cost
        print("Recommendation: Consider stopping or downsizing this VM.")
        print(f"Potential Savings: ${monthly_cost}/month")

    print()

print("--------------------------------")
print(f"Total Cloud Cost: ${total_cost}/month")
print(f"Potential Savings: ${potential_savings}/month")