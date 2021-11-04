# fav_langs = {
#     "ash": ["python", "ruby"],
#     "wil": ["basic", "r"],
#     "dan": ["python"],
#     "suz": ["c", "ruby"]
# }

# poll_takers = ["ash", "bri", "cam", "dan", "edd"]

# for name, languages in fav_langs.items():
#     if len(languages) == 1:
#         print(f"{name.title()}'s favorite language is:'")
#     else:
#         print(f"{name.title()}'s favorite languages are:'")
#     for language in languages:
#         print(f"\t{language.title()}")

# aliens = []

# for alien_num in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# for alien in aliens[:5]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
# for alien in aliens[:10]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15


# print(aliens[:10])

# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeston',
#     },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#     }
# }

# for username, user_info in users.items():
#     print(f'\nUsername: {username}')
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
#     print(f'\tFull Name: {full_name.title()}')
#     print(f'\tLocation: {location.title()}')

# people = {
#     "ash": {
#         "first": "ash",
#         "last": "hits",
#         "city": "austin",
#         "job": "ux",
#     },
#     "jeb": {
#         "first": "jeb", 
#         "last": "stone", 
#         "city": "austin", 
#         "job": "ds"
#         },
# }


# for name, details in people.items():
#     print(name.title())

# pets = {
#     "joe": {
#         "owner_first": "ash",
#         "owner_last": "hits",
#         "city": "austin",
#     },
#     "d'angelo": {
#         "owner_first": "tom", 
#         "owner_last": "harris", 
#         "city": "austin",
#     },
#     "zuko": {
#         "owner_first": "larissa", 
#         "owner_last": "parisien", 
#         "city": "new rochelle",
#     },
# }


# for pet, details in pets.items():
#     print(pet.title())
#     fullname = 
#     print(f'')
#     print

cities = {
    "austin": {
        "pop": 1000000,
        "state": "tx",
        "region": "sw",
    },
    "new york city": {
        "pop": 10000000,
        "state": "ny",
        "region": "ne",
    },
    "atlanta": {
        "pop": 5000000,
        "state": "ga",
        "region": "se"
    }
}

for city, info in cities.items():
    pop = info['pop']
    state = info['state']
    region = info['region']
    print(f'The city is {city.title()}.')
    print(f"{city.title()}'s population is {pop}")
    print(f"{city.title()} is in {state.upper()} in the {region.upper()} region.")
