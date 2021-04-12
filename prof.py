from tkinter import *
import tkinter as tk
from tkinter import ttk


class ExamAppllication(tk.Tk):
    """Application root window"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Exam Grade Application")
        self.resizable(width=False, height=False)
        
        
        
        self.recordfrom = DataRecordForm(self)
        self.recordfrom.grid(row=1, padx=10)
        self.savebutton = ttk.Button(self, text="save", command=self.on_save)
        self.savebutton.grid(sticky=tk.E, row=2, padx=10)
        #status bar
        self.status = tk.StringVar()
        self.statusbar = ttk.Label(self, textvariable=self.status)
        self.statusbar.grid(sticky=(tk.W + tk.E), row=3, padx=10)

        ttk.Label(
            self,
            text="Exam Grade  Application", font=("TkDfaultFont", 16).grid(row=0))

       
if __name__ == "__main__":
    app = ExamAppllication()
    app.mainloop()

class StudentDetails:
    def __init__(self,Surname,otherName,studentNo,RegNo,intake,campus,program,school_faculty,Residency
    ,studyTime,Hall,gender,age):
        self.Surname = Surname
        self.otherName = otherName
        self.studentNo = studentNo
        self.RegNo = RegNo
        self.intake = intake
        self.campus = campus
        self.program = program
        self.school_faculty =school_faculty
        self.Residency = Residency
        self.studyTime = studyTime
        self.Hall = Hall
        self.gender = gender
        self.age = age

    def StudentInfor(self):
        self.gender = input("Gender: ")
        self.age = input("Age: ")

    def StudentNames(self):
        self.Surname = input("Surname: ")    
        self.otherName = input("Other Names: ")
        return self.Surname + " " + self.otherName
        

    def StudentIndexNo(self):
        self.studentNo = input("Student Number: ")    
        self.RegNo = input("Reg/Index No: ")
        self.intake = input("Year of Intake: ")
        self.studyTime = input("Study Time: ")


    def StudentAdmin(self):
        self.campus = input("Campus: ")
        self.program = input("Program: ")
        self.school_faculty = input("School/ Faculty: ")
        self.Residency = input("Residency: ")
        self.Hall = input("Hall: ")

    def PrintInfor_Log(self):
        print('\n'"GENERAL STUDENTS INFORMATION"'\n')
        print('\n'"Student Name:",self.Surname + " "+ self.otherName,'\n',"Student No: ",self.studentNo,
        '\n',"Reg /Index No: ",self.RegNo,'\n',"Year of Intake: ",self.intake,'\n',"Campus: ",self.campus,'\n',"Program: ",self.program,
        '\n',"School /Faculty: ",self.school_faculty,'\n',"Residency: ",self.Residency
    ,'\n',"Study Time: ",self.studyTime,'\n',"Hall: ",self.Hall,'\n',"Gender: ",self.gender,'\n',"Age: ",self.age,'\n')    


students = StudentDetails("","","","","","","","","","","","","",) 
# students.StudentNames()
# students.StudentInfor()
# students.StudentIndexNo()
# students.StudentAdmin() 
# students.PrintInfor_Log()    

class StudentGrading(StudentDetails):
    def __init__(self,Surname,otherName,studentNo,RegNo,intake,campus,program,school_faculty,Residency,studyTime,Hall,gender,age,scalePoint):
        super().__init__(self,Surname,otherName,studentNo,RegNo,intake,campus,program,school_faculty,Residency,studyTime,Hall,age)

        self.scalePoint = scalePoint
        self.results = None

    def creditStanding(self):
        print ("That is your class standing from numbers of credit earned")
        # input for the studentname and  credit points earned  
        print("Input your Points")
        self.scalePoint = int(input("Credit points: "))
        if self.scalePoint >= 75:
            print(students.StudentNames(), "Excellent") 
        elif self.scalePoint >= 65 and 75:
            print(students.StudentNames(), "Credit")
        elif self.scalePoint >= 50 and 60:
            print(students.StudentNames(),"Passed")
        elif self.scalePoint <=50:
            print(students.StudentNames(),"Failed")
        else:
            print("RETAKE") 
        self.results = []  
        if self.scalePoint == self.scalePoint:  ###if results in scalepoint:
            self.results.append(self.scalePoint) ##reuslts.app

    def ViewResults(self):
        print("Results in Data Analysis:",self.results)

        ##conditional closes
gradingsys = StudentGrading("","","","","","","","","","","","","","")    
gradingsys.creditStanding()
gradingsys.ViewResults()
# class StudentsResults(StudentDetails,StudentGrading):
#     def __init__(self,Surname,otherName,studentNo,RegNo,intake,campus,program,school_faculty,Residency,studyTime,Hall,gender,age,scalePoint):
#         super().__init__(self,Surname,otherName,studentNo,RegNo,scalePoint)
#         self.results = results

 

        

