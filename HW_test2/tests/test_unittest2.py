import HW_test2
import unittest

EXPECTED = ('ok')

class TestFunctions(unittest.TestCase):

    def SetUp(self) -> None:
        print("Метод срабатывает перед каждым текстом ==> setUp")

    @parametrized.expand(EXPECTED)
    def create_folder(self, exp_result):
        result = create_folder(exp_result)
        self.assertEqual(exp_result, result)
            