import unittest
import finding_political_donors_by_date_and_by_zip

class TestIsZipValid(unittest.TestCase):
    """Test class for function finding_political_donors_by_date_and_by_zip.is_zip_valid"""
    def test_zipcode_with_fewer_than_5_digits(self):
        """Test to see if zipcode with fewer than 5 digits is considered valid"""
        actual = finding_political_donors_by_date_and_by_zip.is_zip_valid('1859')
        expected = False
        self.assertEqual(expected, actual)

    def test_zipcode_with_5_digits(self):
        """Test to see if zipcode with exactly 5 digits is considered valid"""
        actual = finding_political_donors_by_date_and_by_zip.is_zip_valid('14221')
        expected = True
        self.assertEqual(expected, actual)

    def test_zipcode_with_more_than_5_digits(self):
        """Test to see if zipcode more than 5 digits is considered valid"""
        actual = finding_political_donors_by_date_and_by_zip.is_zip_valid('100216')
        expected = True
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
