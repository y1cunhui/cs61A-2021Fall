test = {
  'name': 'regex_classes',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          lark> r"cs61[abc]"
          rstring
            word  cs
            character  61
            class
              character  a
              character  b
              character  c
          lark> r"cs61[a-c]"
          rstring
            word  cs
            character  61
            class
              range
                a
                c
          lark> r"[a-cdef-xyz]"
          rstring
            class
              range
                a
                c
              character  d
              character  e
              range
                f
                x
              character  y
              character  z
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      %import hw10 (rstring, word, group, pipe, class, character, range, num_quant, plus_quant, star_quant)
      %ignore /\s+/
      ?start: rstring
      """,
      'teardown': '',
      'type': 'lark'
    }
  ]
}
