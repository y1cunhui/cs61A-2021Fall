test = {
  'name': 'Problem 7',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> big_limit = 10
          >>> minimum_mewtations("wird", "wiry", big_limit)
          1
          >>> minimum_mewtations("wird", "bird", big_limit)
          1
          >>> minimum_mewtations("wird", "wir", big_limit)
          1
          >>> minimum_mewtations("wird", "bwird", big_limit)
          1
          >>> minimum_mewtations("speling", "spelling", big_limit)
          1
          >>> minimum_mewtations("used", "use", big_limit)
          1
          >>> minimum_mewtations("hash", "ash", big_limit)
          1
          >>> minimum_mewtations("ash", "hash", big_limit)
          1
          >>> minimum_mewtations("roses", "arose", big_limit)     # roses -> aroses -> arose
          2
          >>> minimum_mewtations("tesng", "testing", big_limit)   # tesng -> testng -> testing
          2
          >>> minimum_mewtations("rlogcul", "logical", big_limit) # rlogcul -> logcul -> logicul -> logical
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> big_limit = 10
          >>> minimum_mewtations("cats", "scat", big_limit)
          2
          >>> minimum_mewtations("purng", "purring", big_limit)
          2
          >>> minimum_mewtations("ckiteus", "kittens", big_limit)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> small_words_list = ["spell", "nest", "test", "pest", "best", "bird", "wired",
          ...                     "abstraction", "abstract", "wire", "peeling", "gestate",
          ...                     "west", "spelling", "bastion"]
          >>> autocorrect("speling", small_words_list, minimum_mewtations, 10)
          'spelling'
          >>> autocorrect("abstrction", small_words_list, minimum_mewtations, 10)
          'abstraction'
          >>> autocorrect("wird", small_words_list, minimum_mewtations, 10)
          'bird'
          >>> autocorrect("gest", small_words_list, minimum_mewtations, 10)
          'nest'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # ***Check that the recursion stops when the limit is reached***
          >>> import trace, io
          >>> from contextlib import redirect_stdout
          >>> with io.StringIO() as buf, redirect_stdout(buf):
          ...     trace.Trace(trace=True).runfunc(minimum_mewtations, "someawe", "awesome", 3)
          ...     output = buf.getvalue()
          >>> len([line for line in output.split('\n') if 'funcname' in line]) < 1000
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('eyed', 'ey', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('place', 'york', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('prep', 'ounce', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('coed', 'coed', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('goofy', 'oxyl', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('silly', 'silly', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('grain', 'gz', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('winna', 'woinna', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('baku', 'baku', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('mark', 'laker', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('ethos', 'jzos', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('lend', 'erne', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('skid', 'widd', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('study', 'study', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('scold', 'cq', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('flamy', 'fak', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('dotal', 'dotl', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('mince', 'mqince', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('ada', 'cdca', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('minar', 'chain', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('tough', 'tojwh', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('teet', 'home', k) > k for k in range(4)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('mumps', 'tuts', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('heart', 'heart', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('qoph', 'death', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('dheri', 'zbr', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('keeve', 'keve', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('boort', 'stulm', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('jodel', 'jodeal', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('dabba', 'fan', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('cloak', 'wind', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('sung', 'guskg', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('mon', 'moy', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('lover', 'lover', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('omer', 'mr', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('cibol', 'zibox', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('menu', 'exeat', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('blvd', 'km', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('sensa', 'sine', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('enrol', 'lungy', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('octet', 'ctbs', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('manga', 'guama', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('trike', 'tskhikue', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('skete', 'skete', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('site', 'xdit', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('demob', 'ratwa', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('tinea', 'wreat', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('break', 'libs', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('tubae', 'huqqe', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('run', 'tsuba', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('shy', 'shy', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('terma', 'tfrma', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('krama', 'kradmxk', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('jesse', 'jesqe', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('essay', 'ssar', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('begun', 'begun', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('vii', 'vii', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('rides', 'rides', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('alga', 'alga', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('asker', 'akx', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('rocky', 'rociky', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('crain', 'ckci', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('kinch', 'kinch', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('bort', 'bort', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('deter', 'gale', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('gaize', 'gaize', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('heme', 'hhtem', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('boats', 'bnoats', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('mown', 'yomn', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('anana', 'waa', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('peasy', 'xuas', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('pie', 'tizzy', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('quin', 'iupi', k) > k for k in range(4)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('among', 'sculp', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('ja', 'a', k) > k for k in range(2)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('aube', 'aube', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('mf', 'kf', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('ta', 'jowl', k) > k for k in range(4)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('downy', 'downy', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('brook', 'sxook', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('brood', 'browao', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('unset', 'rocky', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('pole', 'plec', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('dir', 'dir', k) > k for k in range(3)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('rider', 'rider', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('urate', 'ura', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('swift', 'gade', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('gucki', 'guiai', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('dang', 'dqanf', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('cruth', 'ashruth', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('aloof', 'alafof', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('alive', 'alv', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('arow', 'arxgw', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('lemon', 'sahib', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('moire', 'dean', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('feaze', 'febzhc', k) > k for k in range(6)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('socii', 'soib', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('mashy', 'mash', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('a', 'a', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('salol', 'salol', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import minimum_mewtations, autocorrect
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
