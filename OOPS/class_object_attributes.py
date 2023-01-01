class emp:
    count=0 #class attributes
    def emp_details(self,name,stream,yoj):
        self.name=name   # object attributes
        self.stream=stream
        self.yoj=yoj
        self.no_of_employee()
        self.display()
        return None
    def no_of_employee(self):
        emp.count+=1
        return None
    def display(self):
        print(f'Name : {self.name}\t Profile : {self.stream} \t Year of joining : {self.yoj}')
    
def main():
    emp1=emp()
    emp2=emp()
    
    emp1.emp_details("chandan","devops",2020)
    emp2.emp_details("sakshi","devops",2019)

    print("Total Employee : ",emp.count)


if __name__=='__main__':
    main()