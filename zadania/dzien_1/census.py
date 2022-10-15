class Manager:
    def __init__(self):
        self.name = "Marian"


class Restaurant:
    def __init__(self):
        self.name = "SuperTruperZarcie"

    def get_manager(self):
        manager = Manager()
        return manager


class City:
    def __init__(self):
        self.name = "Cracow"

    def get_restaurant(self):
        zarcie = Restaurant()
        return zarcie


class Country:
    def __init__(self):
        self.name = "Poland"

    def get_city(self):
        cracow = City()
        return cracow


class Census:
    def __init__(self):
        pass

    def get_country(self):
        poland = Country()
        return poland


census = Census()

# person = census.get_country() \
#     .get_city() \
#     .get_restaurant() \
#     .get_manager()

# country = census.get_country()
# city = country.get_city()
# restaurant = city.get_restaurant()
# person = restaurant.get_manager()

person = census.get_country().get_city().get_restaurant().get_manager()

print(person.name)
