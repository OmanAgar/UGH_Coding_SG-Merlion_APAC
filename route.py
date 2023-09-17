import osmapi as osm , bs4 as bs , openrouteservice as ors , math
ors_key = "5b3ce3597851110001cf62488f97a0c484214cacb893f3be729f251a"

# coords use long1,lat1,long2,lat2
# coords = ((103.840724,1.427385),(103.835380,1.429710))
# print(f"Distance: {math.ceil(calc_duration(coords)['routes'][0]['summary']['distance']/1000*1000)/1000}km\n"+
#       f"ETA: {math.ceil(calc_duration(coords)['routes'][0]['summary']['duration']/60*100)/100} mins")

class Route:
    def __init__(self,lo1,la1,lo2,la2,driver,rider):
        self.lo1 = lo1
        self.la1 = la1
        self.la2 = la2
        self.lo2 = lo2
        self.formatted = ((lo1,la1),(lo2,la2))
        self.driver = driver
        self.rider = rider
    def setup_routes(self):
        try:
            client = ors.Client(key=ors_key)
            self.routes = client.directions(self.formatted)
            return True
        except:
            return False
    def return_duration(self):
        return math.ceil(self.routes['routes'][0]['summary']['duration']/60*100)/100
    def return_distance(self):
        return math.ceil(self.routes['routes'][0]['summary']['distance']/1000*1000)/1000

def make_route(lo1,la1,lo2,la2,driver,rider):
    return Route(lo1,la1,lo2,la2,driver,rider)
