from pathlib import Path
import unittest

from bugbear import BugBearChecker
from bugbear import B001, B002, B003, B301, B302, B303, B304, B305, B306, B901


class BugbearTestCase(unittest.TestCase):
    maxDiff = None

    def test_b001(self):
        filename = Path(__file__).absolute().parent / 'b001.py'
        bbc = BugBearChecker(filename=str(filename))
        errors = list(bbc.run())
        self.assertEqual(
            errors,
            [B001(8, 0), B001(40, 4)],
        )

    def test_b002(self):
        filename = Path(__file__).absolute().parent / 'b002.py'
        bbc = BugBearChecker(filename=str(filename))
        errors = list(bbc.run())
        self.assertEqual(
            errors,
            [B002(13, 8), B002(17, 12)],
        )

    def test_b003(self):
        filename = Path(__file__).absolute().parent / 'b003.py'
        bbc = BugBearChecker(filename=str(filename))
        errors = list(bbc.run())
        self.assertEqual(
            errors,
            [B003(10, 0)],
        )

    def test_b301_b302_b305(self):
        filename = Path(__file__).absolute().parent / 'b301_b302_b305.py'
        bbc = BugBearChecker(filename=str(filename))
        errors = list(bbc.run())
        self.assertEqual(
            errors,
            [B301(37, 4), B301(38, 4), B301(39, 4), B301(40, 4)] +
            [B302(41, 4), B302(42, 4), B302(43, 4), B302(44, 4)] +
            [B305(45, 4), B305(46, 4)]
        )

    def test_b303_b304(self):
        filename = Path(__file__).absolute().parent / 'b303_b304.py'
        bbc = BugBearChecker(filename=str(filename))
        errors = list(bbc.run())
        self.assertEqual(
            errors,
            [B303(21, 4), B304(38, 4)],
        )

    def test_b306(self):
        filename = Path(__file__).absolute().parent / 'b306.py'
        bbc = BugBearChecker(filename=str(filename))
        errors = list(bbc.run())
        self.assertEqual(
            errors,
            [B306(9, 10)],
        )

    def test_b901(self):
        filename = Path(__file__).absolute().parent / 'b901.py'
        bbc = BugBearChecker(filename=str(filename))
        errors = list(bbc.run())
        self.assertEqual(
            errors,
            [B901(6, 0), B901(34, 0)]
        )


if __name__ == '__main__':
    unittest.main()
