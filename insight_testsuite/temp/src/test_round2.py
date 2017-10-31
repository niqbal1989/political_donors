import unittest
import finding_political_donors_by_date_and_by_zip

class TestRound2(unittest.TestCase):
    """Test class for function finding_political_donors_by_date_by_zip.round2"""
    def test_round2_down(self):
        """Test that numbers that are less than <0.5 round to the nearest integer"""
        actual = finding_political_donors_by_date_and_by_zip.round2(2.4)
        expected = 2
        self.assertEqual(expected, actual)

    def test_round2_boundary(self):
        """Test that numbers with decimal at boundary of 0.5 will round up to nearest integer"""
        actual = finding_political_donors_by_date_and_by_zip.round2(10.5)
        expected = 11
        self.assertEqual(expected, actual)

    def test_round2_up(self):
        """Test that numbers with decimal above boundary of 0.5 will round up to the nearest integer"""
        actual = finding_political_donors_by_date_and_by_zip.round2(3.6)
        expected = 4
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
