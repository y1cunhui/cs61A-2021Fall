test = {
  'name': 'bluedog',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM bluedog;
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          sqlite> SELECT * FROM bluedog_songs;
          blue|dog|Clair De Lune
          blue|dog|Shake It Off
          blue|dog|Old Town Road
          blue|dog|Dancing Queen
          blue|dog|Old Town Road
          blue|dog|Clair De Lune
          blue|dog|Dancing Queen
          blue|dog|Clair De Lune
          blue|dog|STAY
          blue|dog|Old Town Road
          blue|dog|Shake It Off
          blue|dog|STAY
          blue|dog|Clair De Lune
          blue|dog|Clair De Lune
          blue|dog|STAY
          blue|dog|Clair De Lune
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab13.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
