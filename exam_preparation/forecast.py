def forecast2(*data):
    result = []

    def add_locations(type_of_location):  # type of location = Sunny or Cloudy or Rainy
        locations = list(filter(lambda x: x[1] == type_of_location, data))
        [result.append(f"{l[0]} - {type_of_location}") for l in sorted(locations)]

    add_locations("Sunny")
    add_locations("Cloudy")
    add_locations("Rainy")

    return '\n'.join(result)


def forecast(*data):
    result = []

    def add_locations(type_of_location):  # type of location = Sunny or Cloudy or Rainy
        locations = []

        for location, weather in data:
            if weather == type_of_location:
                locations.append(location)

        for l in sorted(locations):
            result.append(f"{l} - {type_of_location}")

    add_locations("Sunny")
    add_locations("Cloudy")
    add_locations("Rainy")

    return '\n'.join(result)


print(forecast2(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
