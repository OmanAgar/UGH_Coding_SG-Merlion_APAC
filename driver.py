class Driver:
    def __init__(self,fn,ln,a,pn,vn,p,n,m,s):
        self.info = {"First Name":fn,"Last Name":ln,"Age":a,
                    "Phone Number":pn,"Vehicle Number":vn,"People":p,"Notice":n}
        self.vehicle = {"Model":m,"Seats":s}
    def return_info(self):
        return self.info
    def return_vehicle(self):
        return self.vehicle
    def change_info(self,content,index):
        self.info.insert(content,index)
        self.info.pop(index+1)
        return self.info
    def change_info(self,content,index):
        self.info.insert(content,index)
        self.info.pop(index+1)
        return self.vehicle

def add_driver(Driver,fn,ln,a,pn,vn,p,n,m,s):
    return Driver(fn,ln,a,pn,vn,p,n,m,s)
