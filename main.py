#!/usr/bin/env python3
import csv
from functools import reduce

def Average(lst): 
    return reduce(lambda a, b: a + b, lst) / len(lst) 

with open('ukpostcodes.csv', 'r')  as ifp:
	# Create an empty dictionary for each area
	postcode_areas = dict()
	csv_reader = csv.DictReader(ifp)
	for row in csv_reader:
		# Get the postcode area (e.g. AB0 from AB0 1XX)
		postcode_area = row['postcode'].split(' ')[0]
		
		# Only add the postcode area to the dict if it's one that we've not
		# seen before
		if postcode_area not in postcode_areas:
			postcode_areas[postcode_area] = {'lats': [], 'lngs': []}
		
		# If either the lat on lng is empty, ignore the row
		# Otherwise, add to the dict
		if (row['latitude'] != '' and row['longitude'] != ''):
			postcode_areas[postcode_area]['lats'].append(float(row['latitude']))
			postcode_areas[postcode_area]['lngs'].append(float(row['longitude']))

with open('region_postcodes.csv', 'w') as ofp:
	csv_writer = csv.DictWriter(ofp, fieldnames=['postcode_area', 'lat', 'lng'])
	csv_writer.writeheader()
	for area in postcode_areas:
		# Ignore any postcode areas that have no lats or lngs stored
		if len(postcode_areas[area]['lats']) > 0 and len(postcode_areas[area]['lngs']) > 0:
			lat = Average(postcode_areas[area]['lats'])
			lng = Average(postcode_areas[area]['lngs'])
			csv_writer.writerow({'postcode_area': area, 'lat': lat, 'lng': lng})
