==============
flake8-bugbear
==============

.. image:: https://travis-ci.org/PyCQA/flake8-bugbear.svg?branch=master
    :target: https://travis-ci.org/PyCQA/flake8-bugbear

A plugin for Flake8 finding likely bugs and design problems in your
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
``except BaseException:``.  Disable E722 to avoid duplicate warnings.

**B002**: Python does not support the unary prefix increment. Writing
``++n`` is equivalent to ``+(+(n))``, which equals ``n``. You meant ``n
+= 1``.

**B003**: Assigning to ``os.environ`` doesn't clear the
environment.  Subprocesses are going to see outdated
variables, in disagreement with the current process.  Use
``os.environ.clear()`` or the ``env=``  argument to Popen.

**B004**: Using ``hasattr(x, '__call__')`` to test if ``x`` is callable
is unreliable.  If ``x`` implements custom ``__getattr__`` or its
``__call__`` is itself not callable, you might get misleading
results.  Use ``callable(x)`` for consistent results.

**B005**: Using ``.strip()`` with multi-character strings is misleading
the reader. It looks like stripping a substring. Move your
character set to a constant if this is deliberate. Use
``.replace()`` or regular expressions to remove string fragments.

**B006**: Do not use mutable data structures for argument defaults.  All
calls reuse one instance of that data structure, persisting changes
between them.

**B007**: Loop control variable not used within the loop body.  If this is
intended, start the name with an underscore.


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

The following warnings are disabled by default because they are
controversial.  They may or may not apply to you, enable them explicitly
in your configuration if you find them useful.  Read below on how to
enable.

**B901**: Using ``return x`` in a generator function used to be
syntactically invalid in Python 2. In Python 3 ``return x`` can be used
in a generator as a return value in conjunction with ``yield from``.
Users coming from Python 2 may expect the old behavior which might lead
to bugs.  Use native ``async def`` coroutines or mark intentional
``return x`` usage with ``# noqa`` on the same line.

**B902**: Invalid first argument used for method. Use ``self`` for
instance methods, and `cls` for class methods (which includes `__new__`
and `__init_subclass__`) or instance methods of metaclasses (detected as
classes directly inheriting from ``type``).

**B903**: Use ``collections.namedtuple`` (or ``typing.NamedTuple``) for
data classes that only set attributes in an ``__init__`` method, and do
nothing else. If the attributes should be mutable, define the attributes
in ``__slots__`` to save per-instance memory and to prevent accidentally
creating additional attributes on instances.

**B950**: Line too long. This is a pragmatic equivalent of
``pycodestyle``'s E501: it considers "max-line-length" but only triggers
when the value has been exceeded by **more than 10%**. You will no
longer be forced to reformat code due to the closing parenthesis being
one character too far to satisfy the linter. At the same time, if you do
significantly violate the line length, you will receive a message that
states what the actual limit is. This is inspired by Raymond Hettinger's
`"Beyond PEP 8" talk <https://www.youtube.com/watch?v=wf-BqAjZb8M>`_ and
highway patrol not stopping you if you drive < 5mph too fast. Disable
E501 to avoid duplicate warnings.


How to enable opinionated warnings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable these checks, specify a ``--select`` command-line option or
``select=`` option in your config file.  As of Flake8 3.0, this option
is a whitelist (checks not listed are being implicitly disabled), so you
have to explicitly specify all checks you want enabled. For example::

	[flake8]
	max-line-length = 80
	max-complexity = 12
	...
	select = C,E,F,W,B,B901

Note that we're enabling the complexity checks, the PEP8 ``pycodestyle``
errors and warnings, the pyflakes fatals and all default Bugbear checks.
Finally, we're also specifying B901 as a check that we want enabled.

If you'd like all optional warnings to be enabled for you (future proof
your config!), say ``B9`` instead of ``B901``. You will need Flake8 3.2+
for this feature.

Note that ``pycodestyle`` also has a bunch of warnings that are disabled
by default.  Those get enabled as soon as there is an ``ignore =`` line
in your configuration.  I think this behavior is surprising so Bugbear's
opinionated warnings require explicit selection.


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
instead of wasting cycles on Unicode compatibility, etc.


License
-------

MIT


Change Log
----------

17.4.0
~~~~~~

* bugfix: Also check async methods for B006 + B902

17.3.0
~~~~~~

* introduced B903 (patch contributed by Martijn Pieters)

* bugfix: B902 now enforces `cls` for instance methods on metaclasses
  and `metacls` for class methods on metaclasses

17.2.0
~~~~~~

* introduced B902

* bugfix: opinionated warnings no longer invisible in Syntastic

* bugfix: opinionated warnings stay visible when --select on the
  command-line is used with full three-digit error codes

16.12.2
~~~~~~~

* bugfix: opinionated warnings no longer get enabled when user specifies
  ``ignore =`` in the configuration.  Now they require explicit
  selection as documented above also in this case.

16.12.1
~~~~~~~

* bugfix: B007 no longer crashes on tuple unpacking in for-loops

16.12.0
~~~~~~~

* introduced B007

* bugfix: remove an extra colon in error formatting that was making Bugbear
  errors invisible in Syntastic

* marked as "Beta" in trove classifiers, it's been used in production
  for 8+ months

16.11.1
~~~~~~~

* introduced B005

* introduced B006

* introduced B950

16.11.0
~~~~~~~

* bugfix: don't raise false positives in B901 on closures within
  generators

* gracefully fail on Python 2 in setup.py

16.10.0
~~~~~~~

* introduced B004

* introduced B901, thanks Markus!

* update ``flake8`` constraint to at least 3.0.0

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

Glued together by `Łukasz Langa <mailto:lukasz@langa.pl>`_. Multiple
improvements by `Markus Unterwaditzer <mailto:markus@unterwaditzer.net>`_,
`Martijn Pieters <mailto:github.com@zopatista.com>`_, and
`Cooper Lees <mailto:me@cooperlees.com>`_.
