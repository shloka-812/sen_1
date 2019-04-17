from .models import Outbreak
import datetime

def changedate(wrongdate):
	date_time_obj = datetime.datetime.strptime(wrongdate, '%d %B %y').date()
	return date_time_obj
i=0
filename = "diseases.csv"
with open(filename, 'r') as f:
	fields = f.readline()
	while True:
			i=i+1
			line = f.readline()
			if line == "":
				break
			words = line.split(',')
			try:
				newdate=changedate(words[0])
				q=Outbreak(disease_name =words[1], no_of_deaths = words[3], no_of_affected = words[2], location = words[4],o_date = newdate)
				q.save()
			except:
				print(i)
