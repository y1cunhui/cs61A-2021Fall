test = {
  'name': 'double',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM double;
          breakfast|dinner|La Val's
          breakfast|dinner|Sliver
          breakfast|snack|La Val's
          lunch|snack|La Val's
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
