#definig same method in deifferent classes

class chandan(object):
    def __init__(self,name,course):
        self.name=name
        self.course=course
        return None
    def display(self):
        print(f'{self.name} \t {self.course}')


class sakshi(chandan): #inherit chandan class
    def __init__(self,name,course):
        self.name=name
        self.course=course
        return None


chandan_obj=chandan("chandan","devex")
sakshi_obj=sakshi("sakhsi","jrdevops")

sakshi_obj.display()
chandan_obj.display()