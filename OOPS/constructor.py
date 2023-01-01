class Emp:
    count=0
    def __init__(self,name,stream):
        Emp.count+=1
        self.name=name
        self.stream=stream
        self.display()
        #print("Init method")
        return None
    def display(self):
        print(f'{self.name},{self.stream}')
        return
emp1=Emp("chandan","devops")
emp2=Emp("sakshi","devops")
print(Emp.count)