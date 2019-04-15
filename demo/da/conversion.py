from .models import citymap,countrymap
import csv 
   
filename = "citytocoord.csv"
countrytemp = ""
with open(filename, 'r') as f:
	fields = f.readline()
	while True:
			line = f.readline()
			if line == "":
				break
			words = line.split(',')
			q=citymap(city=words[0],lat=words[1],lng=words[2])
			q.save()
			if (countrytemp != words[3]):
				countrytemp=words[3]
				r = countrymap(country=words[3],lat=words[1],lng=words[2])
				r.save()
