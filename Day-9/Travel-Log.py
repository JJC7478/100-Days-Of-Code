travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#Function that allows new countries to be added to travel_log
def add_new_country(country, visit_number, city_names):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visit_number
    new_country["cities"] = city_names

    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)