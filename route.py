import osmapi as osm , bs4 as bs , openrouteservice as ors , math
ors_key = "5b3ce3597851110001cf62488f97a0c484214cacb893f3be729f251a"

def calc_duration(coords):
    client = ors.Client(key=ors_key)
    routes = client.directions(coords)
    return routes
coords use long1,lat1,long2,lat2
coords = ((103.840724,1.427385),(103.835380,1.429710))
print(f"Distance: {math.ceil(calc_duration(coords)['routes'][0]['summary']['distance']/1000*1000)/1000}km\n"+
      f"ETA: {math.ceil(calc_duration(coords)['routes'][0]['summary']['duration']/60*100)/100} mins")
