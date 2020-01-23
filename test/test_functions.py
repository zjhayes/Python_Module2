import unittest
from main import camper_age_input


class MyTestCase(unittest.TestCase):

    def test_convert_to_months(self):
        self.assertEquals(camper_age_input.convert_to_months(2.5), 28)


if __name__ == '__main__':
    unittest.main()
