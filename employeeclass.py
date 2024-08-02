import datetime
today = datetime.date.today()
year = today.year
#print(year)

class Company:
    def __init__(self,cname):
        self._cname=cname
    def displayCname(self):
        print("Company Name: ",self._cname)
    def address(self):
        return "Technopark Phase 2 Trivendrum"

# c1 = Company("UST")
# c2 = Company("BMW")
# c1.displayCname()
# c2.displayCname()

class Employee(Company):
    isMarried = True    
    empcount = 0
    def __init__(self,cname,fname,lname,designation,yob):
        self._cname = cname
        self._fname = fname
        self._lname = lname
        self._designation = designation
        self._age = year-yob
        Employee.empcount+=1
    def getEmpDetails(self):
        self.displayCname()
        print("fullname: ",self._fname , " ", self._lname)
        print("Age: ",self._age)
        print("Designation: ",self._designation)
        print("Marital Status: ",self.isMarried)
        print("Employee count: ",self.empcount)
    def address(self):
        print("Company Address: " super().address())
        print("Employee Address: Ginger Hotel Technopark phase1")
        
e1 = Employee("Hematite", "Parag", "Joshi", "Program Head", 1984)
e1.isMarried = False    
#e1.empcount=8;
e1.getEmpDetails()
e1.address()

e2 = Employee("Hematite", "Prachi", "Joshi", "HR Head", 1987)
e2.getEmpDetails()
e3 = Employee("Hematite", "Sarang", "Deshpande", "Finance Head", 2000)
e3.getEmpDetails()
e4 = Employee("Hematite", "Daesha", "Kulkarni", "Ops Head", 2001)
e4.getEmpDetails()
e5 = Employee("Hematite", "Prakash", "Kulkarni", "Ops Head", 2001)
e5.getEmpDetails()


#print(Employee.empcount)


