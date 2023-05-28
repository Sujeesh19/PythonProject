class StudentData:
    def __init__(self, name, rollno, mark1, mark2):
        self.name = name
        self.rollno = rollno
        self.mark1 = mark1
        self.mark2 = mark2

    def display(mydata):
        for i in mydata:
            print("Roll No.: ", i.rollno, "\nName: ", i.name, "\nMark 1: ", i.mark1, "\nMark 2: ", i.mark2, "\n")

    def search(rollno, myData):
        for i in myData:
            if i.rollno == rollno:
                return [True, i]
        else:
            return [False]

    def delete(rollno, myData):
        for i in range(len(myData)):
            if myData[i].rollno == rollno:
                del myData[i]
                return True
        else:
            return False

    def update(data):
        print('''What you have to update
                     Press 1. Update Name
                     Press 2. Update Roll No.
                     Press 3. Update Mark1
                     Press 4. Update Mark2''')

        choice = int(input("Enter your choice to update the value: "))
        if choice == 1:
            newName = input("Enter the new Name: ")
            data.name = newName
        elif choice == 2:
            newRollNo = int(input("Enter the new Roll No. : "))
            data.rollno = newRollNo
        elif choice == 3:
            newMark1 = int(input("Enter the new Marks 1: "))
            data.mark1 = newMark1
        elif choice == 4:
            newMark2 = int(input("Enter the new Marks 2: "))
            data.mark2 = newMark2
        else:
            print("Enter correct option again.")
            StudentData.update(data)



######################################################################################################################################

a = StudentData("Sujeesh", 1, 31, 45)
b = StudentData("Gaurav", 2, 45, 54)
c = StudentData("Rohit", 3, 56, 65)
myData = [a, b, c]
# print(myData[0])

while True:
    print('''
    \t\tPress 1. Adding new Entry
    \t\tPress 2. Display Student Data
    \t\tPress 3. Searching in Student Data
    \t\tPress 4. Deleting a record
    \t\tPress 5. Updating existing record
    \t\tPress any key to exit''')

    choice = int(input("Enter Your choice: "))
    if choice == 1:
        rollno = int(input("Enter the Roll No. : "))
        if not StudentData.search(rollno, myData)[0]:
            name = input("Enter the Name: ")
            mark1 = int(input("Enter the mark1: "))
            mark2 = int(input("Enter the mark2: "))
            newEntry = StudentData(name, rollno, mark1, mark2)
            myData.append(newEntry)
        else:
            print("Roll No. is Already present.")

    elif choice == 2:
        StudentData.display(myData)

    elif choice == 3:
        rollno = int(input("Enter the Roll No. to be searched: "))
        x = StudentData.search(rollno, myData)
        if x[0]:
            data = x[1]
            print("Roll No. ", rollno, " is Found in Student data.")
            print("Name: ", data.name, "\nMark 1: ", data.mark1, "\nMark 2: ", data.mark2)
        else:
            print("Entered Roll No. is not present in the Record.")

    elif choice == 4:
        rollno = int(input("Enter the Roll No. to be delete: "))
        if StudentData.delete(rollno, myData):
            print("Roll No. ", rollno, "has been deleted Successfully.")
        else:
            print("Entered Roll No. is not Present in the Record.")

    elif choice == 5:
        rollno = int(input("Enter the Roll No. to update: "))
        x = StudentData.search(rollno, myData)
        if x[0]:
            data = x[1]
            StudentData.update(data)
        else:
            print("Entered Roll No. is not present in the Record.")

    else:
        break
