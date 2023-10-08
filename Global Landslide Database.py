import requests
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://data.nasa.gov/resource/dd9e-wu2v.json'
response = requests.get(url)
data = response.json()
data_df = pd.DataFrame(data)


countries_list = list(data_df['country_name'])
landSlide_per_country = {}

for country in countries_list:
    if country in landSlide_per_country.keys():
        landSlide_per_country[country] += 1
    else:
        landSlide_per_country[country] = 1


sorted_landSlide_per_country = dict(sorted(landSlide_per_country.items(), key=lambda item: item[1]))

landSlideCount = list(sorted_landSlide_per_country.values())
countries = list(sorted_landSlide_per_country.keys())



# Convert countries to strings
countries = [str(country) for country in countries]


plt.barh(countries, landSlideCount, height = .6)
plt.xlabel('Frequency')
plt.ylabel('Countries')
plt.title('Global Landslide Locations')
plt.show()
