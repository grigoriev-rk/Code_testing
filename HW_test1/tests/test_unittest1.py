import unittest
#from HW_test import get_name_by_number, show_documents, get_directory_by_number, add_document, remove_document, main, documents, directories
import HW_test


FIXTURES = [
    ("2207 876234", "Василий Гупкин"),
    ("11-2", "Геннадий Покемонов"),
    ("10006", "Аристарх Павлов")  
    ]


FIXTURES_3 = [
    ('8-800-555-3535', 'Leo Doveberg', 'invoice','3', 'Запись добавлена на существующую полку')
    ('8-800-555-3535', 'Leo Doveberg', 'invoice','4', 'Запись добавлена на новую полку')
    ]


FIXTURES_4 = [
    ('8-800-555-3535', 'Документ удален из базы данных и убран с полки')
    ]



class TestFunctions(unittest.TestCase):

    def SetUp(self) -> None:
        print("Метод срабатывает перед каждым текстом ==> setUp")

    @parametrized.expand(FIXTURES)
    def test_get_name_by_number(self, number, exp_result):
        result = get_name_by_number(number)
        self.assertEqual(exp_result, result)

    @parametrized.expand(FIXTURES_3)
    def add_document(self):
        result = add_document(self, number, name, doc_type, directory_number, exp_result)
        self.assertEqual(exp_result, result)


    @parametrized.expand(FIXTURES_4)
    def remove_document(self):
        result = remove_document(self, number, exp_result)
        self.assertEqual(exp_result, result)