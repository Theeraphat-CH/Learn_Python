textw = open("/storage/emulated/0/commandline.txt","w")

for i in range(1,8):
    textw.writelines("execute @e[typr=armor_stand] ~~~ detect ~~-1~ lapiz_ore 0 fill ~4~4~4 ~-4~-4~-4 carrots "+str(i)+" replace carrots "+str(i-1)+"\n")
    
textw.close()
textr = open("/storage/emulated/0/commandline.txt","r")

print(textr.read())