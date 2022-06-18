
# Use this to simulate getting random teperatures for any city
from random import randint

# TODO: Add validation for cities.

def get_temperature(city):
    """
    Returns a tuple of temperatures in fahrenheit and celcius
    """
    # TODO: Fetch real temperature from a weather service/api
    temp_f = randint(-3200, 11000)/100 # temparature in deg F upto 2 decimals
    temp_c = (temp_f - 32) * 5 / 9
    return temp_f, temp_c

def get_rel_humidity(city):
    """
    Returns a 2 decimal float which is relative humidity value.
    """
    # TODO: Fetch real temperature from a weather service/api
    return randint(0, 9900)/100 # temparature in  2 decimals