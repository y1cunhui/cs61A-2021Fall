test = {
  'name': 'simple-csv',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          lark> first,second,third
          ....> fourth,fifth,sixth,,eighth
          start
            lines
              line
                word  first
                word  second
                word  third
              newline
              line
                word  fourth
                word  fifth
                word  sixth
                word
                word  eighth
          lark> one,,,,three
          start
            lines
              line
                word  one
                word
                word
                word
                word  three
          lark> ,,,word
          start
            lines
              line
                word
                word
                word
                word  word
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      %import lab14 (lines, line, word, newline)
      start: lines
      """,
      'teardown': '',
      'type': 'lark'
    }
  ]
}
