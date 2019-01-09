stock_dict = {'GM': 'General Motors',
              'CAT': 'Caterpillar',
              'EK': "Eastman Kodak",
              'GE': "General Electric"
              }

purchases = [('GE', 100, '10-sep-2001', 48),
             ('GM', 200, '11-sep-2007', 35),
             ('CAT', 100, '1-apr-1999', 24),
             ('GM', 50, '4-apr-1987', 53),
             ('EK', 450, '37-apr-1987', 13),
             ('GE', 200, '1-jul-1998', 56)]

# 1) We want individual output like this:
# I purchased General Electric stock on 10 - sep - 2001 for $4800
# 2) While also building up a collection we can loop over that contains each company and all the purchases we made of that company's stock
# report = {
#     "GE": [('GE', 100, '10-sep-2001', 48), ('GE', 200, '1-jul-1998', 56)],
#     "CAT": [('CAT', 100, '1-apr-1999', 24)]
# }
# so we can loop over that and generate a readable report in the terminal
report = {}
for purchase in purchases:
  abbrev = purchase[0]
  full_name = stock_dict[abbrev]
  no_of_shares = purchase[1]
  purch_date = purchase[2]
  purch_price = purchase[3]
  full_purchase_price = no_of_shares * purch_price
  print(f"I purchased {full_name} stock on {purch_date} for ${full_purchase_price}.")

  try:
    report[abbrev].append(purchase)
  except KeyError:
    report[abbrev] = list()
    report[abbrev].append(purchase)

for abbrev, purchases_list in report.items():
  print(f"-------{abbrev}-------")
  total_portfolio_stock_value = 0
  for purchase in purchases_list:
    total_portfolio_stock_value += purchase[1] * purchase[3]
    print(f"     {purchase}")
  print(f"Total value of stock in portfolio: ${total_portfolio_stock_value}\n\n")


# Comprehensions
flowers = ['Lily', 'Snapdragon', 'Rose', 'Tulip']
bees = ['bumblebee', "honeybee", "dobee", "Aybee"]

# flowers_quotes = []
# for flower in flowers:
#   flowers_quotes.append(f"{flower}s make me sneeze")

flowers_quotes = {f"{flower}s make me sneeze" for flower in flowers}
# print(flowers_quotes)

large_flowers = []
for flower in flowers:
  for bee in bees:
    large_flowers.append(f'The {bee} pollinates the {flower}.')

large_flowers = [
  f'The {bee} pollinates the {flower}.'
  for flower in flowers
  for bee in bees
]

print(large_flowers)

my_family = {
    'sister': {
        'name': 'Sarah',
        'age': 43
    },
    'mother': {
        'name': 'Judy',
        'age': 76
    },
    'father': {
        'name': 'Ray',
        'age': 79
    }
}

# The loop way
# family_stuff = set()
# for family_member, member_values in my_family.items():
#   family_stuff.add(f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old' )

# As a dict comprehension
family_stuff = {f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old' for (family_member, member_values) in my_family.items()}

print(family_stuff)

# If you've read this far, you rock. Now prove it by rewriting the stocks code with comprehensions instead of loops!'
