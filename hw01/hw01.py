from operator import add, sub


def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = add
    else:
        f = sub
    return f(a, b)


def a_plus_abs_b_syntax_check():
    """Check that you didn't change the return statement of a_plus_abs_b.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    # You don't need to edit this function. It's just here to check your work.


def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    return x*x+y*y+z*z-max(x,y,z)*max(x,y,z)


def two_of_three_syntax_check():
    """Check that your two_of_three code consists of nothing but a return statement.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    # You don't need to edit this function. It's just here to check your work.


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    


def limited(x, z, limit):
    """Logic that is common to invert and change."""
    if x != 0:
        return min(z, limit)
    else:
        return limit


def invert_short(x, limit):
    """Return 1/x, but with a limit.

    >>> x = 0.2
    >>> 1/x
    5.0
    >>> invert_short(x, 100)
    5.0
    >>> invert_short(x, 2)    # 2 is smaller than 5
    2

    >>> x = 0
    >>> invert_short(x, 100)  # No error, even though 1/x divides by 0!
    100
    """
    return limited(x, 1 / x, limit)


def change_short(x, y, limit):
    """Return abs(y - x) as a fraction of x, but with a limit.

    >>> x, y = 2, 5
    >>> abs(y - x) / x
    1.5
    >>> change_short(x, y, 100)
    1.5
    >>> change_short(x, y, 1)    # 1 is smaller than 1.5
    1

    >>> x = 0
    >>> change_short(x, y, 100)  # No error, even though abs(y - x) / x divides by 0!
    100
    """
    return limited(x, abs(y - x) / x, limit)


def invert_and_change_syntax_check():
    """Checks that definitions of invert_short and change_short are just return statements.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(invert_short)).body[0].body]
    ['Expr', 'Return']
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(change_short)).body[0].body]
    ['Expr', 'Return']
    """
    # You don't need to edit this function. It's just here to check your work.


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"


"*** YOUR CODE HERE ***"
quine = ''


def quine_test():
    """
    >>> quine_test()
    QUINE!
    """
    import contextlib, io

    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        exec(quine)
    quine_output = f.getvalue()
    if quine == quine_output:
        print("QUINE!")
        return
    print("Not a quine :(")
    print("Code was:   %r" % quine)
    print("Output was: %r" % quine_output)
    print("Side by side:")
    print(quine)
    print("*" * 100)
    print(quine_output)
    print("*" * 100)
