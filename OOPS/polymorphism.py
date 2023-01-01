#definig same method in deifferent classes

class chandan(object):
    def __init__(self,name,course):
        self.name=name
        self.course=course
        return None
    def display(self):
        print(f'{self.name} \t {self.course}')


class sakshi(object):
    def __init__(self,name,course):
        self.name=name
        self.course=course
        return None
    def display(self):
        print(f'{self.name} \t {self.course}')


chandan_obj=chandan("chandan","devex")
sakshi_obj=sakshi("sakhsi","jrdevops")

sakshi_obj.display()
chandan_obj.display()