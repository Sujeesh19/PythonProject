class StudentData:
    def __init__(self, name, rollno, mark1, mark2):
        self.name = name
        self.rollno = rollno
        self.mark1 = mark1
        self.mark2 = mark2
    def display(self):
        print(self)

    def search(self, myData):
        if self in myData:
            return True
        else:
            return False

    def delete(self, myData):
        if self in myData:
            del myData[rollno]
            return True
        else:
            return False

    def update(self, myData):
        if self in myData:
            print('''What you have to update
                                1. Update Name
                                2. Update Roll No.
                                3. Update Mark1
                                4. Update Mark2''')
            choice = int(input("Enter your choice to update the value: "))
            if choice == 1:
                newName = input("Enter the new Name: ")
                myData[self][0] = newName
            elif choice == 2:
                newRollNo = int(input("Enter the new Roll No. : "))
                myData[newRollNo] = myData[self]
                del myData[self]
            elif choice == 3:
                newMark1 = int(input("Enter the new Marks 1: "))
                myData[self][1] = newMark1
            elif choice == 4:
                newMark2 = int(input("Enter the new Marks 2: "))
                myData[self][2] = newMark2
        else:
            print("Please Enter Correct Roll No.")

myData = {}
while True:
    print('''\t\t\t1. Adding new Entry
    \t\t2. Display Student Data
    \t\t3. Searching in Student Data
    \t\t4. Deleting a record
    \t\t5. Updating existing record
    \t\t6. Press any key to exit''')
    print()
    choice = int(input("Enter Your choice: "))
    if choice == 1:
        name = input("Enter the Name: ")
        rollno = int(input("Enter the Roll No. : "))
        mark1 = int(input("Enter the mark1: "))
        mark2 = int(input("Enter the mark2: "))
        StudentData(name, rollno, mark1, mark2)
        myData[rollno] = [name, mark1, mark2]
        print()


    elif choice == 2:
        StudentData.display(myData)
        print()


    elif choice == 3:
        rollno = int(input("Enter the Roll No. to be searched: "))
        if StudentData.search(rollno, myData):
            print(rollno," Found in Student data")
        else:
            print(rollno, "Not Found")
        print()


    elif choice == 4:
        rollno = int(input("Enter the Roll No. to be delete: "))
        if StudentData.delete(rollno, myData):
            print(rollno, "is deleted Successfully from Student  Data")
        else:
            print("Enter correct Roll No")
        print()


    elif choice == 5:
        rollno = int(input("Enter the Roll No. to update: "))
        StudentData.update(rollno, myData)
        print()


    else:
        break


