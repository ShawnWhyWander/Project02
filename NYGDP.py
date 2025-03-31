import json
import matplotlib.pyplot as plt

with open ("NY.GDP.MKTP.CD.customization", encoding = "utf-8") as file:
    data = json.load(file)


us_gdp = []

for record in data[1]:
    if record['country']['id'] == 'US':
        year = int(record['date'])
        gdp = record['value']
        if gdp is not None:
            us_gdp.append((year,gdp))

us_gdp.sort(key=lambda x: x[0])
years = [year for year, _ in us_gdp]
gdp_values = [gdp for _, gdp in us_gdp]
gdp_values = [g/1e12  for g in gdp_values]


plt.figure (figsize=(10,5))
plt.plot(years, gdp_values, marker='o')
plt.title("US GDP Growth Over Time")
plt.xlabel("Year")
plt.ylabel("GDP (Trillions USD)")
plt.tight_layout()

plt.savefig("us_gdp_growth.png", dpi=300)
plt.show()



'''
    print(type(data))
    print(len(data))
    print(type(data[0]))
    print(type(data[1]))

    print (json.dumps(data[1][0], indent =2))
'''