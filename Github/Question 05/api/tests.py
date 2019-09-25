import unittest
from validation_str import verification_alphabet
from validation_str import verification_extension
from validation_str import character_text_101
from validation_str import verification_letter
import api
#from ..api import api
#from validator import validator


class TestApi(unittest.TestCase):
    def test_01(self):
        self.assertEqual(verification_alphabet('a'), 'a')

    def test_02(self):
        self.assertEqual(verification_alphabet('ar'), False)

    def test_03(self):
        self.assertEqual(verification_alphabet('1'), False)

    def test_04(self):
        self.assertEqual(verification_extension(character_text_101()), False)

    def test_05(self):
        self.assertEqual(verification_letter('ama'), 'ama')

    def test_06(self):
        self.assertEqual(verification_letter('osso'), 'osso')

    def test_07(self):
        self.assertEqual(verification_letter('mamão'), 'mamao')

    def test_08(self):
        self.assertEqual(verification_letter('Aurélio'), 'aurelio')

    def test_09(self):
        self.assertEqual(verification_letter('Gr1d'), 'Entrada invalida')

    def test_10(self):
        self.assertEqual(0, 0)

    def test_11(self):
        self.assertEqual(0, 0)


# insira o que deseja testar


# gerador de string de 100 caracteres


if __name__ == '__main__':
    unittest.main()
