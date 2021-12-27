test = {
  'name': 'regex_quantifiers',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          lark> r"[a-z]{,7}[0-9]{2,4}[a-z]{2,}"
          rstring
            num_quant
              class
                range
                  a
                  z
              7
            num_quant
              class
                range
                  0
                  9
              2
              4
            num_quant
              class
                range
                  a
                  z
              2
          lark> r"([a-z]|[A-Z])+[0-9]*"
          rstring
            plus_quant
              group
                pipe
                  class
                    range
                      a
                      z
                  class
                    range
                      A
                      Z
            star_quant
              class
                range
                  0
                  9
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
