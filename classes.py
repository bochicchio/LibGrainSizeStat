# classes.py>

class data:
    def __init__(self, siteList):
        self.siteList = siteList

    def populate(self, siteList):       
        site.name = siteList[1]



        

class site(data):
    def __init__(self, latitude, longitude, name):
        self.latitude = latitude
        self.longitude = longitude
        self.name = name



# class sample(site):
#     def __init__(self,subName, date, sizeFraction, sampleWeight, percentRetained):
#         self.subName = subName
#         self.date = date
#         self.sizeFraction = sizeFraction
#         self.sampleWeight = sampleWeight
#         self.percentRetained = percentRetained






