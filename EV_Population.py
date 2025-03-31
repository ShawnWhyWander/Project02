import csv
import matplotlib.pyplot as plt

#file = open("Electric_Vehicle_Population_Data.csv")
with open ("Electric_Vehicle_Population_Data.csv", newline ='', encoding = 'utf-8') as file:
    fileReader = csv.reader(file)
    next(fileReader)

    model_counts = {'bmw': 0, 'chevrolet': 0, 'hyundai': 0, 'mazda': 0, 'nissan': 0, 'tesla': 0, }
    
    for row in fileReader:
        make = row[6].lower()
        if make in model_counts:
            model_counts[make] += 1
        

'''
model_TESLA = 0
model_HYUNDAI = 0
model_BMW = 0
model_NISSAN = 0
model_MAZDA = 0
model_CHEVROLET = 0

for row in fileReader:
    if row[6].lower() == 'tesla':
        model_TESLA += 1
    if row[6].lower() == 'hyundai':
        model_HYUNDAI += 1
    if row[6].lower() == 'bmw':
        model_BMW += 1
    if row[6].lower() == 'nissan':
        model_NISSAN += 1
    if row[6].lower() == 'mazda':
        model_MAZDA += 1
    if row[6].lower() == 'chevrolet':
        model_CHEVROLET += 1
'''


    

#brands = ['BMW', 'Chevrolet', 'Hyundai',  'Mazda', 'Nissan', 'Tesla']
#counts = [model_BMW, model_CHEVROLET, model_HYUNDAI, model_MAZDA, model_NISSAN, model_TESLA]

brands = [brand.capitalize() for brand in model_counts]
counts = [model_counts[brand] for brand in model_counts]

plt.figure (figsize=(10,6))
bars = plt.bar(brands, counts, color = 'skyblue')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval+50, int(yval), ha='center', va='bottom', fontsize = 10)

plt.xlabel ('Car Brand')
plt.ylabel ('Number of Electric Cars')
plt.title ('Electric Vehicle Count by Brand in Washington State')
plt.xticks (rotation = 30)
plt.tight_layout()

plt.savefig("EV_Population.png", dpi=300)
plt.show()