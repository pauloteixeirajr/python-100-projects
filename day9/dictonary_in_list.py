# Write a program that adds to a travel log.

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "number_of_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "number_of_visits": 6
    },
]


def add_new_country(country, num_visits, cities):
    travel_log.append({
        "country": country,
        "cities_visited": cities,
        "number_of_visits": num_visits
    })


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
