import unittest
from student import Student
from datetime import timedelta

class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student("Test", "Student")

        self.assertEqual(student.full_name, 'Test Student')

    def test_alert_santa(self):
        student = Student("Test", "Santa")
        student.alert_santa()

        self.assertTrue(student.naughty_list)
    
    def test_email(self):
        student = Student("test", "email")
        
        self.assertEqual(student.email, 'testemail@email.com')
    
    def test_apply_extension(self):
        student = Student("test", "extension")
        old_date = student.end_date
        student.apply_extension(5)

        self.assertEqual(student.end_date, old_date + timedelta(days=5))


if __name__ == "__main__":
    unittest.main()
