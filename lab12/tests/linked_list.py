test = {
  'name': 'linked_list',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          lark> Link(1)
          link  1
          lark> Link(1, Link(2, Link(3, Link(4))))
          link
            1
            link
              2
              link
                3
                link  4
          lark> Link(5, Link(7, Link(Link(8, Link(9)))))
          link
            5
            link
              7
              link
                link
                  8
                  link  9
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      %import lab12 (link, link_first, link_rest)
      %ignore /\s+/
      ?start: link
      """,
      'teardown': '',
      'type': 'lark'
    }
  ]
}
