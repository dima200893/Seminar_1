def generate_bonus_dict(names, rates, bonuses):
    return {name: rate * float(bonus.rstrip("%")) / 100
            for name, rate, bonus in zip(names, rates, bonuses)}


list_names = ["Alice", "Bob", "Charlie"]
list_rates = [1000, 2000, 1500]
list_bonuses = ["10.25%", "5.50%", "12.75%"]

result_dict = generate_bonus_dict(list_names, list_rates, list_bonuses)
print(result_dict)
