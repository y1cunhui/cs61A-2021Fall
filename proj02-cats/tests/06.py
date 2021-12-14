test = {
  'name': 'Problem 6',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> big_limit = 10
          >>> feline_flips("car", "cad", big_limit)
          1
          >>> feline_flips("this", "that", big_limit)
          2
          >>> feline_flips("one", "two", big_limit)
          3
          >>> feline_flips("from", "form", big_limit)
          2
          >>> feline_flips("awe", "awesome", big_limit)
          4
          >>> feline_flips("someawe", "awesome", big_limit)
          6
          >>> feline_flips("awful", "awesome", big_limit)
          5
          >>> feline_flips("awful", "awesome", 3) > 3
          True
          >>> feline_flips("awful", "awesome", 4) > 4
          True
          >>> feline_flips("awful", "awesome", 5) > 5
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> big_limit = 10
          >>> feline_flips("nice", "rice", big_limit)    # Substitute: n -> r
          1
          >>> feline_flips("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
          2
          >>> feline_flips("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
          3
          >>> feline_flips("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
          5
          >>> feline_flips("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> big_limit = 10
          >>> feline_flips("goodbye", "good", big_limit)
          3
          >>> feline_flips("pront", "print", big_limit)
          1
          >>> feline_flips("misspollid", "misspelled", big_limit)
          2
          >>> feline_flips("worry", "word", big_limit)
          2
          >>> feline_flips("first", "flashy", big_limit)
          4
          >>> feline_flips("hash", "ash", big_limit)
          4
          >>> feline_flips("ash", "hash", big_limit)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> small_words_list = ["spell", "nest", "test", "pest", "best", "bird", "wired",
          ...                     "abstraction", "abstract", "peeling", "gestate", "west",
          ...                     "spelling", "bastion"]
          >>> autocorrect("speling", small_words_list, feline_flips, 10)
          'peeling'
          >>> autocorrect("abstrction", small_words_list, feline_flips, 10)
          'abstract'
          >>> autocorrect("wird", small_words_list, feline_flips, 10)
          'bird'
          >>> autocorrect("gest", small_words_list, feline_flips, 10)
          'nest'
          >>> # ban iteration, list comprehensions
          >>> test.check('cats.py', 'feline_flips', ['While', 'For', 'ListComp'])
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Check that the recursion stops when the limit is reached
          >>> import trace, io
          >>> from contextlib import redirect_stdout
          >>> with io.StringIO() as buf, redirect_stdout(buf):
          ...     trace.Trace(trace=True).runfunc(feline_flips, "someaweqwertyuio", "awesomeasdfghjkl", 3)
          ...     output = buf.getvalue()
          >>> len([line for line in output.split('\n') if 'funcname' in line]) < 10
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('eyed', 'ey', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('place', 'york', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('prep', 'ounce', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('coed', 'coed', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('goofy', 'oxyl', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('silly', 'silly', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('grain', 'graiq', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('winna', 'wonnai', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('baku', 'baku', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('mark', 'laker', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('ethos', 'erhoi', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('lend', 'erne', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('skid', 'skd', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('study', 'study', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('scold', 'scql', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('flamy', 'flam', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('dotal', 'dota', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('mince', 'mincew', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('ada', 'adasi', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('minar', 'chain', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('tough', 'tojwh', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('teet', 'home', k) > k for k in range(4)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('mumps', 'tuts', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('heart', 'heart', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('qoph', 'death', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('dheri', 'eh', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('keeve', 'keev', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('boort', 'stulm', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('jodel', 'jodelu', k) > k for k in range(6)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('dabba', 'fan', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('cloak', 'wind', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('sung', 'gukgg', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('mon', 'moy', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('lover', 'lover', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('omer', 'omev', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('cibol', 'iib', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('menu', 'exeat', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('blvd', 'km', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('sensa', 'sine', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('enrol', 'lungy', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('octet', 'sct', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('manga', 'guama', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('trike', 'trikgw', k) > k for k in range(6)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('skete', 'skete', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('site', 'dity', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('demob', 'ratwa', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('tinea', 'wreat', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('break', 'libs', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('tubae', 'huqqe', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('run', 'tsuba', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('shy', 'shy', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('terma', 'tfrma', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('krama', 'kramakd', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('jesse', 'messe', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('essay', 'hssa', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('begun', 'begun', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('vii', 'vii', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('rides', 'rides', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('alga', 'alga', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('asker', 'ts', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('rocky', 'rockyp', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('crain', 'cr', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('kinch', 'kinch', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('bort', 'bort', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('deter', 'gale', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('gaize', 'gaize', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('heme', 'hemvn', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('boats', 'boatsz', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('mown', 'yomn', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('anana', 'agan', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('peasy', 'aeasv', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('pie', 'tizzy', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('quin', 'quinffp', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('among', 'sculp', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('ja', 'j', k) > k for k in range(2)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('aube', 'aube', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('mf', 'kf', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('ta', 'jowl', k) > k for k in range(4)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('downy', 'downy', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('brook', 'sxook', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('brood', 'broodd', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('unset', 'rocky', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('pole', 'po', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('dir', 'dir', k) > k for k in range(3)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('rider', 'rider', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('urate', 'uraxb', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('swift', 'gade', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('gucki', 'gacki', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('dang', 'dangb', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('cruth', 'cruthibh', k) > k for k in range(8)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('aloof', 'alfofk', k) > k for k in range(6)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('alive', 'aoiv', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('arow', 'arowlp', k) > k for k in range(6)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('lemon', 'sahib', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('moire', 'dean', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('feaze', 'feazefeb', k) > k for k in range(8)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('socii', 'soci', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('mashy', 'mash', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_flips('a', 'a', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_flips('salol', 'salol', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import feline_flips, autocorrect
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
