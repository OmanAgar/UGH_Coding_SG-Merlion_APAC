class Rider:
    def __init__(self,fn,ln,a,pn):
        self.info = {"First Name":fn,"Last Name":ln,"Age":a,
                    "Phone Number":pn}
    def return_info(self):
        return self.info
    def change_info(self,content,index):
        self.info.insert(content,index)
        self.info.pop(index+1)
        return self.info

def make_rider(Rider,fn,ln,a,pn):
    return Rider(fn,ln,a,pn)