test = {
  'name': 'Problem 9',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> p = [[1, 4, 6, 7], [0, 4, 6, 9]]
          >>> words = ['This', 'is', 'fun']
          >>> match = time_per_word(words, p)
          >>> get_words(match)
          ['This', 'is', 'fun']
          >>> get_times(match)
          [[3, 2, 1], [4, 2, 3]]
          >>> p = [[0, 2, 3], [2, 4, 7]]
          >>> match = time_per_word(['hello', 'world'], p)
          >>> word_at(match, word_index=1)
          'world'
          >>> get_times(match)
          [[2, 1], [2, 3]]
          >>> time(match, player_num=0, word_index=1)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[83, 86, 87, 92, 94], [21, 26, 27, 30, 31]]
          >>> match = time_per_word(['colophonium', 'spatangoid', 'newsstand', 'stereochromy'], p)
          >>> get_words(match)
          ['colophonium', 'spatangoid', 'newsstand', 'stereochromy']
          >>> get_times(match)
          [[3, 1, 5, 2], [5, 1, 3, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[16, 18, 23, 28, 30, 33]]
          >>> match = time_per_word(['unstatesmanlike', 'median', 'cueca', 'meroplankton', 'foremilk'], p)
          >>> get_words(match)
          ['unstatesmanlike', 'median', 'cueca', 'meroplankton', 'foremilk']
          >>> get_times(match)
          [[2, 5, 5, 2, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[72], [22]]
          >>> match = time_per_word([], p)
          >>> get_words(match)
          []
          >>> get_times(match)
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[72, 73, 77]]
          >>> match = time_per_word(['uncommixed', 'gentlewomanly'], p)
          >>> get_words(match)
          ['uncommixed', 'gentlewomanly']
          >>> get_times(match)
          [[1, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[87, 90, 93], [72, 74, 79]]
          >>> match = time_per_word(['unmistakableness', 'musiclike'], p)
          >>> get_words(match)
          ['unmistakableness', 'musiclike']
          >>> get_times(match)
          [[3, 3], [2, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[16, 21, 22, 23], [73, 77, 82, 86], [8, 9, 11, 16]]
          >>> match = time_per_word(['antinoise', 'archcupbearer', 'opisthotonoid'], p)
          >>> get_words(match)
          ['antinoise', 'archcupbearer', 'opisthotonoid']
          >>> get_times(match)
          [[5, 1, 1], [4, 5, 4], [1, 2, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[79, 82, 83]]
          >>> match = time_per_word(['nephros', 'cixiid'], p)
          >>> get_words(match)
          ['nephros', 'cixiid']
          >>> get_times(match)
          [[3, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[57, 58, 60, 63, 66]]
          >>> match = time_per_word(['crural', 'accredit', 'deltation', 'esophagomalacia'], p)
          >>> get_words(match)
          ['crural', 'accredit', 'deltation', 'esophagomalacia']
          >>> get_times(match)
          [[1, 2, 3, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[83, 84, 85, 90]]
          >>> match = time_per_word(['basiradial', 'pseudoliterary', 'electroextraction'], p)
          >>> get_words(match)
          ['basiradial', 'pseudoliterary', 'electroextraction']
          >>> get_times(match)
          [[1, 1, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[65, 69, 71, 73, 78, 81, 86], [22, 23, 24, 29, 33, 34, 35], [52, 55, 59, 60, 61, 64, 69]]
          >>> match = time_per_word(['horde', 'termolecular', 'unbeatably', 'unamenable', 'ratio', 'speciology'], p)
          >>> get_words(match)
          ['horde', 'termolecular', 'unbeatably', 'unamenable', 'ratio', 'speciology']
          >>> get_times(match)
          [[4, 2, 2, 5, 3, 5], [1, 1, 5, 4, 1, 1], [3, 4, 1, 1, 3, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[28, 30]]
          >>> match = time_per_word(['interlardment'], p)
          >>> get_words(match)
          ['interlardment']
          >>> get_times(match)
          [[2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[91, 93]]
          >>> match = time_per_word(['casual'], p)
          >>> get_words(match)
          ['casual']
          >>> get_times(match)
          [[2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[48, 50, 55, 57]]
          >>> match = time_per_word(['purblindly', 'chromo', 'casson'], p)
          >>> get_words(match)
          ['purblindly', 'chromo', 'casson']
          >>> get_times(match)
          [[2, 5, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[25, 30, 33]]
          >>> match = time_per_word(['strigal', 'scrawler'], p)
          >>> get_words(match)
          ['strigal', 'scrawler']
          >>> get_times(match)
          [[5, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[28, 29, 32, 36], [10, 11, 13, 14]]
          >>> match = time_per_word(['gormandize', 'pochay', 'negotiatrix'], p)
          >>> get_words(match)
          ['gormandize', 'pochay', 'negotiatrix']
          >>> get_times(match)
          [[1, 3, 4], [1, 2, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[12], [5]]
          >>> match = time_per_word([], p)
          >>> get_words(match)
          []
          >>> get_times(match)
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[65, 70], [68, 70]]
          >>> match = time_per_word(['pectous'], p)
          >>> get_words(match)
          ['pectous']
          >>> get_times(match)
          [[5], [2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[22, 27], [57, 62], [45, 50]]
          >>> match = time_per_word(['campylometer'], p)
          >>> get_words(match)
          ['campylometer']
          >>> get_times(match)
          [[5], [5], [5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[62, 65, 66], [49, 52, 53]]
          >>> match = time_per_word(['intercrescence', 'incendiarism'], p)
          >>> get_words(match)
          ['intercrescence', 'incendiarism']
          >>> get_times(match)
          [[3, 1], [3, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[74, 77, 78, 81, 83, 86]]
          >>> match = time_per_word(['unrioting', 'heaps', 'kitling', 'workhouse', 'scriver'], p)
          >>> get_words(match)
          ['unrioting', 'heaps', 'kitling', 'workhouse', 'scriver']
          >>> get_times(match)
          [[3, 1, 3, 2, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[90, 92, 97, 101]]
          >>> match = time_per_word(['infanglement', 'cavern', 'autotriploid'], p)
          >>> get_words(match)
          ['infanglement', 'cavern', 'autotriploid']
          >>> get_times(match)
          [[2, 5, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 5]]
          >>> match = time_per_word(['fiddley'], p)
          >>> get_words(match)
          ['fiddley']
          >>> get_times(match)
          [[1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[8, 13, 16, 21, 22, 25]]
          >>> match = time_per_word(['saponify', 'bakerless', 'nonluminous', 'zonesthesia', 'argumentatively'], p)
          >>> get_words(match)
          ['saponify', 'bakerless', 'nonluminous', 'zonesthesia', 'argumentatively']
          >>> get_times(match)
          [[5, 3, 5, 1, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[31, 36, 40, 43]]
          >>> match = time_per_word(['overfrailty', 'affair', 'gelatinizability'], p)
          >>> get_words(match)
          ['overfrailty', 'affair', 'gelatinizability']
          >>> get_times(match)
          [[5, 4, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[17, 22, 27], [1, 5, 9]]
          >>> match = time_per_word(['toys', 'uranophane'], p)
          >>> get_words(match)
          ['toys', 'uranophane']
          >>> get_times(match)
          [[5, 5], [4, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[23, 24, 26, 30, 35], [44, 49, 54, 55, 59], [50, 55, 57, 61, 63]]
          >>> match = time_per_word(['impercipient', 'ali', 'indult', 'palmitic'], p)
          >>> get_words(match)
          ['impercipient', 'ali', 'indult', 'palmitic']
          >>> get_times(match)
          [[1, 2, 4, 5], [5, 5, 1, 4], [5, 2, 4, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[90, 95, 97, 99, 100, 104], [32, 35, 39, 44, 47, 48]]
          >>> match = time_per_word(['rubberneck', 'telangiectasy', 'unratable', 'dissolvableness', 'redheadedly'], p)
          >>> get_words(match)
          ['rubberneck', 'telangiectasy', 'unratable', 'dissolvableness', 'redheadedly']
          >>> get_times(match)
          [[5, 2, 2, 1, 4], [3, 4, 5, 3, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[37, 38, 40, 42]]
          >>> match = time_per_word(['nocturia', 'cataphyllum', 'alroot'], p)
          >>> get_words(match)
          ['nocturia', 'cataphyllum', 'alroot']
          >>> get_times(match)
          [[1, 2, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[22, 26], [32, 37]]
          >>> match = time_per_word(['undissenting'], p)
          >>> get_words(match)
          ['undissenting']
          >>> get_times(match)
          [[4], [5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[83, 84, 88, 93, 98, 101], [97, 99, 103, 104, 107, 111]]
          >>> match = time_per_word(['accresce', 'during', 'unreproachableness', 'incomputable', 'sulphosuccinic'], p)
          >>> get_words(match)
          ['accresce', 'during', 'unreproachableness', 'incomputable', 'sulphosuccinic']
          >>> get_times(match)
          [[1, 4, 5, 5, 3], [2, 4, 1, 3, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[53, 57, 59, 62, 67, 68], [17, 19, 23, 28, 29, 33], [46, 48, 51, 56, 60, 65]]
          >>> match = time_per_word(['unembraced', 'counterprotection', 'karyolysis', 'contuse', 'esophagomalacia'], p)
          >>> get_words(match)
          ['unembraced', 'counterprotection', 'karyolysis', 'contuse', 'esophagomalacia']
          >>> get_times(match)
          [[4, 2, 3, 5, 1], [2, 4, 5, 1, 4], [2, 3, 5, 4, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[23, 28, 31], [58, 63, 66], [28, 31, 34]]
          >>> match = time_per_word(['resay', 'benjy'], p)
          >>> get_words(match)
          ['resay', 'benjy']
          >>> get_times(match)
          [[5, 3], [5, 3], [3, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[88, 90, 92, 94], [19, 23, 28, 32], [71, 74, 78, 80]]
          >>> match = time_per_word(['pantomime', 'fumatory', 'driftpiece'], p)
          >>> get_words(match)
          ['pantomime', 'fumatory', 'driftpiece']
          >>> get_times(match)
          [[2, 2, 2], [4, 5, 4], [3, 4, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[67, 71, 74, 76, 79], [61, 66, 70, 75, 80]]
          >>> match = time_per_word(['uncurl', 'lobulose', 'parapsychical', 'revengement'], p)
          >>> get_words(match)
          ['uncurl', 'lobulose', 'parapsychical', 'revengement']
          >>> get_times(match)
          [[4, 3, 2, 3], [5, 4, 5, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[85, 89], [68, 71], [35, 38]]
          >>> match = time_per_word(['lintwhite'], p)
          >>> get_words(match)
          ['lintwhite']
          >>> get_times(match)
          [[4], [3], [3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[55, 57]]
          >>> match = time_per_word(['myristicaceous'], p)
          >>> get_words(match)
          ['myristicaceous']
          >>> get_times(match)
          [[2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[55, 60, 64, 66, 71, 75], [6, 7, 9, 14, 19, 23]]
          >>> match = time_per_word(['swearingly', 'pimple', 'unbundled', 'bencite', 'unfrustrably'], p)
          >>> get_words(match)
          ['swearingly', 'pimple', 'unbundled', 'bencite', 'unfrustrably']
          >>> get_times(match)
          [[5, 4, 2, 5, 4], [1, 2, 5, 5, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[22, 26, 27, 28], [35, 38, 39, 43]]
          >>> match = time_per_word(['unpapal', 'saiga', 'unbungling'], p)
          >>> get_words(match)
          ['unpapal', 'saiga', 'unbungling']
          >>> get_times(match)
          [[4, 1, 1], [3, 1, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[83, 88], [60, 63]]
          >>> match = time_per_word(['rhymemaking'], p)
          >>> get_words(match)
          ['rhymemaking']
          >>> get_times(match)
          [[5], [3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[20, 24]]
          >>> match = time_per_word(['uninterlocked'], p)
          >>> get_words(match)
          ['uninterlocked']
          >>> get_times(match)
          [[4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[12, 15, 18, 22, 24, 26, 27], [71, 75, 79, 83, 84, 86, 91]]
          >>> match = time_per_word(['moly', 'boldness', 'uraniid', 'inherently', 'diphenol', 'dermoskeleton'], p)
          >>> get_words(match)
          ['moly', 'boldness', 'uraniid', 'inherently', 'diphenol', 'dermoskeleton']
          >>> get_times(match)
          [[3, 3, 4, 2, 2, 1], [4, 4, 4, 1, 2, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[98]]
          >>> match = time_per_word([], p)
          >>> get_words(match)
          []
          >>> get_times(match)
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[82, 85, 88, 92, 97, 99, 100], [86, 91, 96, 98, 99, 104, 105], [74, 78, 80, 84, 88, 92, 95]]
          >>> match = time_per_word(['probationism', 'pargeboard', 'liquidly', 'nongentile', 'metrification', 'unseamanship'], p)
          >>> get_words(match)
          ['probationism', 'pargeboard', 'liquidly', 'nongentile', 'metrification', 'unseamanship']
          >>> get_times(match)
          [[3, 3, 4, 5, 2, 1], [5, 5, 2, 1, 5, 1], [4, 2, 4, 4, 4, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[51, 53, 57, 61, 64]]
          >>> match = time_per_word(['purloiner', 'cinnabarine', 'orlop', 'ovolo'], p)
          >>> get_words(match)
          ['purloiner', 'cinnabarine', 'orlop', 'ovolo']
          >>> get_times(match)
          [[2, 4, 4, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[84, 88, 91, 92, 94]]
          >>> match = time_per_word(['undersheriffship', 'remonetize', 'crustation', 'syntypicism'], p)
          >>> get_words(match)
          ['undersheriffship', 'remonetize', 'crustation', 'syntypicism']
          >>> get_times(match)
          [[4, 3, 1, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[95, 99, 104, 106]]
          >>> match = time_per_word(['physiological', 'truantly', 'photomezzotype'], p)
          >>> get_words(match)
          ['physiological', 'truantly', 'photomezzotype']
          >>> get_times(match)
          [[4, 5, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[75, 79, 82, 85, 88, 89], [93, 94, 95, 99, 102, 107], [60, 64, 65, 68, 69, 70]]
          >>> match = time_per_word(['zymin', 'bloodstroke', 'dioestrous', 'heterochthonous', 'supraseptal'], p)
          >>> get_words(match)
          ['zymin', 'bloodstroke', 'dioestrous', 'heterochthonous', 'supraseptal']
          >>> get_times(match)
          [[4, 3, 3, 3, 1], [1, 1, 4, 3, 5], [4, 1, 3, 1, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[55, 58, 62, 66, 67, 70, 72], [50, 53, 55, 60, 62, 64, 65]]
          >>> match = time_per_word(['actiniochrome', 'reassimilation', 'bandicoot', 'nettlefoot', 'macarism', 'usurp'], p)
          >>> get_words(match)
          ['actiniochrome', 'reassimilation', 'bandicoot', 'nettlefoot', 'macarism', 'usurp']
          >>> get_times(match)
          [[3, 4, 4, 1, 3, 2], [3, 2, 5, 2, 2, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[68], [91]]
          >>> match = time_per_word([], p)
          >>> get_words(match)
          []
          >>> get_times(match)
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[12, 17, 22], [69, 71, 76], [5, 8, 9]]
          >>> match = time_per_word(['teems', 'haematosepsis'], p)
          >>> get_words(match)
          ['teems', 'haematosepsis']
          >>> get_times(match)
          [[5, 5], [2, 5], [3, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[11]]
          >>> match = time_per_word([], p)
          >>> get_words(match)
          []
          >>> get_times(match)
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[94, 96, 101, 106, 110, 115, 120], [52, 55, 60, 65, 69, 72, 75]]
          >>> match = time_per_word(['labroid', 'prophasis', 'uncomplimented', 'subside', 'pseudandry', 'saltcat'], p)
          >>> get_words(match)
          ['labroid', 'prophasis', 'uncomplimented', 'subside', 'pseudandry', 'saltcat']
          >>> get_times(match)
          [[2, 5, 5, 4, 5, 5], [3, 5, 5, 4, 3, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[69, 72, 76, 80, 83, 87]]
          >>> match = time_per_word(['coconscious', 'diploglossate', 'fatalistic', 'ow', 'disquietedness'], p)
          >>> get_words(match)
          ['coconscious', 'diploglossate', 'fatalistic', 'ow', 'disquietedness']
          >>> get_times(match)
          [[3, 4, 4, 3, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[37, 42], [61, 62]]
          >>> match = time_per_word(['thunderousness'], p)
          >>> get_words(match)
          ['thunderousness']
          >>> get_times(match)
          [[5], [1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[9, 11, 16, 21, 22, 26], [6, 11, 16, 17, 19, 22]]
          >>> match = time_per_word(['heavenish', 'dysmetria', 'cl', 'posthexaplaric', 'dinglebird'], p)
          >>> get_words(match)
          ['heavenish', 'dysmetria', 'cl', 'posthexaplaric', 'dinglebird']
          >>> get_times(match)
          [[2, 5, 5, 1, 4], [5, 5, 1, 2, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[55, 59, 60, 65, 67, 71], [37, 39, 43, 44, 45, 48]]
          >>> match = time_per_word(['lands', 'rippable', 'hectical', 'profanism', 'pachysalpingitis'], p)
          >>> get_words(match)
          ['lands', 'rippable', 'hectical', 'profanism', 'pachysalpingitis']
          >>> get_times(match)
          [[4, 1, 5, 2, 4], [2, 4, 1, 1, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[87, 92, 95, 96, 99, 103], [22, 24, 26, 31, 35, 36]]
          >>> match = time_per_word(['scleranth', 'perdricide', 'renably', 'sorn', 'glutting'], p)
          >>> get_words(match)
          ['scleranth', 'perdricide', 'renably', 'sorn', 'glutting']
          >>> get_times(match)
          [[5, 3, 1, 3, 4], [2, 2, 5, 4, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[37, 41, 43, 45, 46, 51, 54], [72, 73, 76, 79, 81, 83, 84]]
          >>> match = time_per_word(['cardiectomy', 'mien', 'wellness', 'antitobacconist', 'zoosporangiophore', 'sarcogenous'], p)
          >>> get_words(match)
          ['cardiectomy', 'mien', 'wellness', 'antitobacconist', 'zoosporangiophore', 'sarcogenous']
          >>> get_times(match)
          [[4, 2, 2, 1, 5, 3], [1, 3, 3, 2, 2, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[21, 23, 28, 33], [35, 38, 43, 46], [25, 26, 29, 30]]
          >>> match = time_per_word(['unidealistic', 'pretermitter', 'automatist'], p)
          >>> get_words(match)
          ['unidealistic', 'pretermitter', 'automatist']
          >>> get_times(match)
          [[2, 5, 5], [3, 5, 3], [1, 3, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[57, 61], [0, 1]]
          >>> match = time_per_word(['prefacer'], p)
          >>> get_words(match)
          ['prefacer']
          >>> get_times(match)
          [[4], [1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[33, 38, 42, 47, 51, 52], [87, 90, 95, 96, 99, 103], [40, 41, 44, 47, 52, 57]]
          >>> match = time_per_word(['toxic', 'sphaeristerium', 'sexualization', 'tugurium', 'epineurium'], p)
          >>> get_words(match)
          ['toxic', 'sphaeristerium', 'sexualization', 'tugurium', 'epineurium']
          >>> get_times(match)
          [[5, 4, 5, 4, 1], [3, 5, 1, 3, 4], [1, 3, 3, 5, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[34, 39, 41, 46], [42, 46, 49, 52], [65, 66, 70, 74]]
          >>> match = time_per_word(['appositionally', 'earthly', 'orchiocatabasis'], p)
          >>> get_words(match)
          ['appositionally', 'earthly', 'orchiocatabasis']
          >>> get_times(match)
          [[5, 2, 5], [4, 3, 3], [1, 4, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[11, 13, 15], [58, 63, 65]]
          >>> match = time_per_word(['americium', 'polariscopy'], p)
          >>> get_words(match)
          ['americium', 'polariscopy']
          >>> get_times(match)
          [[2, 2], [5, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[17, 18, 22, 25, 30]]
          >>> match = time_per_word(['acrocephaly', 'brushed', 'removedness', 'peenge'], p)
          >>> get_words(match)
          ['acrocephaly', 'brushed', 'removedness', 'peenge']
          >>> get_times(match)
          [[1, 4, 3, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[51, 52, 53, 56, 57]]
          >>> match = time_per_word(['humicubation', 'hyperdulic', 'crimple', 'soother'], p)
          >>> get_words(match)
          ['humicubation', 'hyperdulic', 'crimple', 'soother']
          >>> get_times(match)
          [[1, 1, 3, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[6, 7, 8, 10, 15, 18, 21], [1, 3, 5, 8, 11, 14, 15]]
          >>> match = time_per_word(['abstractedly', 'parapsidal', 'unattendance', 'expirable', 'wheelwright', 'rind'], p)
          >>> get_words(match)
          ['abstractedly', 'parapsidal', 'unattendance', 'expirable', 'wheelwright', 'rind']
          >>> get_times(match)
          [[1, 1, 2, 5, 3, 3], [2, 2, 3, 3, 3, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[79, 83, 84, 88, 91], [90, 93, 97, 100, 101]]
          >>> match = time_per_word(['oliguresis', 'plethoretical', 'plantlike', 'electrotechnology'], p)
          >>> get_words(match)
          ['oliguresis', 'plethoretical', 'plantlike', 'electrotechnology']
          >>> get_times(match)
          [[4, 1, 4, 3], [3, 4, 3, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[9, 13, 17, 21], [91, 93, 94, 99]]
          >>> match = time_per_word(['hubber', 'patrology', 'spermatophore'], p)
          >>> get_words(match)
          ['hubber', 'patrology', 'spermatophore']
          >>> get_times(match)
          [[4, 4, 4], [2, 1, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[28, 33, 37], [24, 29, 33], [23, 28, 32]]
          >>> match = time_per_word(['miskindle', 'deathbed'], p)
          >>> get_words(match)
          ['miskindle', 'deathbed']
          >>> get_times(match)
          [[5, 4], [5, 4], [5, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[9, 10, 13, 17, 20, 21, 25], [56, 57, 62, 63, 67, 69, 74], [97, 102, 106, 107, 108, 111, 115]]
          >>> match = time_per_word(['nummi', 'undisparaged', 'polarly', 'baldachino', 'strumae', 'posttoxic'], p)
          >>> get_words(match)
          ['nummi', 'undisparaged', 'polarly', 'baldachino', 'strumae', 'posttoxic']
          >>> get_times(match)
          [[1, 3, 4, 3, 1, 4], [1, 5, 1, 4, 2, 5], [5, 4, 1, 1, 3, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[84, 89, 92, 97, 98, 101, 105], [72, 74, 76, 78, 83, 86, 89], [96, 101, 102, 105, 108, 112, 113]]
          >>> match = time_per_word(['wraprascal', 'renominate', 'quondam', 'gullibility', 'staysail', 'unfleshly'], p)
          >>> get_words(match)
          ['wraprascal', 'renominate', 'quondam', 'gullibility', 'staysail', 'unfleshly']
          >>> get_times(match)
          [[5, 3, 5, 1, 3, 4], [2, 2, 2, 5, 3, 3], [5, 1, 3, 3, 4, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[40, 43, 45, 46]]
          >>> match = time_per_word(['microclimatological', 'acquaintancy', 'tarsoplasty'], p)
          >>> get_words(match)
          ['microclimatological', 'acquaintancy', 'tarsoplasty']
          >>> get_times(match)
          [[3, 2, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[74], [94], [69]]
          >>> match = time_per_word([], p)
          >>> get_words(match)
          []
          >>> get_times(match)
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[71, 76, 80, 85, 86, 90, 95], [97, 101, 104, 108, 112, 114, 116], [53, 55, 60, 62, 64, 69, 72]]
          >>> match = time_per_word(['impanate', 'undisinfected', 'unnapkined', 'stockwright', 'nonconcern', 'clandestineness'], p)
          >>> get_words(match)
          ['impanate', 'undisinfected', 'unnapkined', 'stockwright', 'nonconcern', 'clandestineness']
          >>> get_times(match)
          [[5, 4, 5, 1, 4, 5], [4, 3, 4, 4, 2, 2], [2, 5, 2, 2, 5, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[11, 13, 17, 20, 24, 27, 31], [31, 35, 36, 39, 43, 45, 48]]
          >>> match = time_per_word(['agamogenesis', 'gmbh', 'toothy', 'achromatism', 'uintathere', 'horrorsome'], p)
          >>> get_words(match)
          ['agamogenesis', 'gmbh', 'toothy', 'achromatism', 'uintathere', 'horrorsome']
          >>> get_times(match)
          [[2, 4, 3, 4, 3, 4], [4, 1, 3, 4, 2, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[19]]
          >>> match = time_per_word([], p)
          >>> get_words(match)
          []
          >>> get_times(match)
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[26, 29]]
          >>> match = time_per_word(['unstoried'], p)
          >>> get_words(match)
          ['unstoried']
          >>> get_times(match)
          [[3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[57, 62, 66, 67, 71]]
          >>> match = time_per_word(['tomblet', 'wapp', 'matrix', 'pitfall'], p)
          >>> get_words(match)
          ['tomblet', 'wapp', 'matrix', 'pitfall']
          >>> get_times(match)
          [[5, 4, 1, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[78, 82, 87, 88, 92, 97]]
          >>> match = time_per_word(['angiocholecystitis', 'yoven', 'lovably', 'sheepmonger', 'molave'], p)
          >>> get_words(match)
          ['angiocholecystitis', 'yoven', 'lovably', 'sheepmonger', 'molave']
          >>> get_times(match)
          [[4, 5, 1, 4, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 6, 10, 13, 16]]
          >>> match = time_per_word(['virify', 'ferrohydrocyanic', 'wambly', 'hydrotechnic', 'capillose'], p)
          >>> get_words(match)
          ['virify', 'ferrohydrocyanic', 'wambly', 'hydrotechnic', 'capillose']
          >>> get_times(match)
          [[2, 3, 4, 3, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[23, 26, 28, 31, 36], [15, 20, 22, 27, 30], [81, 82, 87, 91, 96]]
          >>> match = time_per_word(['aphesis', 'lactase', 'pleionian', 'guige'], p)
          >>> get_words(match)
          ['aphesis', 'lactase', 'pleionian', 'guige']
          >>> get_times(match)
          [[3, 2, 3, 5], [5, 2, 5, 3], [1, 5, 4, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[49, 51, 53, 57], [42, 46, 51, 52]]
          >>> match = time_per_word(['overstalled', 'obstupefy', 'predeparture'], p)
          >>> get_words(match)
          ['overstalled', 'obstupefy', 'predeparture']
          >>> get_times(match)
          [[2, 2, 4], [4, 5, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[31, 34, 36, 40], [98, 100, 104, 106], [80, 85, 89, 94]]
          >>> match = time_per_word(['operated', 'cithara', 'apparent'], p)
          >>> get_words(match)
          ['operated', 'cithara', 'apparent']
          >>> get_times(match)
          [[3, 2, 4], [2, 4, 2], [5, 4, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[0, 1, 5]]
          >>> match = time_per_word(['translocate', 'contradictive'], p)
          >>> get_words(match)
          ['translocate', 'contradictive']
          >>> get_times(match)
          [[1, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[78, 79, 81]]
          >>> match = time_per_word(['institute', 'agamid'], p)
          >>> get_words(match)
          ['institute', 'agamid']
          >>> get_times(match)
          [[1, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[51, 56, 60]]
          >>> match = time_per_word(['blastophthoric', 'subscience'], p)
          >>> get_words(match)
          ['blastophthoric', 'subscience']
          >>> get_times(match)
          [[5, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[9, 13, 15, 20, 22]]
          >>> match = time_per_word(['optotype', 'raise', 'placentitis', 'virtualism'], p)
          >>> get_words(match)
          ['optotype', 'raise', 'placentitis', 'virtualism']
          >>> get_times(match)
          [[4, 2, 5, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[9, 14, 15, 18, 19, 23, 27]]
          >>> match = time_per_word(['clanjamphrey', 'belord', 'vermeology', 'wrive', 'phellodermal', 'weaponry'], p)
          >>> get_words(match)
          ['clanjamphrey', 'belord', 'vermeology', 'wrive', 'phellodermal', 'weaponry']
          >>> get_times(match)
          [[5, 1, 3, 1, 4, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[79]]
          >>> match = time_per_word([], p)
          >>> get_words(match)
          []
          >>> get_times(match)
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[43, 46, 49, 50], [58, 63, 67, 72], [8, 10, 11, 13]]
          >>> match = time_per_word(['disensure', 'flashing', 'swarfer'], p)
          >>> get_words(match)
          ['disensure', 'flashing', 'swarfer']
          >>> get_times(match)
          [[3, 3, 1], [5, 4, 5], [2, 1, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[58, 61, 64, 65]]
          >>> match = time_per_word(['semiography', 'phosphoaminolipide', 'unilocularity'], p)
          >>> get_words(match)
          ['semiography', 'phosphoaminolipide', 'unilocularity']
          >>> get_times(match)
          [[3, 3, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[93, 96, 101], [29, 34, 36], [36, 39, 41]]
          >>> match = time_per_word(['coast', 'stageably'], p)
          >>> get_words(match)
          ['coast', 'stageably']
          >>> get_times(match)
          [[3, 5], [5, 2], [3, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[11, 16, 19], [70, 73, 75], [15, 18, 23]]
          >>> match = time_per_word(['interacinous', 'boycottism'], p)
          >>> get_words(match)
          ['interacinous', 'boycottism']
          >>> get_times(match)
          [[5, 3], [3, 2], [3, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[48, 53, 55, 57, 59, 60], [77, 82, 86, 89, 90, 91]]
          >>> match = time_per_word(['gormed', 'spry', 'agrobiological', 'zaphara', 'unlessoned'], p)
          >>> get_words(match)
          ['gormed', 'spry', 'agrobiological', 'zaphara', 'unlessoned']
          >>> get_times(match)
          [[5, 2, 2, 2, 1], [5, 4, 3, 1, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[22, 26, 27, 30], [93, 94, 97, 102], [56, 57, 59, 61]]
          >>> match = time_per_word(['motel', 'ten', 'kittendom'], p)
          >>> get_words(match)
          ['motel', 'ten', 'kittendom']
          >>> get_times(match)
          [[4, 1, 3], [1, 3, 5], [1, 2, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[97, 100, 105, 109, 113, 118, 123], [96, 97, 101, 105, 110, 112, 116], [20, 22, 26, 31, 34, 35, 38]]
          >>> match = time_per_word(['exhibitions', 'durational', 'templarlikeness', 'boghole', 'tersulphate', 'slubby'], p)
          >>> get_words(match)
          ['exhibitions', 'durational', 'templarlikeness', 'boghole', 'tersulphate', 'slubby']
          >>> get_times(match)
          [[3, 5, 4, 4, 5, 5], [1, 4, 4, 5, 2, 4], [2, 4, 5, 3, 1, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[97, 101, 104, 109, 111], [66, 68, 73, 76, 79]]
          >>> match = time_per_word(['blackishly', 'fungous', 'script', 'rais'], p)
          >>> get_words(match)
          ['blackishly', 'fungous', 'script', 'rais']
          >>> get_times(match)
          [[4, 3, 5, 2], [2, 5, 3, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[71, 75, 76], [28, 33, 36]]
          >>> match = time_per_word(['garruline', 'immusical'], p)
          >>> get_words(match)
          ['garruline', 'immusical']
          >>> get_times(match)
          [[4, 1], [5, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[65, 67, 70], [68, 71, 73]]
          >>> match = time_per_word(['ogam', 'wettish'], p)
          >>> get_words(match)
          ['ogam', 'wettish']
          >>> get_times(match)
          [[2, 3], [3, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[40, 41], [73, 76]]
          >>> match = time_per_word(['autometric'], p)
          >>> get_words(match)
          ['autometric']
          >>> get_times(match)
          [[1], [3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> test.swap_implementations(cats) # Make sure the abstraction barrier isn't crossed!
          >>> p = [[1, 4, 6, 7], [0, 4, 6, 9]]
          >>> words = ['This', 'is', 'fun']
          >>> match = cats.time_per_word(words, p)
          >>> cats.get_words(match)
          ['This', 'is', 'fun']
          >>> cats.get_times(match)
          [[3, 2, 1], [4, 2, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import cats
      >>> import tests.abstraction_check as test # Make sure the abstraction barrier isn't crossed!
      """,
      'teardown': r"""
      >>> test.restore_implementations(cats)
      """,
      'type': 'doctest'
    }
  ]
}
