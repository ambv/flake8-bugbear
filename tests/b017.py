"""
Should emit:
B017 - on lines 10
"""
import unittest


CONSTANT = True


def something_else() -> None:
    for i in (1, 2, 3):
       print(i)


class Foobar(unittest.TestCase):
    def evil_raises(self) -> None:
        with self.assertRaises(Exception):
            raise Exception("Evil I say!")

    def context_manager_raises(self) -> None:
        with self.assertRaises(Exception) as ex:
            raise Exception("Context manager is good")
        self.assertEqual("Context manager is good", str(ex.exception))

    def regex_raises(self) -> None:
        with self.assertRaisesRegex(Exception, "Regex is good"):
            raise Exception("Regex is good")
