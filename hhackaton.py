import osmapi as osm , bs4 as bs , openrouteservice as ors , math
ors_key = "5b3ce3597851110001cf62488f97a0c484214cacb893f3be729f251a"

##def calc_duration(coords):
##    client = ors.Client(key=ors_key)
##    routes = client.directions(coords)
##    return routes
###coords use long1,lat1,long2,lat2
##coords = ((103.840724,1.427385),(103.835380,1.429710))
##print(f"Distance: {math.ceil(calc_duration(coords)['routes'][0]['summary']['distance']/1000*1000)/1000}km\n"+
##      f"ETA: {math.ceil(calc_duration(coords)['routes'][0]['summary']['duration']/60*100)/100} mins")

class Driver:
    def __init__(self):
        self.info = {"First Name":"N/A","Last Name":"N/A","Age":0,
                    "Phone Number":"N/A","Vehicle Number":"N/A","People":0,"Notice":"N/A"}
        self.vehicle = {"Model":"N/A,"Seats":0}
    def return_info(self):
        return self.info
    def return_vehicle(self):
        return self.vehicle
    def add_info(self,fn,ln,a,pn,vn,p,n):
        self.info = {"First Name":fn,"Last Name":ln,"Age":a,
                    "Phone Number":pn,"Vehicle Number":vn,"People":p,"Notice":n}
        return
    def add_vehicle(self,m,s):
        self.vehicle = {"Model":m,"Seats":s}
        return

driverA = Driver
driverA.add_info(driverA,"Joxi","Han",14,"+65 8123 4567","ABC 1234D",3,"Dropping off another passenger")
driverA.add_vehicle(driverA,"Toyota 86",4)
print(str(driverA.return_info(driverA))+"\n"+
      str(driverA.return_vehicle(driverA)))
