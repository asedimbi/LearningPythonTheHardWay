print('hello')

class emp:
    def __init__(self, jDate = None, eid = None):
        self.eid = eid
        self.jDate = jDate
        self.rating = -1
    
    def printEmp(self):
        print(f'EID: {self.eid}, JoinDate: {self.jDate}, Rating: {self.rating}')


class office:
    def __init__(self):
        self.deptRepo = dict()
        self.DeptCounter = 10

    def addDept(self, dept):
        self.deptRepo[self.DeptCounter] = dept
        dept.dID = self.DeptCounter
        self.DeptCounter += 1

    def printOffice(self):
        print('Following are Depts in this Office:')
        for dID in self.deptRepo.keys():
            print(dID)



class dept:
    def __init__(self, empArray = [], man = None):
        self.dID = None
        self.empRepo = dict()
        self.IDcounter = 1000
        for emp in empArray:
            self.addEmp(emp)
        self.man = man

    def addEmp(self, emp):
        emp.eid = self.IDcounter
        self.empRepo[self.IDcounter] = emp
        self.IDcounter += 1

    def getMaxRatedEmp(self):
        maxRating = float('-inf')
        maxEmp = None
        for eID, emp in self.empRepo:
            if emp.rating > maxRating:
                maxEmp = emp
                maxRating = emp.rating
        return maxEmp

    def getEmpStartingAfter(self, startDate):
        res = []
        for eID, emp in self.empRepo:
            if emp.jDate >= startDate:
                res.append(emp)
        return res

    def printDept(self):
        print(f'DeptID: {self.dID}, EMP Count: {self.IDcounter - 1000}, ManagerID: {self.man.eid}')
        print('-------------------------EMP List--------------------------------')
        for emp in self.empRepo.values():
            emp.printEmp()

class manager(emp):
    def __init__(self, jDate= None, eid=None, dept = None):
        super().__init__(jDate, eid)
        self.dept = dept

    def addEmp(self, emp):
        self.dept.addEmp(emp)

    def assignRatings(self):
        for eID in self.dept.empRepo.keys():    
            perf = self.calPerformance(self.dept.empRepo[eID])
            self.dept.empRepo[eID].rating = perf
        
    def calPerformance(self, emp):
        return (emp.eid + 1) % 5

    def getMaxRatedEmp(self):
        return self.dept.getMaxRatedEmp()

if __name__ == "__main__":
    MyOffice = office()
    MyDept = dept()
    MyManager = manager(50005, 1)
    emp1 = emp(50006)
    emp1.printEmp()
    MyManager.dept = MyDept
    MyDept.man = MyManager

    MyManager.addEmp(emp1)
    MyManager.addEmp(emp(50006))
    MyManager.addEmp(emp(50016))
    MyManager.addEmp(emp(50026))
    MyManager.addEmp(emp(50036))
    MyManager.addEmp(emp(50046))
    MyManager.addEmp(emp(50046))
    MyManager.addEmp(emp(50046))
    MyManager.addEmp(emp(50056))
    MyDept.printDept()
    print('*******************')
    print('** After Ratings **')
    print('*******************')
    MyManager.assignRatings()
    MyDept.printDept()
    MyManager.printEmp()


