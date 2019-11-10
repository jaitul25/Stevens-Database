""" Creating a Repository for University """

import os
from collections import defaultdict
from prettytable import PrettyTable
from HW08_Jaitul_Bharodiya import file_reading_gen

class repository:
    " Student and Instructor repository"
    def __init__(self, direct, tables=True):
        self._direct = direct
        self._students = dict()
        self._instructors = dict()

        try:
            self._get_students(os.path.join(direct, 'students.txt'))
            self._get_instructors(os.path.join(direct, 'instructors.txt'))
            self._get_grades(os.path.join(direct, 'grades.txt'))
        except FileNotFoundError:
            raise FileNotFoundError
        else:
            if tables:
                print(" Student Table ")
                self.student_table()
                print(" Instructor Table ")
                self.instructor_table()

    def _get_students(self, path):
        """ Student detail are read using file reading gen and added to dictionary """ 
        for cwid, name, major in file_reading_gen(path,3,sep=';',header=False):
            self._students[cwid] = Student(cwid, name, major)

    def _get_instructors(self, path):
        """ Instructor detail are read using file reading gen and added to dictionary """ 
        for cwid, name, dept in file_reading_gen(path, 3, sep='|', header=False):
            self._instructors[cwid] = Instructor(cwid, name, dept)

    def _get_grades(self, path):
        """Grades are read using file reading gen and assigned to student and instructor """
        for std_cwid, course, grade, instructor_cwid in file_reading_gen(path, 4, sep='|', header=False):
            if std_cwid in self._students:
                self._students[std_cwid].add_course(course, grade)
            else:
                print(f'Grades for student is {std_cwid}')

            if instructor_cwid in self._instructors:
                self._instructors[instructor_cwid].add_student(course)
            else:
                print(f'Grades for instructor is {instructor_cwid}')

    def student_table(self):
        """ Student table """
        tab = PrettyTable(field_names=Student.tab_header)
        for student in self._students.values():
            tab.add_row(student.tab_row())
        print(tab)

    def instructor_table(self):
        """ Instructor table """
        tab = PrettyTable(field_names = Instructor.tab_header)
        for instructor in self._instructors.values():
            for row in instructor.tab_row():
                tab.add_row(row)
        print(tab)


class Student:
    """ Student class """
    tab_header = ['CWID', 'Name', 'Completed Courses']

    def __init__(self, cwid, name, major):
        self._cwid = cwid
        self._name = name
        self._major = major
        self._courses = dict()

    def add_course(self, course, grade):
        """ Adding course with grade """
        self._courses[course] = grade

    def tab_row(self):
        """ Returning a row in table """ 
        return [self._cwid, self._name, sorted(self._courses.keys())]


class Instructor:
    """ Instructor class """
    tab_header = ['CWID', 'Name', 'Dept', 'Course', 'Students']

    def __init__(self, cwid, name, dept):
        self._cwid = cwid
        self._name = name
        self._dept = dept
        self._courses = defaultdict(int)

    def add_student(self, course):
        """ NUmber of students taking course with Instructor """
        self._courses[course] += 1

    def tab_row(self):
        """ Yield the row """
        for course, count in self._courses.items():
            yield [self._cwid, self._name, self._dept, course, count]


def main():
    direct = 'E:\Python Practice'
    repository(direct)

if __name__ == '__main__':
    main()









