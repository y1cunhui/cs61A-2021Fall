"""The buffer module assists in iterating through lines and tokens."""

import math
import sys


class Buffer:
    """A Buffer provides a way of accessing a sequence of tokens across lines.

    Its constructor takes an iterator, called "the source", that returns the
    next line of tokens as a list each time it is queried, or None to indicate
    the end of data.

    The Buffer in effect concatenates the sequences returned from its source
    and then supplies the items from them one at a time through its pop_first()
    method, calling the source for more sequences of items only when needed.

    In addition, Buffer provides a current method to look at the
    next item to be supplied, without sequencing past it.

    The __str__ method prints all tokens read so far, up to the end of the
    current line, and marks the current token with >>.

    >>> buf = Buffer(iter([['(', '+'], [15], [12, ')']]))
    >>> buf.pop_first()
    '('
    >>> buf.pop_first()
    '+'
    >>> buf.current()
    15
    >>> buf.current()   # Calling current twice should not change buf
    15
    >>> buf.pop_first()
    15
    >>> buf.current()
    12
    >>> buf.pop_first()
    12
    >>> buf.pop_first()
    ')'
    >>> buf.pop_first()  # returns None
    """

    def __init__(self, source):
        self.index = 0
        self.source = source
        self.current_line = ()
        self.current()

    def pop_first(self):
        """Remove the next item from self and return it. If self has
        exhausted its source, returns None."""
        # BEGIN PROBLEM 1
        "*** YOUR CODE HERE ***"
        ans = self.current()
        self.index += 1
        return ans
        # END PROBLEM 1

    def current(self):
        """Return the current element, or None if none exists."""
        while not self.more_on_line():
            try:
                # BEGIN PROBLEM 1
                "*** YOUR CODE HERE ***"
                self.current_line = next(self.source)
                self.index = 0
                # END PROBLEM 1
            except StopIteration:
                self.current_line = ()
                return None
        return self.current_line[self.index]

    def more_on_line(self):
        return self.index < len(self.current_line)


# Try to import readline for interactive history
try:
    import readline
except:
    pass


class InputReader:
    """An InputReader is an iterable that prompts the user for input."""

    def __init__(self, prompt):
        self.prompt = prompt

    def __iter__(self):
        while True:
            yield input(self.prompt)
            self.prompt = ' ' * len(self.prompt)


class LineReader:
    """A LineReader is an iterable that prints lines after a prompt."""

    def __init__(self, lines, prompt, comment=";"):
        self.lines = lines
        self.prompt = prompt
        self.comment = comment

    def __iter__(self):
        while self.lines:
            line = self.lines.pop(0).strip('\n')
            if (self.prompt is not None and line != "" and
                not line.lstrip().startswith(self.comment)):
                print(self.prompt + line)
                self.prompt = ' ' * len(self.prompt)
            yield line
        raise EOFError
