test = {
  'name': 'List Mutation',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # If nothing would be output by Python, type Nothing
          >>> # If the code would error, type Error
          >>> lst = [5, 6, 7, 8]
          >>> lst.append(6)
          Nothing
          >>> lst
          [5, 6, 7, 8, 6]
          >>> lst.insert(0, 9)
          >>> lst
          [9, 5, 6, 7, 8, 6]
          >>> x = lst.pop(2)
          >>> lst
          [9, 5, 7, 8, 6]
          >>> lst.remove(x)
          >>> lst
          [9, 5, 7, 8]
          >>> a, b = lst, lst[:]
          >>> a is lst
          True
          >>> b == lst
          True
          >>> b is lst
          False
          >>> lst = [1, 2, 3]
          >>> lst.extend([4,5])
          >>> lst
          [1, 2, 3, 4, 5]
          >>> lst.extend([lst.append(9), lst.append(10)])
          >>> lst
          [1, 2, 3, 4, 5, 9, 10, None, None]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
