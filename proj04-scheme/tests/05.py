test = {
  'name': 'Problem 5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': 'fd4dd892ccea3adcf9446dc4a9738d47',
          'choices': [
            r"""
            Pair('quote', Pair(A, nil)), where:
                A is the quoted expression
            """,
            r"""
            [A], where:
                A is the quoted expression
            """,
            r"""
            Pair(A, nil), where:
                A is the quoted expression
            """,
            r"""
            A, where:
                A is the quoted expression
            """
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What is the structure of the expressions argument to do_quote_form?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> do_quote_form(Pair(3, nil), global_frame)
          3c7e8a3a2176a696c3a66418f78dff6b
          # locked
          >>> do_quote_form(Pair('hi', nil), global_frame)
          95448591e64e04a7a7885d5fb9b45583
          # locked
          >>> expr = Pair(Pair('+', Pair('x', Pair(2, nil))), nil)
          >>> do_quote_form(expr, global_frame) # Make sure to use Pair notation
          2301ee746b57783004f00f39498fdaed
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      >>> global_frame = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> ''hello
          f675ad62f5f67e5229145843fd6bbcaa
          # locked
          # choice: (quote hello)
          # choice: hello
          # choice: (hello)
          # choice: (quote (quote (hello)))
          scm> (quote (1 2))
          484e4b42665b2864d685ef07fe666107
          # locked
          scm> (car '(1 2 3))
          eb892a26497f936d1f6cae54aacc5f51
          # locked
          scm> (cdr '(1 2))
          750540b47bda75ff036b4a9aa741b087
          # locked
          scm> (cons 'car '('(4 2)))
          2234c2efce8aa029eaab9df8f6431f75
          # locked
          scm> (eval (cons 'car '('(4 2))))
          46beb7deeeb5e9af1c8d785b12558317
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (quote hello)
          hello
          scm> 'hello
          hello
          scm> ''hello
          (quote hello)
          scm> (quote (1 2))
          (1 2)
          scm> '(1 2)
          (1 2)
          scm> (car (car '((1))))
          1
          scm> (quote 3)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
