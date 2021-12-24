test = {
  'name': 'buffer',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
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
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from buffer import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
