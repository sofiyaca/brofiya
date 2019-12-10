import csv 
import json
import geocoder

def api_data():
	with open('locations.csv', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='|')
		locations = {}
		for row in reader:
			location = row[0] + ', ' + row[1]
			data = geocoder.arcgis(location).json
			locations.update({location: data})
		return locations

print(api_data())		

csv_headers = ['address', 'lat', 'lng']

with open('addresses.csv', 'w') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=csv_headers)
	writer.writeheader()
	for data in api_data():
		writer.writerow(data) 

