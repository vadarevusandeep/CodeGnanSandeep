#base class
class university:
    def __init__(self,NAME,EDUCATION,COURSES,AGE):
        self.NAME = NAME
        self.COURSES = COURSES
        self.EDUCATION = EDUCATION
        self.AGE = AGE
        print("MAHARAJ VIJAYARAM GAJAPATHI RAJ COLLEGE OF ENGINEERING DETAILS")
class Student(university):   
    def studentdetails(self,sid):
        self.sid = sid
        print(f"Student details:")
        print(f"Name : {self.NAME}\nAge : {self.AGE}\nEducation : {self.EDUCATION}\nCourses : {self.COURSES}")
        print(f"sid : {self.sid}\n")
class Professor(university):
    def professsordetails(self,pid):
        self.pid = pid
        print(f"Professor details:")
        print(f"Name : MR.{self.NAME} sir\nAge : {self.AGE}\nEducation : {self.EDUCATION}\nCourses : {self.COURSES}")
        print(f"pid : {self.pid}")
class Courses(university):
    def coursesdetails(self):
        pass
s = Student("sandeep","BTECH",["python","sql"],22)
s.studentdetails(754)
p = Professor("DEEPAK","MTECH,PHD",["AIML,WEBDEVELOPMENT"],35)
p.professsordetails(25)