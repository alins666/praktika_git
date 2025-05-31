from mm import mm
from cm import cm
from dm import dm

meters = float(input("Введите количество метров: "))

print(f"{meters} метров = {mm.meters_to_millimeters(meters)} миллиметров")
print(f"{meters} метров = {cm.meters_to_centimeters(meters)} сантиметров")
print(f"{meters} метров = {dm.meters_to_decimeters(meters)} дециметров")
