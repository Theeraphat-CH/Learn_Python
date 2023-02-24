#open("ชื่อไฟล์","โหมด","เข้ารหัส")
textfw = open("/storage/emulated/0/command.txt","w")

for i in range(1,8):
    x = str(i)
    y = str(i-1)
    textfw.writelines("execute @e[type=armor_stand] ~~~ detect ~~-1~ lapiz_block 0 fill ~4~4~4 ~-4~-4~-4 wheat "+x+" replace "+y+" wheat"+"\n")
textfw.close()
textfr = open("/storage/emulated/0/command.txt","r") 
print(textfr.read())