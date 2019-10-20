import csv
from functools import reduce

def Average(lst): 
    return reduce(lambda a, b: a + b, lst) / len(lst) 

with open('ukpostcodes.csv', 'r')  as ifp:
	postcode_areas = {}
	csv_reader = csv.DictReader(ifp)

	for row in csv_reader:
		postcode_area = row['postcode'].split(' ')[0]
		
		if postcode_area not in postcode_areas:
			postcode_areas[postcode_area] = {'lats': [], 'lngs': []}
		if (row['latitude'] != '' and row['longitude'] != ''):
			postcode_areas[postcode_area]['lats'].append(float(row['latitude']))
			postcode_areas[postcode_area]['lngs'].append(float(row['longitude']))

with open('region_postcodes.csv', 'w') as ofp:
	csv_writer = csv.DictWriter(ofp, fieldnames=['postcode_area', 'lat', 'lng'])
	csv_writer.writeheader()
	for area in postcode_areas:
		if len(postcode_areas[area]['lats']) > 0 and len(postcode_areas[area]['lngs']) > 0:
			lat = Average(postcode_areas[area]['lats'])
			lng = Average(postcode_areas[area]['lngs'])
			csv_writer.writerow({'postcode_area': area, 'lat': lat, 'lng': lng})
