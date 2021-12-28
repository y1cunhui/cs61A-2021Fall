test = {
  'name': 'opening',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM opening;
          Sliver
          Pizzahhh
          La Val's
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab14.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
