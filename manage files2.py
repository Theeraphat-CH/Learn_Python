textfw = open()

while True:
    studyid = input("Input Student ID : ")
    if studyid == "exit":
        break
    score = input("Enter Score : ")
    textfw.writelines(studyid+"\t"+score+"\n")
    
textfw.close()
textfr = open()
grade = None
for line in textfr.readlines():
    scores = line[-4:].strip()
    studentid = line[:-4].strip()
    #print("ID : ",studentid," Score ==> ",scores)
    scores = int(scores)
    if scores >= 80:
        grade = "A"
    elif scores >= 70 and scores < 80:
        grade = "B"
    elif scores >= 60 and scores < 70:
        grade = "C"
    elif scores >= 50 and scores < 60:
        grade = "D"
    elif scores < 50:
        grade = "F"
    print("ID : ",studentid," Score ==> ",scores," Grade ==> ",grade)

    textfw = open()
    textfw.writelines("ID : "+studentid+" Score ==> "+str(scores)+" Grade ==> "+grade+"\n")
textfw.close()