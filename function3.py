import os.path

def add_student():
  roll=input("Enter roll no: ")
  name=input("Enter name: ")
  course=input("Enter course: ")
  marks=input("Enter marks: ")

  with open("student.txt","a")as f:
     f.write(f"{roll},{name},{course},{marks}")
     print("\n Student record added Successfully\n")
     
# def view_stu():
#    if not os.path.exists("student.txt"):
#       print("No Student found\n")
#       return
#    with open("student.txt","r")as f:
#       lines=f.readlines()

#       if not lines:
#          print("\n No student to dispaly")
#       else:
#          print("\tRoll\tName\tCourse\tmarks") 
#          print("-"*40)    
#          roll,name,course,marks=lines.strip().split(",") 
#          print(f"{roll}\t{name}\t{course}\t{marks}")
#          print()

def view_stu():
    if not os.path.exists("student.txt"):
        print("No Student found\n")
        return

    with open("student.txt", "r") as f:
        lines = f.readlines()

    if not lines:
        print("\nNo student to display")
    else:
        print("\tRoll\tName\tCourse\tMarks")
        print("-" * 40)
        for line in lines:
            roll, name, course, marks = line.strip().split(",")
            print(f"\t{roll}\t{name}\t{course}\t{marks}")
        print()

def delete_stu():
   roll_no=input("enter roll no u want to delete: ")

   if not os.path.exists("student.txt"):
      print("\n Student data not Found")
      return
   with open("student.txt","r")as f:
      lines=f.readlines()

      found=False
      with open("student.txt","w")as f:
         for l in lines:
            roll,name,course,marks=l.strip().split(",")
            if roll!=roll_no:
               f.write(l)
            else:
               found(True)
      if found:
         print("\nStudent Deleted Successfully")
      else:
         print('\nStudent Not Found\n')

def main():
   while True:
      print("--------------All STUDENT OPERATIONS------------")
      print("1. Add Student")
      print("2. View Student")
      print("3. Delete Student")
      print("4. Exit")
      ch=input("Enter your choice: ")
      if ch=="1":
         add_student()
      elif ch=="2":
         view_stu()
      elif ch=="3":
         delete_stu()
      elif ch=="4":
         print("THANKS FOR CHOOSING OPERATION")
         break
      else:
         print("Invalid Input")
         
         
            
if __name__=='__main__':
   main()