test = {
  'name': 'Problem 10',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> p0 = [2, 2, 3]
          >>> p1 = [6, 1, 2]
          >>> fastest_words(match(['What', 'great', 'luck'], [p0, p1]))
          [['What'], ['great', 'luck']]
          >>> p0 = [2, 2, 3]
          >>> p1 = [6, 1, 3]
          >>> fastest_words(match(['What', 'great', 'luck'], [p0, p1]))  # with a tie, choose the first player
          [['What', 'luck'], ['great']]
          >>> p2 = [4, 3, 1]
          >>> fastest_words(match(['What', 'great', 'luck'], [p0, p1, p2]))
          [['What'], ['great'], ['luck']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p0 = [5, 1, 3]
          >>> p1 = [4, 1, 6]
          >>> fastest_words(match(['Just', 'have', 'fun'], [p0, p1]))
          [['have', 'fun'], ['Just']]
          >>> p0  # input lists should not be mutated
          [5, 1, 3]
          >>> p1
          [4, 1, 6]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 4, 3, 5, 1]]
          >>> fastest_words(match(['newsstand', 'stereochromy', 'quinaldine', 'invalidate', 'japingly'], p))
          [['newsstand', 'stereochromy', 'quinaldine', 'invalidate', 'japingly']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 1, 1], [2, 5, 5]]
          >>> fastest_words(match(['unstatesmanlike', 'median', 'cueca'], p))
          [['median', 'cueca'], ['unstatesmanlike']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 2, 4, 3]]
          >>> fastest_words(match(['introspectional', 'squamigerous', 'sair', 'heterodromy', 'butylene'], p))
          [['introspectional', 'squamigerous', 'sair', 'heterodromy', 'butylene']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(match([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 3, 5, 2, 1, 5], [3, 5, 3, 5, 4, 1], [2, 1, 3, 1, 2, 3]]
          >>> fastest_words(match(['musiclike', 'nonregarding', 'oxypropionic', 'postvide', 'muncheel', 'reburial'], p))
          [['musiclike', 'muncheel'], ['oxypropionic', 'reburial'], ['nonregarding', 'postvide']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 1, 1, 5, 2], [1, 4, 5, 4, 2], [5, 3, 2, 2, 3]]
          >>> fastest_words(match(['nuggety', 'phlegmatous', 'doomsman', 'butterfingered', 'scouse'], p))
          [['phlegmatous', 'doomsman', 'scouse'], ['nuggety'], ['butterfingered']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5], [3], [3]]
          >>> fastest_words(match(['cixiid'], p))
          [[], ['cixiid'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4]]
          >>> fastest_words(match(['accredit'], p))
          [['accredit']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1]]
          >>> fastest_words(match(['electroextraction'], p))
          [['electroextraction']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 2, 5, 4], [1, 3, 2, 1], [4, 2, 5, 1]]
          >>> fastest_words(match(['termolecular', 'unbeatably', 'unamenable', 'ratio'], p))
          [['unbeatably'], ['termolecular', 'unamenable', 'ratio'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 1, 2, 3, 1], [2, 1, 3, 1, 5]]
          >>> fastest_words(match(['interlardment', 'supercargo', 'inquilinity', 'mackenboy', 'trauma'], p))
          [['interlardment', 'supercargo', 'inquilinity', 'trauma'], ['mackenboy']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words(match([], p))
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 2, 5, 2, 3], [4, 3, 1, 1, 5], [3, 2, 4, 5, 4]]
          >>> fastest_words(match(['chromo', 'casson', 'unpliableness', 'overweeningly', 'unsquandered'], p))
          [['chromo', 'casson', 'unsquandered'], ['unpliableness', 'overweeningly'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(match([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 3, 1, 1]]
          >>> fastest_words(match(['negotiatrix', 'attaintment', 'concurringly', 'glyoxaline'], p))
          [['negotiatrix', 'attaintment', 'concurringly', 'glyoxaline']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 4, 2, 1, 3]]
          >>> fastest_words(match(['marble', 'undeleted', 'subrogation', 'lownly', 'nebulosity'], p))
          [['marble', 'undeleted', 'subrogation', 'lownly', 'nebulosity']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 2, 1, 1, 1, 3], [3, 5, 1, 2, 3, 3]]
          >>> fastest_words(match(['pectous', 'kathal', 'supercargoship', 'keelblock', 'celiosalpingectomy', 'pronumber'], p))
          [['kathal', 'supercargoship', 'keelblock', 'celiosalpingectomy', 'pronumber'], ['pectous']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 2, 2, 2, 1, 3], [3, 4, 4, 4, 2, 2]]
          >>> fastest_words(match(['coalhole', 'osmotic', 'barnard', 'irreligiousness', 'nitrobacteria', 'cellarless'], p))
          [['osmotic', 'barnard', 'irreligiousness', 'nitrobacteria'], ['coalhole', 'cellarless']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 3, 3], [1, 1, 3], [2, 3, 3]]
          >>> fastest_words(match(['incendiarism', 'carbamide', 'families'], p))
          [['families'], ['incendiarism', 'carbamide'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 1, 3, 2, 3, 3], [5, 1, 2, 4, 2, 5]]
          >>> fastest_words(match(['heaps', 'kitling', 'workhouse', 'scriver', 'chilicothe', 'anteprandial'], p))
          [['heaps', 'kitling', 'scriver', 'anteprandial'], ['workhouse', 'chilicothe']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 1, 1, 3], [3, 4, 4, 1], [1, 2, 3, 3]]
          >>> fastest_words(match(['brat', 'structureless', 'opacous', 'successfully'], p))
          [['structureless', 'opacous'], ['successfully'], ['brat']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words(match([], p))
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 5, 1, 5], [3, 5, 1, 3]]
          >>> fastest_words(match(['saponify', 'bakerless', 'nonluminous', 'zonesthesia'], p))
          [['bakerless', 'nonluminous'], ['saponify', 'zonesthesia']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(match([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 5, 4], [5, 4, 3], [4, 4, 4]]
          >>> fastest_words(match(['uranophane', 'whereso', 'toolmaking'], p))
          [['uranophane'], ['whereso', 'toolmaking'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 1, 5, 5, 2, 5]]
          >>> fastest_words(match(['ali', 'indult', 'palmitic', 'carbon', 'scudder', 'novaculite'], p))
          [['ali', 'indult', 'palmitic', 'carbon', 'scudder', 'novaculite']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 5, 3, 2, 4, 2], [5, 1, 3, 4, 1, 3]]
          >>> fastest_words(match(['telangiectasy', 'unratable', 'dissolvableness', 'redheadedly', 'recluse', 'galloon'], p))
          [['telangiectasy', 'dissolvableness', 'redheadedly', 'galloon'], ['unratable', 'recluse']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(match([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5], [1]]
          >>> fastest_words(match(['incorporable'], p))
          [[], ['incorporable']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 1, 4], [2, 1, 2]]
          >>> fastest_words(match(['accresce', 'during', 'unreproachableness'], p))
          [['accresce', 'during'], ['unreproachableness']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 2, 4, 2, 2], [2, 4, 3, 3, 5]]
          >>> fastest_words(match(['counterprotection', 'karyolysis', 'contuse', 'esophagomalacia', 'investigatorial'], p))
          [['karyolysis', 'esophagomalacia', 'investigatorial'], ['counterprotection', 'contuse']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(match([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 4, 3, 2, 5, 4], [2, 4, 2, 3, 4, 1]]
          >>> fastest_words(match(['driftpiece', 'archaic', 'oreotragine', 'nystagmic', 'refute', 'wellhole'], p))
          [['driftpiece', 'archaic', 'nystagmic'], ['oreotragine', 'refute', 'wellhole']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(match([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 4], [4, 3]]
          >>> fastest_words(match(['colly', 'ransackle'], p))
          [[], ['colly', 'ransackle']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 2, 1, 4], [4, 1, 1, 2]]
          >>> fastest_words(match(['clodpated', 'subcouncil', 'digestment', 'hierocratic'], p))
          [['clodpated', 'digestment'], ['subcouncil', 'hierocratic']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 3], [5, 2]]
          >>> fastest_words(match(['swearingly', 'pimple'], p))
          [['swearingly'], ['pimple']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 4, 4]]
          >>> fastest_words(match(['unbungling', 'rizzle', 'undistinguishableness'], p))
          [['unbungling', 'rizzle', 'undistinguishableness']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 3, 2], [2, 5, 1]]
          >>> fastest_words(match(['nonassortment', 'gowan', 'uneducable'], p))
          [['gowan'], ['nonassortment', 'uneducable']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1], [5]]
          >>> fastest_words(match(['uninterlocked'], p))
          [['uninterlocked'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 2], [5, 3, 4], [3, 4, 4]]
          >>> fastest_words(match(['boldness', 'uraniid', 'inherently'], p))
          [['boldness', 'uraniid', 'inherently'], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 2, 3]]
          >>> fastest_words(match(['eartab', 'wileful', 'manioc'], p))
          [['eartab', 'wileful', 'manioc']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 5, 2], [3, 3, 3], [5, 4, 3]]
          >>> fastest_words(match(['pargeboard', 'liquidly', 'nongentile'], p))
          [['nongentile'], ['pargeboard', 'liquidly'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(match([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 5, 4]]
          >>> fastest_words(match(['remonetize', 'crustation', 'syntypicism'], p))
          [['remonetize', 'crustation', 'syntypicism']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 5, 2], [1, 2, 2], [1, 1, 5]]
          >>> fastest_words(match(['photomezzotype', 'durian', 'precompletion'], p))
          [['precompletion'], ['photomezzotype'], ['durian']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 5, 4, 1, 4], [3, 1, 1, 3, 4]]
          >>> fastest_words(match(['bloodstroke', 'dioestrous', 'heterochthonous', 'supraseptal', 'heading'], p))
          [['supraseptal', 'heading'], ['bloodstroke', 'dioestrous', 'heterochthonous']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(match([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 5, 1]]
          >>> fastest_words(match(['podgily', 'collectivism', 'mitotically'], p))
          [['podgily', 'collectivism', 'mitotically']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 2, 3, 5, 5], [1, 3, 4, 3, 4], [2, 5, 5, 1, 4]]
          >>> fastest_words(match(['haematosepsis', 'apomecometry', 'yrs', 'briefly', 'urinometric'], p))
          [['apomecometry', 'yrs'], ['haematosepsis', 'urinometric'], ['briefly']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(match([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1], [2], [1]]
          >>> fastest_words(match(['prophasis'], p))
          [['prophasis'], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 4, 4], [3, 4, 4, 2]]
          >>> fastest_words(match(['diploglossate', 'fatalistic', 'ow', 'disquietedness'], p))
          [['diploglossate', 'fatalistic', 'ow'], ['disquietedness']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 1, 1, 3, 5], [2, 3, 3, 3, 2]]
          >>> fastest_words(match(['carbomethoxyl', 'dianilid', 'strack', 'whacky', 'stationery'], p))
          [['dianilid', 'strack', 'whacky'], ['carbomethoxyl', 'stationery']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 1], [1, 2]]
          >>> fastest_words(match(['dysmetria', 'cl'], p))
          [['cl'], ['dysmetria']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 2], [1, 4]]
          >>> fastest_words(match(['rippable', 'hectical'], p))
          [['hectical'], ['rippable']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 4, 5, 2], [3, 2, 1, 5]]
          >>> fastest_words(match(['scleranth', 'perdricide', 'renably', 'sorn'], p))
          [['scleranth', 'sorn'], ['perdricide', 'renably']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 2, 1, 4, 1], [2, 3, 2, 3, 1], [2, 5, 2, 3, 1]]
          >>> fastest_words(match(['mien', 'wellness', 'antitobacconist', 'zoosporangiophore', 'sarcogenous'], p))
          [['mien', 'wellness', 'antitobacconist', 'sarcogenous'], ['zoosporangiophore'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4]]
          >>> fastest_words(match(['nonactinic'], p))
          [['nonactinic']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 1, 4, 1], [4, 2, 1, 2]]
          >>> fastest_words(match(['prefacer', 'parasynetic', 'podogyne', 'ravissant'], p))
          [['prefacer', 'parasynetic', 'ravissant'], ['podogyne']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4], [1]]
          >>> fastest_words(match(['toxic'], p))
          [[], ['toxic']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 4], [3, 2], [5, 4]]
          >>> fastest_words(match(['orchiocatabasis', 'brangling'], p))
          [['orchiocatabasis'], ['brangling'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(match([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 1, 4, 3]]
          >>> fastest_words(match(['brushed', 'removedness', 'peenge', 'equid'], p))
          [['brushed', 'removedness', 'peenge', 'equid']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 1, 3, 1, 3, 1]]
          >>> fastest_words(match(['hyperdulic', 'crimple', 'soother', 'overkind', 'cinnamaldehyde', 'veretilliform'], p))
          [['hyperdulic', 'crimple', 'soother', 'overkind', 'cinnamaldehyde', 'veretilliform']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 1, 2, 1, 2], [2, 3, 5, 3, 3], [3, 3, 1, 4, 1]]
          >>> fastest_words(match(['parapsidal', 'unattendance', 'expirable', 'wheelwright', 'rind'], p))
          [['parapsidal', 'unattendance', 'wheelwright'], [], ['expirable', 'rind']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 4, 3, 1]]
          >>> fastest_words(match(['plethoretical', 'plantlike', 'electrotechnology', 'superioress'], p))
          [['plethoretical', 'plantlike', 'electrotechnology', 'superioress']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 4], [4, 2]]
          >>> fastest_words(match(['spermatophore', 'sapping'], p))
          [['spermatophore'], ['sapping']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 5, 5, 4], [4, 4, 1, 4], [4, 2, 2, 1]]
          >>> fastest_words(match(['gangrenous', 'lostness', 'doctrinarian', 'nonphosphorized'], p))
          [[], ['gangrenous', 'doctrinarian'], ['lostness', 'nonphosphorized']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 2, 2], [1, 2, 1], [1, 5, 3]]
          >>> fastest_words(match(['undisparaged', 'polarly', 'baldachino'], p))
          [['polarly'], ['undisparaged', 'baldachino'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 1, 1, 5, 2, 5], [3, 2, 1, 5, 2, 3], [1, 5, 3, 3, 3, 4]]
          >>> fastest_words(match(['wraprascal', 'renominate', 'quondam', 'gullibility', 'staysail', 'unfleshly'], p))
          [['renominate', 'quondam', 'staysail'], ['unfleshly'], ['wraprascal', 'gullibility']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 2, 1], [3, 2, 4]]
          >>> fastest_words(match(['tarsoplasty', 'unprincipal', 'myrmicoid'], p))
          [['tarsoplasty', 'unprincipal', 'myrmicoid'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 5, 1]]
          >>> fastest_words(match(['fibrinate', 'pillarlet', 'widdendream'], p))
          [['fibrinate', 'pillarlet', 'widdendream']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 1], [4, 2], [3, 2]]
          >>> fastest_words(match(['undisinfected', 'unnapkined'], p))
          [['undisinfected', 'unnapkined'], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 2, 5], [3, 4, 2], [4, 4, 1]]
          >>> fastest_words(match(['gmbh', 'toothy', 'achromatism'], p))
          [['toothy'], ['gmbh'], ['achromatism']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(match([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words(match([], p))
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 2, 5, 4]]
          >>> fastest_words(match(['wapp', 'matrix', 'pitfall', 'bardel'], p))
          [['wapp', 'matrix', 'pitfall', 'bardel']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 5, 1, 4, 5, 5], [1, 4, 5, 2, 3, 5]]
          >>> fastest_words(match(['yoven', 'lovably', 'sheepmonger', 'molave', 'hate', 'walloon'], p))
          [['sheepmonger', 'walloon'], ['yoven', 'lovably', 'molave', 'hate']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 3], [1, 2]]
          >>> fastest_words(match(['ferrohydrocyanic', 'wambly'], p))
          [['ferrohydrocyanic'], ['wambly']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 2, 3, 5, 1, 2]]
          >>> fastest_words(match(['lactase', 'pleionian', 'guige', 'tellureted', 'magistratically', 'playwrightry'], p))
          [['lactase', 'pleionian', 'guige', 'tellureted', 'magistratically', 'playwrightry']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words(match([], p))
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 2], [5, 2, 4], [4, 4, 2]]
          >>> fastest_words(match(['apparent', 'natron', 'mazopathia'], p))
          [['apparent', 'mazopathia'], ['natron'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(match([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1], [5], [1]]
          >>> fastest_words(match(['agamid'], p))
          [['agamid'], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(match([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(match([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 2, 5, 1, 3], [1, 4, 4, 1, 4], [1, 4, 3, 4, 2]]
          >>> fastest_words(match(['belord', 'vermeology', 'wrive', 'phellodermal', 'weaponry'], p))
          [['belord', 'vermeology', 'phellodermal'], [], ['wrive', 'weaponry']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(match([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 5, 2], [3, 4, 1, 1], [5, 2, 1, 2]]
          >>> fastest_words(match(['swarfer', 'threap', 'philosophistical', 'pushwainling'], p))
          [['swarfer'], ['philosophistical', 'pushwainling'], ['threap']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 3], [3, 3]]
          >>> fastest_words(match(['unilocularity', 'fumigant'], p))
          [['fumigant'], ['unilocularity']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 5, 3, 5, 2, 2], [1, 3, 2, 3, 5, 1], [2, 3, 5, 2, 4, 4]]
          >>> fastest_words(match(['stageably', 'rattlejack', 'corium', 'crumbable', 'coelialgia', 'agape'], p))
          [['coelialgia'], ['stageably', 'rattlejack', 'corium', 'agape'], ['crumbable']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 5], [3, 3], [3, 2]]
          >>> fastest_words(match(['boycottism', 'yo'], p))
          [[], ['boycottism'], ['yo']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 1, 5], [5, 2, 4]]
          >>> fastest_words(match(['spry', 'agrobiological', 'zaphara'], p))
          [['spry', 'agrobiological'], ['zaphara']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(match([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3], [5], [3]]
          >>> fastest_words(match(['durational'], p))
          [['durational'], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 2]]
          >>> fastest_words(match(['fungous', 'script'], p))
          [['fungous', 'script']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 4, 5], [1, 3, 4], [5, 5, 5]]
          >>> fastest_words(match(['immusical', 'azimine', 'commentarialism'], p))
          [[], ['immusical', 'azimine', 'commentarialism'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 2], [2, 5], [2, 3]]
          >>> fastest_words(match(['wettish', 'carthame'], p))
          [['carthame'], ['wettish'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 5, 2], [4, 2, 2]]
          >>> fastest_words(match(['stilted', 'sensorivascular', 'disadvantageously'], p))
          [['disadvantageously'], ['stilted', 'sensorivascular']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import match, fastest_words
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> test.swap_implementations(cats) # Make sure the abstraction barrier isn't crossed!
          >>> p0 = [2, 2, 3]
          >>> p1 = [6, 1, 2]
          >>> cats.fastest_words(cats.match(['What', 'great', 'luck'], [p0, p1]))
          [['What'], ['great', 'luck']]
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
