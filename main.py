from mm import meters_to_millimeters
from cm import meters_to_centimeters
from dm import meters_to_decimeters
from km import meters_to_kilometers

meters = float(input("Введите количество метров: "))

print(f"{meters} метров = {meters_to_millimeters(meters)} миллиметров")
print(f"{meters} метров = {meters_to_centimeters(meters)} сантиметров")
print(f"{meters} метров = {meters_to_decimeters(meters)} дециметров")
print(f"{meters} метров = {meters_to_kilometers(meters)} километров")
