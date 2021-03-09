class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        return f"The restaurant name is {self.restaurant_name}"

    def open_restaurant(self):\
        return f"The restaurant {self.restaurant_name} is open"

#Instance
napoli = Restaurant("Napoli","italian Food")
#Attributes
print(f"Restaurant: {napoli.restaurant_name}")
print(f"Cuisine type of {napoli.restaurant_name} is {napoli.cuisine_type}")
#Methods
print(napoli.describe_restaurant())
print(napoli.open_restaurant())