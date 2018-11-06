import tmdbsimple as tmdb
import http.client
import webbrowser
import requests
import json
import csv
from tmdbv3api import Movie
from tmdbv3api import TMDb


#establishing the connection
conn = http.client.HTTPSConnection("api.themoviedb.org")
payload = "{}"

#copy of the API key for further use and queries
tmdb.API_KEY ='cc3e54bdd37c85826e15195a8f8a49df'

# conn.request("GET", "/3/authentication/token/new?api_key=cc3e54bdd37c85826e15195a8f8a49df", payload)
# res = conn.getresponse()
# token = res.read()
# reslist = token.decode("utf-8").split('"')
# token = reslist[9]

#token copied from execution of the previous lines of code,
# since first I need to obtain authentication and then use the token to actually query the API
token = "300494ea33952f03dbcc060cdf7d75473ee5f4dc"
print("token")
print(token)
#webbrowser.open('https://www.themoviedb.org/authenticate/'+token)

payload = "{}"

# conn.request("GET", "/3/authentication/session/new?request_token="+token+"&api_key=cc3e54bdd37c85826e15195a8f8a49df", payload)
# res = conn.getresponse()
# data = res.read()
# sessionid = data.decode("utf-8").split('"')

#session id was obtained in the same way I did for token by executing commented code above
sessionid = "e193fb83b8be4bd5be9dc4d7776c48e8a2f33425"
print("session id")
print(sessionid)


#since the 3 version of TMDB API that I was using 
#did not give a possibility to query all the list at once
#I needed to query single page at a time
conn.request("GET", "/3/account/%7Baccount_id%7D/favorite/movies?page=1&sort_by=created_at.asc&language=en-US&session_id="+sessionid+"&api_key=cc3e54bdd37c85826e15195a8f8a49df&output=json", payload)
res = conn.getresponse()
data = res.read().decode("utf-8")
datares = json.loads(data)
#print(datares)
movielist1 =datares['results']
#print("PAGE 1")
#print(movielist)
conn.request("GET", "/3/account/%7Baccount_id%7D/favorite/movies?page=2&sort_by=created_at.asc&language=en-US&session_id="+sessionid+"&api_key=cc3e54bdd37c85826e15195a8f8a49df&output=json", payload)
res = conn.getresponse()
data = res.read().decode("utf-8")
datares = json.loads(data)
movielist2 = datares['results']
#print("PAGE 2")
#print(movielist)
conn.request("GET", "/3/account/%7Baccount_id%7D/favorite/movies?page=3&sort_by=created_at.asc&language=en-US&session_id="+sessionid+"&api_key=cc3e54bdd37c85826e15195a8f8a49df&output=json", payload)
res = conn.getresponse()
data = res.read().decode("utf-8")
datares = json.loads(data)
movielist3 = datares['results']
conn.request("GET", "/3/account/%7Baccount_id%7D/favorite/movies?page=4&sort_by=created_at.asc&language=en-US&session_id="+sessionid+"&api_key=cc3e54bdd37c85826e15195a8f8a49df&output=json", payload)
res = conn.getresponse()
data = res.read().decode("utf-8")
datares = json.loads(data)
movielist4 = datares['results']
conn.request("GET", "/3/account/%7Baccount_id%7D/favorite/movies?page=5&sort_by=created_at.asc&language=en-US&session_id="+sessionid+"&api_key=cc3e54bdd37c85826e15195a8f8a49df&output=json", payload)
res = conn.getresponse()
data = res.read().decode("utf-8")
datares = json.loads(data)
movielist5 = datares['results']
conn.request("GET", "/3/account/%7Baccount_id%7D/favorite/movies?page=6&sort_by=created_at.asc&language=en-US&session_id="+sessionid+"&api_key=cc3e54bdd37c85826e15195a8f8a49df&output=json", payload)
res = conn.getresponse()
data = res.read().decode("utf-8")
datares = json.loads(data)
movielist6 = datares['results']
conn.request("GET", "/3/account/%7Baccount_id%7D/favorite/movies?page=7&sort_by=created_at.asc&language=en-US&session_id="+sessionid+"&api_key=cc3e54bdd37c85826e15195a8f8a49df&output=json", payload)
res = conn.getresponse()
data = res.read().decode("utf-8")
datares = json.loads(data)
movielist7 = datares['results']
conn.request("GET", "/3/account/%7Baccount_id%7D/favorite/movies?page=8&sort_by=created_at.asc&language=en-US&session_id="+sessionid+"&api_key=cc3e54bdd37c85826e15195a8f8a49df&output=json", payload)
res = conn.getresponse()
data = res.read().decode("utf-8")
datares = json.loads(data)
movielist8 = datares['results']
conn.request("GET", "/3/account/%7Baccount_id%7D/favorite/movies?page=9&sort_by=created_at.asc&language=en-US&session_id="+sessionid+"&api_key=cc3e54bdd37c85826e15195a8f8a49df&output=json", payload)
res = conn.getresponse()
data = res.read().decode("utf-8")
datares = json.loads(data)
movielist9 = datares['results']
conn.request("GET", "/3/account/%7Baccount_id%7D/favorite/movies?page=10&sort_by=created_at.asc&language=en-US&session_id="+sessionid+"&api_key=cc3e54bdd37c85826e15195a8f8a49df&output=json", payload)
res = conn.getresponse()
data = res.read().decode("utf-8")
datares = json.loads(data)
movielist10 = datares['results']
conn.request("GET", "/3/account/%7Baccount_id%7D/favorite/movies?page=11&sort_by=created_at.asc&language=en-US&session_id="+sessionid+"&api_key=cc3e54bdd37c85826e15195a8f8a49df&output=json", payload)
res = conn.getresponse()
data = res.read().decode("utf-8")
datares = json.loads(data)
movielist11 = datares['results']
conn.request("GET", "/3/account/%7Baccount_id%7D/favorite/movies?page=12&sort_by=created_at.asc&language=en-US&session_id="+sessionid+"&api_key=cc3e54bdd37c85826e15195a8f8a49df&output=json", payload)
res = conn.getresponse()
data = res.read().decode("utf-8")
datares = json.loads(data)
movielist12 = datares['results']
conn.request("GET", "/3/account/%7Baccount_id%7D/favorite/movies?page=13&sort_by=created_at.asc&language=en-US&session_id="+sessionid+"&api_key=cc3e54bdd37c85826e15195a8f8a49df&output=json", payload)
res = conn.getresponse()
data = res.read().decode("utf-8")
datares = json.loads(data)
movielist13 = datares['results']
movielist = movielist1+movielist2+movielist3+movielist4+movielist5+movielist6+movielist7+movielist8+movielist9+movielist10+movielist11+movielist12+movielist13

