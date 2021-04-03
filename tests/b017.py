"""
Should emit:
B017 - on lines 15, 20, 25

All tests are valid unittest syntax, and will work if this code
is executed.
"""
import asyncio
import unittest


class AssertRaisesThatShouldTrigger(unittest.TestCase):
    def test_bare_Exception(self) -> None:
        """The use of Exception like this will catch everything"""
        with self.assertRaises(Exception):
            print(k["evil"])  # NameError

    def test_tuple_with_Exception(self) -> None:
        """The use of Exception in the tuple will still catch everything"""
        with self.assertRaises((Exception, ValueError)):
            print("I can't spell print", indent=1)  # TypeError

    def test_tuple_with_module_and_Exception(self) -> None:
        """The use of Exception in the tuple will still catch everything"""
        with self.assertRaises((Exception, asyncio.CancelledError)):
            self.bogus  # AttributeError


class AssertRaisesThatShouldNotTrigger(unittest.TestCase):
    def test_context_manager_raises(self) -> None:
        """A context manager being present means someone has probably
        done a test afterwards; a python linter should have caught the
        lack of use of 'ex' otherwise"""
        with self.assertRaises(Exception) as ex:
            raise ValueError("Context manager is good")
        self.assertEqual("Context manager is good", str(ex.exception))

    def test_raisesregex(self) -> None:
        with self.assertRaisesRegex(Exception, "Regex is good"):
            raise ValueError("Regex is good")

    def test_raises_with_absolute_reference(self):
        with self.assertRaises(asyncio.CancelledError):
            raise asyncio.CancelledError()


# None of these should trigger the With visitor.

CONSTANT = True


def something_else() -> None:
    for i in (1, 2, 3):
        print(i)


class Foo:
    def __enter__(self, *args, **kwargs) -> None:
        yield

    def __exit__(self, *args, **kwargs) -> None:
        ...


# This may trigger the visitor, but it shouldn't match the filters
with Foo() as a:
    print(a)

if __name__ == "__main__":
    unittest.main()
