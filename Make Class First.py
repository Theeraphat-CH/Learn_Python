#การสร้าง Class ชื่อจะต้องพิมพ์ใหญ่ก่อนเสมอ
class Employee:
    #สร้าง Method
    def detail(self):
        print("เรียกใช้งาน Method ใน Class Employee")
        self.name = "Theeraphat Chueanokkhum"
        self.salary = 35000
        print("กำหนดคุณสมบัติเรียบร้อย")
        print("ชื่อพนักงาน : {}".format(self.name))
        print("เงินเดือน : {}".format(self.salary))

#สร้างวัตถุ
obj1 = Employee()
obj1.detail()

obj2 = Employee()
obj2.detail()

obj3 = Employee()
obj3.detail()