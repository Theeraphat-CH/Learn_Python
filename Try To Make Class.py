class Student:
    def detail(self,id,name):
        self.id = id
        self.name = name 
    def showData(self):
        print(" ID : {}".format(self.id))
        print(" Name : {}".format(self.name))
        
s01 = Student()
s01.detail("S01","Theeraphat Chueanokkhum")

s01.showData()
