test = {
  'name': 'tree',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          lark> Tree(12)
          tree_node  12
          lark> Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2)])])
          tree_node
            6
            branches
              tree_node  1
              tree_node
                3
                branches
                  tree_node  1
                  tree_node  2
          lark> Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6, [Tree(7)]), Tree(8)])])
          tree_node
            1
            branches
              tree_node
                2
                branches
                  tree_node  3
                  tree_node  4
              tree_node
                5
                branches
                  tree_node
                    6
                    branches
                      tree_node  7
                  tree_node  8
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      %import lab12 (tree_node, label, branches)
      %ignore /\s+/
      ?start: tree_node
      """,
      'teardown': '',
      'type': 'lark'
    }
  ]
}
