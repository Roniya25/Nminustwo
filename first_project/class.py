class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def display(self):
        print(self.name)
        print(self.year)


std1 = Student('Anu', 2002)
std2 = Student('Manu', 2002)
std3 = Student('Keerthi', 2003)
std4 = Student('Ammu', 2005)
std1.display()


class Division:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.stud_list = []

    def add_stud(self, student):
        self.stud_list.append(student)
        print("New student is added : ", self.stud_list)

    def remove_stud(self, name):
        if name in self.stud_list:
            self.stud_list.remove(name)
            print("The student is removed")
        else:
            print("Every students passed")


div1 = Division('arya', '1234')
div1.add_stud('anusha')
div1.remove_stud('ani')





