#การสร้าง Class ชื่อจะต้องพิมพ์ใหญ่ก่อนเสมอ
class Employee:
    #สร้าง Method
    def detail(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department    
    def showData(self):
        print("ชื่อพนักงาน : {}".format(self.name))
        print("เงินเดือน : {}".format(self.salary))
        print("ตำแหน่ง : {}".format(self.department))

#สร้างวัตถุ
obj1 = Employee()
obj1.detail("Tee",60000,"Content Creater")
obj2 = Employee()
obj2.detail("Natee",46000,"Video Editer")
obj3 = Employee()
obj3.detail("Nat",30000,"Drivers")

obj1.showData()
obj2.showData()
obj3.showData()