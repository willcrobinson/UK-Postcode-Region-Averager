# UK-Postcode-Region-Averager
Script to average longitudes/latitudes for postcode areas

## Purpose
I wrote this quick and dirty script to take a CSV of postcode location data (using a full postcode, e.g. AN1 1XX) and average out the longitude and latitudes to give me a rough longitude and latitude for the postcode region (e.g. AN1)

I realise this probably isn't the most scientific way of doing things and there's probably a better way to do this (probably by finding the center of the postcode region) but this data was good enough for my purposes.

## Input/Output
The script reads from a CSV file called `uk_postcodes.csv` which I downloaded from this page: https://www.freemaptools.com/download-uk-postcode-lat-lng.htm

It outputs to a file called `region_postcodes.csv`
