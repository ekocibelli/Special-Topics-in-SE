import unittest
import datetime
from HW08_Ejona_Kocibelli import date_arithmetic, file_reading_gen, FileAnalyzer


class TestContainer(unittest.TestCase):
    def test_date_arithmetic(self):
        """Verify if function date_arithmetic works properly"""
        self.assertEqual(date_arithmetic(),
                         (datetime.datetime(2000, 3, 1, 0, 0), datetime.datetime(2017, 3, 2, 0, 0), 303))

    def test_file_reading_gen(self):
        """Verify that the function reads and yields the information of the file properly"""
        self.path = r"C:\Users\Ejona's Surface\PycharmProjects\ssw810\student_majors.txt"
        expect = [('123', 'Jin He', 'Computer Science'),
                  ('234', 'Nanda Koka', 'Software Engineering'),
                  ('345', 'Benji Cai', 'Software Engineering')]
        result = list(file_reading_gen(r"C:\Users\Ejona's Surface\PycharmProjects\ssw810\student_majors.txt", 3,
                                       sep='|', header=True))

        expect1 = [('123', 'Jin He', 'Computer Science'),
                   ('234', 'Nanda Koka', 'Software Engineering'),
                   ('345', 'Benji Cai', 'Software Engineering')]

        result1 = list(file_reading_gen(r"C:\Users\Ejona's Surface\Desktop\testing\student_majors_noheader.txt", 3,
                                        sep=',', header=False))

        self.assertEqual(result1, expect1)
        self.assertEqual(result, expect)

    def test_analyze_files(self):
        """Verify that analyze_files works properly and adds the right values into the dictionary"""
        expect = {'0_defs_in_this_file.py': {'line': 3, 'char': 57, 'function': 0, 'class': 0}, 'file1.py': {'line': 25
                  , 'char': 270, 'function': 4, 'class': 2}}
        result = FileAnalyzer(r"C:\Users\Ejona's Surface\Desktop\testing").files_summary

        self.assertEqual(expect, result)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
