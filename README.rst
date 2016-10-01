==============
flake8-bugbear
==============

A plugin for flake8 finding likely bugs and design problems in your
program.  Contains warnings that don't belong in pyflakes and
pycodestyle::

    bug·bear  (bŭg′bâr′)
    n.
    1. A cause of fear, anxiety, or irritation: *Overcrowding is often
       a bugbear for train commuters.*
    2. A difficult or persistent problem: *"One of the major bugbears of
       traditional AI is the difficulty of programming computers to
       recognize that different but similar objects are instances of the
       same type of thing" (Jack Copeland).*
    3. A fearsome imaginary creature, especially one evoked to frighten
       children.


List of warnings
----------------

**B001**: Do not use bare ``except:``, it also catches unexpected events
like memory errors, interrupts, system exit, and so on.  Prefer ``except
Exception:``.  If you're sure what you're doing, be explicit and write
``except BaseException:``.

**B002**: Python does not support the unary prefix increment. Writing
``++n`` is equivalent to ``+(+(n))``, which equals ``n``. You meant ``n
+= 1``.

**B003**: Assigning to ``os.environ`` doesn't clear the
environment.  Subprocesses are going to see outdated
variables, in disagreement with the current process.  Use
``os.environ.clear()`` or the ``env=``  argument to Popen.


Python 3 compatibility warnings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These have higher risk of false positives but discover regressions that
are dangerous to slip through when test coverage is not great. Let me
know if a popular library is triggering any of the following warnings
for valid code.

**B301**: Python 3 does not include ``.iter*`` methods on dictionaries.
The default behavior is to return iterables. Simply remove the ``iter``
prefix from the method.  For Python 2 compatibility, also prefer the
Python 3 equivalent if you expect that the size of the dict to be small
and bounded. The performance regression on Python 2 will be negligible
and the code is going to be the clearest.  Alternatively, use
``six.iter*`` or ``future.utils.iter*``.

**B302**: Python 3 does not include ``.view*`` methods on dictionaries.
The default behavior is to return viewables. Simply remove the ``view``
prefix from the method.  For Python 2 compatibility, also prefer the
Python 3 equivalent if you expect that the size of the dict to be small
and bounded. The performance regression on Python 2 will be negligible
and the code is going to be the clearest.  Alternatively, use
``six.view*`` or ``future.utils.view*``.

**B303**: The ``__metaclass__`` attribute on a class definition does
nothing on Python 3. Use ``class MyClass(BaseClass, metaclass=...)``.
For Python 2 compatibility, use ``six.add_metaclass``.

**B304**: ``sys.maxint`` is not a thing on Python 3. Use
``sys.maxsize``.

**B305**: ``.next()`` is not a thing on Python 3. Use the ``next()``
builtin. For Python 2 compatibility, use ``six.next()``.

**B306**: ``BaseException.message`` has been deprecated as of Python 2.6
and is removed in Python 3. Use ``str(e)`` to access the user-readable
message. Use ``e.args`` to access arguments passed to the exception.


Opinionated warnings
~~~~~~~~~~~~~~~~~~~~

Those warnings are disabled by default because the opinions they come from are
controversial.

**B901**: Using ``return x`` in a generator function is syntactically invalid
in Python 2, but in Python 3 ``return x`` in a generator function means ``raise
StopIteration(x)``. Users that come from Python 2 may be used to Python 2
rejecting code that mixes both, so this can lead to situations where it looks
like ``return x`` makes the function generate an empty sequence. Use the more
explicit ``raise StopIteration(x)`` instead of ``return x``.


Tests
-----

Just run::

    python setup.py test


OMG, this is Python 3 only!
---------------------------

Relax, you can run ``flake8`` with all popular plugins as a *tool*
perfectly fine under Python 3.5+ even if you want to analyze Python 2
code.  This way you'll be able to parse all of the new syntax supported
on Python 3 but also *effectively all* the Python 2 syntax at the same
time.

If you're still invested in Python 2, there might be a small subset of
deprecated syntax that you'd have to abandon... but you're already doing
that, right?  `six <https://pypi.python.org/pypi/six>`_ or
`python-future <https://pypi.python.org/pypi/future>`_ bridge the gaps.

By making the code exclusively Python 3.5+, I'm able to focus on the
quality of the checks and re-use all the nice features of the new
releases (check out `pathlib <docs.python.org/3/library/pathlib.html>`_)
instead of wasting cycles on Unicode compatiblity, etc.


License
-------

MIT


Change Log
----------

16.9.0
~~~~~~

* introduced B003

16.7.1
~~~~~~

* bugfix: don't omit message code in B306's warning

* change dependency on ``pep8`` to dependency on ``pycodestyle``, update
  ``flake8`` constraint to at least 2.6.2

16.7.0
~~~~~~

* introduced B306

16.6.1
~~~~~~

* bugfix: don't crash on files with tuple unpacking in class bodies

16.6.0
~~~~~~

* introduced B002, B301, B302, B303, B304, and B305

16.4.2
~~~~~~

* packaging herp derp

16.4.1
~~~~~~

* bugfix: include tests in the source package (to make ``setup.py test``
  work for everyone)

* bugfix: explicitly open README.rst in UTF-8 in setup.py for systems
  with other default encodings

16.4.0
~~~~~~

* first published version

* date-versioned


Authors
-------

Glued together by `Łukasz Langa <mailto:lukasz@langa.pl>`_.