#exporting the scraped data to the txt file
with open('moviedata.txt', 'w') as outfile:
    json.dump(movielist, outfile)
print(len(movielist))
outfile.close()

#set to create a list of paired movies by genre
paired = set()
tmdb1 = TMDb()
tmdb1.api_key = 'cc3e54bdd37c85826e15195a8f8a49df'

#creating the set of movies pairs if they both belong to the same genre
#for the movies with only one genre id I simply checked if they are equal
#while for the movies with more genre ids I gave more degrees of freedom 
#and checked if the movie genre is equal to the first or to the second genre
#which will probably be the main genres of a given movie
for m1 in movielist:
	for m2 in movielist:
		if(m1!=m2):
			if(len(m1['genre_ids'])<2 or len(m2['genre_ids'])<2):
				if(m1['genre_ids'][0]==m2['genre_ids'][0]):
					tup = (m1['title'],m2['title'])
					paired.add(tup)
			elif((len(m1['genre_ids'])>=2 and len(m2['genre_ids'])>=2)):
				if(m1['genre_ids'][0]==m2['genre_ids'][0] or m1['genre_ids'][1]==m2['genre_ids'][0]):
					tup = (m1['title'],m2['title'])
					paired.add(tup)
				

output =set()
for m in paired:
	if (m[1],m[0]) not in output:
		output.add(m)
print(len(output))	

#export the list of pairs as csv file	
with open('genreGraph.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(output)

csvFile.close()



