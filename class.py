class magari:
    def __init__(self, modelname,color,year,chasis_no,CC):
        self.model = modelname
        self.mycolor = color
        self.myyear = year
        self.mychasis_no = chasis_no
        self.myCC=CC
    def onyesha(self):
        print(self.model, self.mycolor, self.myyear, self.mychasis_no, self.myCC)
    #create an object
myobj=magari("Toyota","Blacked",2016,25852,"3200CC")
myobj.onyesha()