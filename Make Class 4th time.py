#Encapsulation : การห่อหุ้ม ทำให้ไม่สามารถแก้ไขข้อมูลใน Class ได้
#Access Modifier : ระดับการเข้าถึง Class , Attribute , Method และอื่นๆ
#การสร้าง Class ชื่อจะต้องพิมพ์ใหญ่ก่อนเสมอ
class Employee:
        #Public Attribute
        def __init__(self,name,salary,department):
            print("Default Constructor")
            self.name = name
            self.salary = salary
            self.department = department
        #Public Method
        def showData(self):
            print("ชื่อพนักงาน : {}".format(self.name))
            print("เงินเดือน : {}".format(self.salary))
            print("ตำแหน่ง : {}".format(self.department))

#สร้างวัตถุ
obj1 = Employee("Tee",60000,"Content Creater")
obj1.showData()
obj2 = Employee("Natee",46000,"Video Editer")
obj2.department = "CEO"
obj2.showData()
obj3 = Employee("Nat",30000,"Drivers")
obj3.salary = 50000
obj3.showData()
obj4 = Employee("Phat",20000,"Chief")
#เปลี่ยนแปลงข้อมูล
obj4.name = "Pat"
obj4.showData()

#เช็คObject
print(isinstance(obj4,Employee))
print(isinstance(obj4,int))
print(isinstance(obj4,str))
print(dir(obj4))
print(obj4.__class__)