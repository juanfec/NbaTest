import urllib.request, json 
import findPairs
import sys

#we get the data in json an save it in a list
players = []
with urllib.request.urlopen("https://mach-eight.uc.r.appspot.com/") as url:
    players = json.load(url)["values"]
#create a separate list fot getting just the h_in values
l = list()
for i in players:
    l.append(int(i.get("h_in")))
#we need to sort the players list since the algoritm will sort it too
#in this part the may have an O complexity of O(n.logn)
players = sorted(players, key = lambda i: i['h_in'])
#the algoritm is going to find the index of the matching pairs
solution = findPairs.FindPairs(l,len(l),int(sys.argv[1])).findPairs()
if len(solution) > 0 :
    for i in solution:
        print(players[i[0]].get("h_in")+" "+players[i[0]].get("first_name") + " " + players[i[0]].get("last_name")+"          "+players[i[1]].get("h_in")+" "+players[i[1]].get("first_name")+" "+players[i[1]].get("last_name"))
else :
    print("No matches found")