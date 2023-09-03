import unittest
from laba import registerUser
from validation.loginValidation import check_if_login_is_valid,check_login_type,checkIfRegistered


class TestIfValidLogin(unittest.TestCase):

    def test_login(self):
        #valid inputs
        self.assertEqual(check_if_login_is_valid("login@mail.ru"),("Success",""))
        self.assertEqual(check_if_login_is_valid("+7-999-999-9999"),("Success",""))
        self.assertEqual(check_if_login_is_valid("5simvolov"),("Success",""))
        # invalid inputs
        self.assertEqual(check_if_login_is_valid("edg1337"),("Failure","User with this login already exists"))
        self.assertEqual(check_if_login_is_valid("+7-999-999-999"),("Failure","Phone number is in incorrect format, must be (+x-xxx-xxx-xxxx)"))
        self.assertEqual(check_if_login_is_valid("edg@mailru"),("Failure", "Email must be in a format of (xxx@xxx.xx)"))
        self.assertEqual(check_if_login_is_valid("aaa"),("Failure", "Login must be at least 5 characters long"))
        self.assertEqual(check_if_login_is_valid("somelogin***"),("Failure", "Login can only contain latin characters, numbers from 0 to 9, and _ symbol"))
        self.assertEqual(check_if_login_is_valid(""),("Failure", "Login can not be empty")) # must be a string index out of range error