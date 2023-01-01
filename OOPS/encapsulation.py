#definig same method in deifferent classes

class chandan(object):
    def __init__(self,name,course):
        self.name=name
        self.__course=course
        self.__display()
        return None
    def __display(self):
        print(f'{self.name} \t {self.__course}')


chandan_obj=chandan("chandan","devex")


#chandan_obj.__display()