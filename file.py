def main():
    menu()
    choose=int(input("Enter your choose: "))
    if choose==1:
        writefile()
    elif choose==2:
        readfile()
    elif choose==3:
        deletedata()
    elif choose==4:
        updatefile()
    elif choose==5:
        searchdata()
    elif choose==6:
        exit()
    else:
        print("Your entry is wroung!")
    main()
def writefile():
        id=input("Enter student id: ")
        name=input("Enter student name: ")
        department=input("Enter department of student: ")
        student_list=[id,name,department]
        with open("file.txt",'a') as w:
            for i in student_list:
                w.writelines(i)
                w.writelines("\t")
            w.writelines("\n")

def readfile():
    with open("file.txt",'r') as y:
        print(y.read())
def deletedata():
    id=input("Enter student id for delete: ")
    with open("file.txt",'r') as b:
        line=b.readlines()
    update_list=[]
    for i in line:
        if not i.startswith(id):
            update_list.append(i)
    with open("file.txt",'w')as n:
        n.writelines(update_list)
    if len(line)==len(update_list):
        print("file not found!!")
    else:
        print("delete is succeful!")
def updatefile():
    id=input("Enter id for update: ")
    with open("file.txt",'r') as t:
        line=t.readlines()
    update_list=[]
    for i in line:
        if not i.startswith(id):
         update_list.append(i)
    id_new=input("Enter new id for student: ")
    update_list.append(id_new)
    update_list.append("\t")
    name=input("Enter update name of student: ")
    update_list.append(name)
    update_list.append("\t")
    department=input("Enter update department: ")
    update_list.append(department)
    update_list.append("\t")
    with open("file.txt",'w')as u:
        u.writelines(update_list)
        u.writelines("\n")
def searchdata():
    id=input("Enter id for Search: ")
    with open("file.txt",'r')as w:
        line=w.readlines()
    for i in line:
        if i.startswith(id):
            print(i)
    print("search is succefuly!")
def menu():
    print('''&&&&&&&&&&&&&(SIMPLE STUDENT FILE)&&&&&&&&&&&&&&&&&&&
              1.write
              2.read
              3.delete
              4.update
              5.search
              6.exit from program
      &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
           ''')                           
main()


















