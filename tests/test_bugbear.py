from pathlib import Path
import subprocess
import unittest

from bugbear import BugBearChecker
from bugbear import (
    B001,
    B002,
    B003,
    B004,
    B005,
    B006,
    B007,
    B008,
    B301,
    B302,
    B303,
    B304,
    B305,
    B306,
    B901,
    B902,
    B903,
    B950,
)


class BugbearTestCase(unittest.TestCase):
    maxDiff = None

    def errors(self, *errors):
        return [BugBearChecker.adapt_error(e) for e in errors]

    def test_b001(self):
        filename = Path(__file__).absolute().parent / "b001.py"
        bbc = BugBearChecker(filename=str(filename))
        errors = list(bbc.run())
        self.assertEqual(errors, self.errors(B001(8, 0), B001(40, 4)))

    def test_b002(self):
        filename = Path(__file__).absolute().parent / "b002.py"
        bbc = BugBearChecker(filename=str(filename))
        errors = list(bbc.run())
        self.assertEqual(errors, self.errors(B002(15, 8), B002(20, 11)))

    def test_b003(self):
        filename = Path(__file__).absolute().parent / "b003.py"
        bbc = BugBearChecker(filename=str(filename))
        errors = list(bbc.run())
        self.assertEqual(errors, self.errors(B003(10, 0)))

    def test_b004(self):
        filename = Path(__file__).absolute().parent / "b004.py"
        bbc = BugBearChecker(filename=str(filename))
        errors = list(bbc.run())
        self.assertEqual(errors, self.errors(B004(3, 7), B004(5, 7)))

    def test_b005(self):
        filename = Path(__file__).absolute().parent / "b005.py"
        bbc = BugBearChecker(filename=str(filename))
        errors = list(bbc.run())
        self.assertEqual(
            errors,
            self.errors(
                B005(4, 0),
                B005(7, 0),
                B005(10, 0),
                B005(13, 0),
                B005(16, 0),
                B005(19, 0),
            ),
        )

    def test_b006_b008(self):
        filename = Path(__file__).absolute().parent / "b006_b008.py"
        bbc = BugBearChecker(filename=str(filename))
        errors = list(bbc.run())
        self.assertEqual(
            errors,
            self.errors(
                B006(10, 24),
                B006(14, 29),
                B006(18, 19),
                B006(22, 19),
                B006(26, 31),
                B008(35, 38),
            ),
        )

    def test_b007(self):
        filename = Path(__file__).absolute().parent / "b007.py"
        bbc = BugBearChecker(filename=str(filename))
        errors = list(bbc.run())
        self.assertEqual(
            errors,
            self.errors(
                B007(6, 4, vars=("i",)),
                B007(18, 12, vars=("k",)),
                B007(30, 4, vars=("i",)),
                B007(30, 12, vars=("k",)),
            ),
        )

    def test_b301_b302_b305(self):
        filename = Path(__file__).absolute().parent / "b301_b302_b305.py"
        bbc = BugBearChecker(filename=str(filename))
        errors = list(bbc.run())
        self.assertEqual(
            errors,
            self.errors(
                B301(39, 4),
                B301(40, 4),
                B301(41, 4),
                B301(42, 4),
                B302(43, 4),
                B302(44, 4),
                B302(45, 4),
                B302(46, 4),
                B305(47, 4),
                B305(48, 4),
            ),
        )

    def test_b303_b304(self):
        filename = Path(__file__).absolute().parent / "b303_b304.py"
        bbc = BugBearChecker(filename=str(filename))
        errors = list(bbc.run())
        self.assertEqual(errors, self.errors(B303(25, 4), B304(42, 4)))

    def test_b306(self):
        filename = Path(__file__).absolute().parent / "b306.py"
        bbc = BugBearChecker(filename=str(filename))
        errors = list(bbc.run())
        self.assertEqual(errors, self.errors(B306(9, 10)))

    def test_b901(self):
        filename = Path(__file__).absolute().parent / "b901.py"
        bbc = BugBearChecker(filename=str(filename))
        errors = list(bbc.run())
        self.assertEqual(errors, self.errors(B901(9, 8), B901(36, 4)))

    def test_b902(self):
        filename = Path(__file__).absolute().parent / "b902.py"
        bbc = BugBearChecker(filename=str(filename))
        errors = list(bbc.run())
        self.assertEqual(
            errors,
            self.errors(
                B902(29, 17, vars=("'i_am_special'", "instance", "self")),
                B902(32, 30, vars=("'cls'", "instance", "self")),
                B902(35, 4, vars=("(none)", "instance", "self")),
                B902(39, 12, vars=("'self'", "class", "cls")),
                B902(42, 22, vars=("*args", "instance", "self")),
                B902(48, 30, vars=("**kwargs", "instance", "self")),
                B902(51, 32, vars=("*, self", "instance", "self")),
                B902(54, 44, vars=("*, self", "instance", "self")),
                B902(68, 17, vars=("'self'", "metaclass instance", "cls")),
                B902(72, 20, vars=("'cls'", "metaclass class", "metacls")),
            ),
        )

    def test_b903(self):
        filename = Path(__file__).absolute().parent / "b903.py"
        bbc = BugBearChecker(filename=str(filename))
        errors = list(bbc.run())
        self.assertEqual(errors, self.errors(B903(32, 0), B903(38, 0)))

    def test_b950(self):
        filename = Path(__file__).absolute().parent / "b950.py"
        bbc = BugBearChecker(filename=str(filename))
        errors = list(bbc.run())
        self.assertEqual(errors, self.errors(B950(6, 92, vars=(92, 79))))

    def test_selfclean_bugbear(self):
        filename = Path(__file__).absolute().parent.parent / "bugbear.py"
        proc = subprocess.run(
            ["flake8", str(filename)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout.decode("utf8"))
        self.assertEqual(proc.stdout, b"")
        # self.assertEqual(proc.stderr, b"")

    def test_selfclean_test_bugbear(self):
        filename = Path(__file__).absolute()
        proc = subprocess.run(
            ["flake8", str(filename)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout.decode("utf8"))
        self.assertEqual(proc.stdout, b"")
        # self.assertEqual(proc.stderr, b'')


if __name__ == "__main__":
    unittest.main()
