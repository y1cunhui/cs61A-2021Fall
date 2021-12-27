test = {
  'name': 'ebnf-grammar',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'Each of the operands can itself be a Calculator expression.',
          'choices': [
            'The subtraction operator requires at least one argument.',
            'The division operator requires at least two arguments.',
            'Each of the operands can itself be a Calculator expression.',
            'Variables can be defined and used as operands.'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'Which aspects of the Calculator language are supported by this grammar?'
        },
        {
          'answer': '(1 + 2)',
          'choices': [
            '(+ 1 2)',
            '(+)',
            '(+ 1 2 3)',
            '(+ 1)',
            '(1 + 2)',
            '(+ 1 (+ 2 3))'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'Which of the following expressions would NOT be parsable according to that BNF?'
        },
        {
          'answer': 'OPERATOR: "+" | "-" | "*" | "/"',
          'choices': [
            'start: calc_expr',
            '?calc_expr: NUMBER | calc_op',
            'calc_op: "(" OPERATOR calc_expr* ")"',
            'OPERATOR: "+" | "-" | "*" | "/"'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'Which line of the BNF should we modify to add support for calculations using a modulus operator, like (% 15 5)?'
        },
        {
          'answer': 'No, this grammar gives enough information for parsing a Calculator expression, but it does not provide enough information to evaluate it.',
          'choices': [
            'Yes, if we feed this grammar into a program that understands BNF grammars, it will be able to parse Calculator expressions and output the result.',
            'Yes, but only if we feed this grammar into a program that was written in the Calculator language itself.',
            'No, this grammar gives enough information for parsing a Calculator expression, but it does not provide enough information to evaluate it.',
            'No, this grammar does not provide enough information for the parsing or evaluation step, it is useful mostly as documentation.'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'Does the BNF grammar provide enough information to create a working interpreter for this version of the Calculator language?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
