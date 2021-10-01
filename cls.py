class Beach:
    location = 'Cape Cod'

# 1. attributes
cape_cod_beach = Beach()

# 2. new instance
beach2 = Beach()

print(cape_cod_beach.location, beach2.location)
cape_cod_beach.location = 'Cancun'
print(cape_cod_beach.location,beach2.location)

# 3. initialization
class Mountain:
    parts = ['tree', 'water'] # class variable
    def __init__(self, location, water_color, temperature): 
        self.location = location # cape_cod_beach(=self).location
        self.water_color = water_color # instance variables
        self.temperature = temperature
        self.heat_rating = 'cool' if temperature > 15 else 'cold'
        
    # 4. method
    def add_part(self, part): # to access the instance's property(parts, location, water_color ...)
        self.parts.append(part)


himalaya = Mountain('Himalaya', 'dark blue', -60)
hallasan = Mountain('Hallasan', 'crystal blue', 17)
print(himalaya.location, hallasan.location)
print(himalaya.heat_rating, hallasan.heat_rating)

# 4. method
print(himalaya.parts)
himalaya.add_part('rock')
print(himalaya.parts)