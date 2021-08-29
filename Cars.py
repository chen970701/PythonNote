class Car():  #可以不加括号 也可以加括号 class Car():
    def __init__(self,name,year):
        self.name=name
        self.year=year
    def log(self):
        print("{:#^10}这辆车已经开了{}年".format(self.name,self.year))



class ElectricCar(Car):
    def __init__(self, name, year,electric):
        super().__init__(name, year)
        self.electric=electric
    def log(self):
        super().log()
        print(self.name+"的电池容量围为"+str(self.electric))
        

        