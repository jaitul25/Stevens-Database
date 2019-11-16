"""" Test for Repository """

import unittest
import os
from HW11_Jaitul_Bharodiya import repository, Student,Instructor, file_reading_gen, Major

class TestRepository(unittest.TestCase):
    """ Test for repository """
    def setUp(self):
        self.test_path = "E:\Python Practice"
        self.repo = repository(self.test_path,False)

    def test_majors(self):
        """ Testing majors table"""
        expected =  [['SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']], ['SYEN', ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]]
        
        calculated = [majors.tab_row() for majors in self.repo._majors.values()]
        self.assertEqual(expected, calculated)

    def test_Student_attributes(self):
        """ Testing student table """
        expected = [['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], {'SSW 540', 'SSW 555'}, None], ['10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 
        'SSW 567', 'SSW 687'], {'SSW 540', 'SSW 555'}, None], ['10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], {'SSW 540', 'SSW 564'}, {'CS 513', 'CS 501', 'CS 545'}], ['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687'], {'SSW 540', 'SSW 555'}, {'CS 513', 'CS 501', 'CS 545'}], ['10183', 'Chapman, O', 'SFEN', ['SSW 689'], {'SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'}, {'CS 513', 'CS 501', 'CS 545'}], ['11399', 'Cordova, I', 'SYEN', ['SSW 540'], {'SYS 671', 'SYS 612', 'SYS 800'}, None], ['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800'], {'SYS 671', 'SYS 612'}, {'SSW 540', 'SSW 565', 'SSW 810'}], ['11658', 'Kelly, P', 'SYEN', [], {'SYS 671', 'SYS 612', 'SYS 800'}, {'SSW 540', 'SSW 565', 'SSW 810'}], ['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645'], {'SYS 671', 'SYS 612', 'SYS 800'}, {'SSW 540', 'SSW 565', 'SSW 810'}], ['11788', 'Fuller, E', 'SYEN', ['SSW 540'], {'SYS 671', 'SYS 612', 'SYS 800'}, None]]

        calculated = [student.tab_row() for cwid, student in self.repo._students.items()]
        self.assertEqual(expected, calculated)

    def test_Instructor_attributes(self):
        """ Testing instructors table """
        expected = {('98765', 'Einstein, A', 'SFEN', 'SSW 567', 4),     
                    ('98765', 'Einstein, A', 'SFEN', 'SSW 540', 3),     
                    ('98764', 'Feynman, R', 'SFEN', 'SSW 564', 3),     
                    ('98764', 'Feynman, R', 'SFEN', 'SSW 687', 3),     
                    ('98764', 'Feynman, R', 'SFEN', 'CS 501', 1),     
                    ('98764', 'Feynman, R', 'SFEN', 'CS 545', 1),     
                    ('98763', 'Newton, I',  'SFEN', 'SSW 555', 1),     
                    ('98763', 'Newton, I', 'SFEN', 'SSW 689', 1 ),    
                    ('98760', 'Darwin, C', 'SYEN', 'SYS 800', 1),     
                    ('98760', 'Darwin, C', 'SYEN', 'SYS 750', 1),     
                    ('98760', 'Darwin, C', 'SYEN', 'SYS 611', 2),     
                    ('98760', 'Darwin, C', 'SYEN', 'SYS 645', 1)}

        calculated = {tuple(detail) for instructor in self.repo._instructors.values() for detail in instructor.tab_row()}
        self.assertEqual(expected, calculated)


if __name__ == "__main__":
    """ Run test cases on startup """
    unittest.main(exit=False, verbosity=2) 