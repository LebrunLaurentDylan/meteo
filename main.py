import requests
import pandas as pd
import matplotlib as plt
from matplotlib import pyplot as plt
import numpy as np
from localisation_data_manager import *
from datetime import datetime


ville = input("Rentrez le nom de la ville: (respectez les tirets et pas d'accents necéssaires)\n==>")
date_prevision = input("Rentrez le nombre de jour de prevision: (max = 16)\n==>")

url = api_url_construteur(ville, int(date_prevision))

response = requests.get(url)
print(response.status_code)
# print(response.content)
data = response.json()
# print("data :\n", data, "\n")


temperature = data['hourly']
plage_temperature = temperature['temperature_2m']
plage_date = temperature['time']
list_date = []
for date in plage_date:
    list_date.append(datetime.strptime(date, '%Y-%m-%dT%H:%M'))

print('date :\n', len(list_date), len(plage_temperature))
# print('température :\n', plage_temperature)
date_temperature = []
array_temperature = {"date": [], "temperature": []}
for date in list_date:
    array_temperature["date"].append(date)
for temp in plage_temperature:
    array_temperature["temperature"].append(float(temp))

meteo_df = pd.DataFrame.from_dict(array_temperature)
plt.ylabel(ville)
plt.scatter(meteo_df['date'], meteo_df['temperature'], color='red', marker="+")
plt.show()
