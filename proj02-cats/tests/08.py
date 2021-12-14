test = {
  'name': 'Problem 8',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> typed = ['I', 'have', 'begun']
          >>> prompt = ['I', 'have', 'begun', 'to', 'type']
          >>> print_progress({'id': 1, 'progress': 0.6})
          ID: 1 Progress: 0.6
          >>> report_progress(typed, prompt, 1, print_progress) # print_progress is called on the report
          ID: 1 Progress: 0.6
          0.6
          >>> report_progress(['I', 'begun'], prompt, 2, print_progress)
          ID: 2 Progress: 0.2
          0.2
          >>> report_progress(['I', 'hve', 'begun', 'to', 'type'], prompt, 3, print_progress)
          ID: 3 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
          >>> # The above function displays progress in the format ID: __, Progress: __
          >>> print_progress({'id': 1, 'progress': 0.6})
          ID: 1 Progress: 0.6
          >>> typed = ['how', 'are', 'you']
          >>> prompt = ['how', 'are', 'you', 'doing', 'today']
          >>> report_progress(typed, prompt, 2, print_progress)
          ID: 2 Progress: 0.6
          0.6
          >>> report_progress(['how', 'aree'], prompt, 3, print_progress)
          ID: 3 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['newsstand'], ['newsstand', 'stereochromy', 'quinaldine', 'invalidate', 'japingly'], 21, print_progress)
          ID: 21 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['unstatesmanlike', 'median', 'cueca', 'meroplankton', 'foremilk'], 16, print_progress)
          ID: 16 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['lamellule', 'unibranchiate', 'introspectional', 'squamigerous', 'sair', 'heterodromy', 'butylene'], ['lamellule', 'unibranchiate', 'introspectional', 'squamigerous', 'sair', 'heterodromy', 'butylene', 'gromatics'], 37, print_progress)
          ID: 37 Progress: 0.875
          0.875
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['gentlewomanly'], ['gentlewomanly', 'titillating', 'counterquip', 'lotto', 'rejoicement', 'acouometer', 'wauns', 'comitatus'], 10, print_progress)
          ID: 10 Progress: 0.125
          0.125
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['musiclike', 'nonregarding'], ['musiclike', 'nonregarding', 'oxypropionic', 'postvide', 'muncheel', 'reburial', 'interfinger'], 36, print_progress)
          ID: 36 Progress: 0.2857142857142857
          0.2857142857142857
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['baNtinOise', 'archcupbearer'], ['antinoise', 'archcupbearer', 'opisthotonoid'], 9, print_progress)
          ID: 9 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['zsM_s', 'ult*raPlauS`ible'], ['sms', 'ultraplausible', 'clankety'], 77, print_progress)
          ID: 77 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['crural', 'accredit', 'deltation'], ['crural', 'accredit', 'deltation', 'esophagomalacia'], 19, print_progress)
          ID: 19 Progress: 0.75
          0.75
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['basiradial', 'pseudoliterary', 'electroextraction'], 83, print_progress)
          ID: 83 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['unamenable'], ['unamenable', 'ratio', 'speciology', 'dimension', 'incenseless'], 59, print_progress)
          ID: 59 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['interlardment', 'supercargo', 'inquilinity', 'mackenboy'], 89, print_progress)
          ID: 89 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['unintrigued'], 81, print_progress)
          ID: 81 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['purblindly', 'chromo', 'casson', 'unpliableness', 'overweeningly', 'unsquandered'], 22, print_progress)
          ID: 22 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['strigal', 'scrawler'], 25, print_progress)
          ID: 25 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['pochay', 'negotiatrix', 'attaintment', 'concurringly', 'glyoxaline', 'terpin', 'kinetoscopic', 'chloralism'], 26, print_progress)
          ID: 26 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['synizesis', 'gmarbleI', 'undeleted'], ['synizesis', 'marble', 'undeleted', 'subrogation', 'lownly', 'nebulosity', 'capricci', 'compelling'], 96, print_progress)
          ID: 96 Progress: 0.125
          0.125
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['supercargoship', 'keelblock', 'vceliosalPingEcTOmyU', 'pronumber'], ['supercargoship', 'keelblock', 'celiosalpingectomy', 'pronumber', 'costotomy'], 57, print_progress)
          ID: 57 Progress: 0.4
          0.4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['campylometer'], 6, print_progress)
          ID: 6 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['incendiarism'], ['incendiarism', 'carbamide', 'families'], 66, print_progress)
          ID: 66 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['Ckitlingx', 'workhouse'], ['kitling', 'workhouse', 'scriver', 'chilicothe', 'anteprandial'], 68, print_progress)
          ID: 68 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['infanglement', 'cavern', 'autotriploid'], 90, print_progress)
          ID: 90 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['plimsoll', 'hanse', 'endognath', 'cluck', 'zoosporiferous', 'stegosaurian', 'enhanced', 'microscopics'], 63, print_progress)
          ID: 63 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['saponify', 'bakerless', 'nonluminous', 'zoNEsthesIal'], ['saponify', 'bakerless', 'nonluminous', 'zonesthesia', 'argumentatively'], 9, print_progress)
          ID: 9 Progress: 0.6
          0.6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['overfrailty', 'affair', 'gelatinizability'], 31, print_progress)
          ID: 31 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['toys'], ['toys', 'uranophane'], 17, print_progress)
          ID: 17 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['impercipient', 'ali'], ['impercipient', 'ali', 'indult', 'palmitic'], 8, print_progress)
          ID: 8 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['rubberneck', 'telangiectasy'], ['rubberneck', 'telangiectasy', 'unratable', 'dissolvableness', 'redheadedly'], 45, print_progress)
          ID: 45 Progress: 0.4
          0.4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['nocturia', 'cataphyllum', 'alroot'], 37, print_progress)
          ID: 37 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['undissenting'], 5, print_progress)
          ID: 5 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['accresce', '&during', 'unreproachableness'], ['accresce', 'during', 'unreproachableness', 'incomputable', 'sulphosuccinic'], 11, print_progress)
          ID: 11 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['unembraced', 'counterprotection'], ['unembraced', 'counterprotection', 'karyolysis', 'contuse', 'esophagomalacia'], 46, print_progress)
          ID: 46 Progress: 0.4
          0.4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['resay', 'benjy'], 23, print_progress)
          ID: 23 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['meant', 'pantomime', 'fumatory', 'driftpiece'], ['meant', 'pantomime', 'fumatory', 'driftpiece', 'archaic', 'oreotragine', 'nystagmic'], 4, print_progress)
          ID: 4 Progress: 0.5714285714285714
          0.5714285714285714
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['uncurl'], ['uncurl', 'lobulose', 'parapsychical', 'revengement'], 61, print_progress)
          ID: 61 Progress: 0.25
          0.25
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['lintwhite'], 85, print_progress)
          ID: 85 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['subcouncil', 'digestment', 'hierocratic'], ['subcouncil', 'digestment', 'hierocratic', 'vasculated', 'purana', 'semipinacolic', 'gramophonically'], 91, print_progress)
          ID: 91 Progress: 0.42857142857142855
          0.42857142857142855
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['ysw(eAringly', 'pimple', 'unbundled', 'bencite'], ['swearingly', 'pimple', 'unbundled', 'bencite', 'unfrustrably'], 74, print_progress)
          ID: 74 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['undistinguishableness', 'squatwise', 'nonplastic', 'lucernal', 'holarctic'], 87, print_progress)
          ID: 87 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['rhymemaking'], 53, print_progress)
          ID: 53 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['noumenalism'], 70, print_progress)
          ID: 70 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['moly'], ['moly', 'boldness', 'uraniid', 'inherently', 'diphenol', 'dermoskeleton'], 71, print_progress)
          ID: 71 Progress: 0.16666666666666666
          0.16666666666666666
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['parkward'], 12, print_progress)
          ID: 12 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['probationism'], ['probationism', 'pargeboard', 'liquidly', 'nongentile', 'metrification', 'unseamanship'], 86, print_progress)
          ID: 86 Progress: 0.16666666666666666
          0.16666666666666666
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['purloiner', 'cinnabarine', 'orlop', 'ovolo'], 51, print_progress)
          ID: 51 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['undersheriffship', 'remonetize', 'crustation', 'syntypicism'], 84, print_progress)
          ID: 84 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['photomezzotype'], ['photomezzotype', 'durian', 'precompletion'], 68, print_progress)
          ID: 68 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['bloodstroke', 'dioestrous', 'Xheterochthonousq'], ['bloodstroke', 'dioestrous', 'heterochthonous', 'supraseptal', 'heading'], 30, print_progress)
          ID: 30 Progress: 0.4
          0.4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['cyphella', 'actiniochrome', 'reassimilation', 'bandicoot', 'nettlefoot'], ['cyphella', 'actiniochrome', 'reassimilation', 'bandicoot', 'nettlefoot', 'macarism', 'usurp'], 65, print_progress)
          ID: 65 Progress: 0.7142857142857143
          0.7142857142857143
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['pemphigoid'], 81, print_progress)
          ID: 81 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['haematosepsis'], ['haematosepsis', 'apomecometry', 'yrs', 'briefly', 'urinometric', 'discernible', 'zooparasite', 'noneviction'], 36, print_progress)
          ID: 36 Progress: 0.125
          0.125
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['lithosiid'], 11, print_progress)
          ID: 11 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['uncomplimented', 'subside', 'pseudandry', 'saltcat'], ['uncomplimented', 'subside', 'pseudandry', 'saltcat', 'potting'], 84, print_progress)
          ID: 84 Progress: 0.8
          0.8
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['coconscious', 'diploglossate', 'fatalistic', 'ow', 'disquietedness'], 69, print_progress)
          ID: 69 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['dianilid', 'strack', 'whacky', 'stationery', 'shee'], 88, print_progress)
          ID: 88 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['heavenish'], ['heavenish', 'dysmetria', 'cl', 'posthexaplaric', 'dinglebird'], 6, print_progress)
          ID: 6 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['hectical', 'profanism', 'pachysalpingitis', 'overweather', 'polyfold', 'inpardonable', 'hypercivilization'], 35, print_progress)
          ID: 35 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['scleranth'], ['scleranth', 'perdricide', 'renably', 'sorn', 'glutting'], 87, print_progress)
          ID: 87 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['cardiectomy'], ['cardiectomy', 'mien', 'wellness', 'antitobacconist', 'zoosporangiophore', 'sarcogenous'], 37, print_progress)
          ID: 37 Progress: 0.16666666666666666
          0.16666666666666666
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['unidealistic', 'pretermitter'], ['unidealistic', 'pretermitter', 'automatist'], 25, print_progress)
          ID: 25 Progress: 0.6666666666666666
          0.6666666666666666
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['prefacer'], 23, print_progress)
          ID: 23 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['toxic'], 99, print_progress)
          ID: 99 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['appositionally', 'earthly'], ['appositionally', 'earthly', 'orchiocatabasis'], 42, print_progress)
          ID: 42 Progress: 0.6666666666666666
          0.6666666666666666
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['americium'], ['americium', 'polariscopy'], 11, print_progress)
          ID: 11 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['obr(u&shed'], ['brushed', 'removedness', 'peenge', 'equid'], 60, print_progress)
          ID: 60 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['humicubation', 'hyperdulic', 'crimple', 'soother'], 51, print_progress)
          ID: 51 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['parapsidalX'], ['parapsidal', 'unattendance', 'expirable', 'wheelwright', 'rind'], 75, print_progress)
          ID: 75 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['oliguresis'], ['oliguresis', 'plethoretical', 'plantlike', 'electrotechnology'], 21, print_progress)
          ID: 21 Progress: 0.25
          0.25
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['hubber'], ['hubber', 'patrology', 'spermatophore'], 91, print_progress)
          ID: 91 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['miskindle', 'deathbed'], 28, print_progress)
          ID: 28 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['nummi'], ['nummi', 'undisparaged', 'polarly', 'baldachino', 'strumae', 'posttoxic'], 80, print_progress)
          ID: 80 Progress: 0.16666666666666666
          0.16666666666666666
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['wraprascal', 'renominate', 'quondam', 'gullibility', 'staysail'], ['wraprascal', 'renominate', 'quondam', 'gullibility', 'staysail', 'unfleshly'], 1, print_progress)
          ID: 1 Progress: 0.8333333333333334
          0.8333333333333334
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['unprincipal'], ['unprincipal', 'myrmicoid', 'nonofficial', 'prinky', 'metaphony', 'subacromial', 'mycetophilid'], 9, print_progress)
          ID: 9 Progress: 0.14285714285714285
          0.14285714285714285
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['empaistic', 'fibrinate', 'pillarlet', 'widdendream', 'underbuy', 'mopla', 'footplate'], ['empaistic', 'fibrinate', 'pillarlet', 'widdendream', 'underbuy', 'mopla', 'footplate', 'traveleress'], 34, print_progress)
          ID: 34 Progress: 0.875
          0.875
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['impanate', 'undisinfected'], ['impanate', 'undisinfected', 'unnapkined', 'stockwright', 'nonconcern', 'clandestineness'], 53, print_progress)
          ID: 53 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['horrorsOme\\P', 'gastroblennorrhea', 'LpoUriN|glyx'], ['horrorsome', 'gastroblennorrhea', 'pouringly', 'procreatrix'], 66, print_progress)
          ID: 66 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['baku', 'uncontentedness', 'teacher', 'upwrought', 'planetography', 'phenanthroline', 'apism', 'thwarteous'], 71, print_progress)
          ID: 71 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['unstoried'], 7, print_progress)
          ID: 7 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['freedom', 'transmutationist', 'tomblet', 'wapp', 'matrix', 'pitfall', 'bardel'], 57, print_progress)
          ID: 57 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['angiocholecystitis', 'yoven', 'lovably', 'sheepmonger'], ['angiocholecystitis', 'yoven', 'lovably', 'sheepmonger', 'molave'], 20, print_progress)
          ID: 20 Progress: 0.8
          0.8
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['chaetophoraceous'], ['chaetophoraceous', 'virify', 'ferrohydrocyanic', 'wambly', 'hydrotechnic', 'capillose', 'unfaultfinding'], 87, print_progress)
          ID: 87 Progress: 0.14285714285714285
          0.14285714285714285
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['lactase', 'pleionian', 'guige'], ['lactase', 'pleionian', 'guige', 'tellureted', 'magistratically', 'playwrightry'], 64, print_progress)
          ID: 64 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['overstalled'], ['overstalled', 'obstupefy', 'predeparture'], 42, print_progress)
          ID: 42 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['operated', 'citHara'], ['operated', 'cithara', 'apparent'], 70, print_progress)
          ID: 70 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['translocate'], ['translocate', 'contradictive'], 40, print_progress)
          ID: 40 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['agamid'], 56, print_progress)
          ID: 56 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['subscience'], 68, print_progress)
          ID: 68 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['optotype', 'raise', 'placentitis', 'virtualism'], 9, print_progress)
          ID: 9 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['clanjamphrey', 'belord', 'vermeology', 'wrive', 'phellodermal', 'weaponry'], 9, print_progress)
          ID: 9 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['louseberry', 'catercorner', 'Epelecann', 'impermanency', 'differ[entiate$'], ['louseberry', 'catercorner', 'pelecan', 'impermanency', 'differentiate', 'trifold', 'snakewood', 'ichneumonid'], 6, print_progress)
          ID: 6 Progress: 0.25
          0.25
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['disensure', 'flashing'], ['disensure', 'flashing', 'swarfer'], 8, print_progress)
          ID: 8 Progress: 0.6666666666666666
          0.6666666666666666
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['unilocularity'], ['unilocularity', 'fumigant'], 58, print_progress)
          ID: 58 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['coast', 'stageably'], 93, print_progress)
          ID: 93 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['yo', 'tympanism', 'untrigonometrical'], 58, print_progress)
          ID: 58 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['gormed', 'spry', 'agrobiological', 'zaphara', 'unlessoned'], 77, print_progress)
          ID: 77 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['ten'], ['ten', 'kittendom'], 22, print_progress)
          ID: 22 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['exhibitions', 'durational'], ['exhibitions', 'durational', 'templarlikeness', 'boghole', 'tersulphate', 'slubby'], 7, print_progress)
          ID: 7 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['blackishly'], ['blackishly', 'fungous', 'script', 'rais'], 66, print_progress)
          ID: 66 Progress: 0.25
          0.25
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['immusical', 'azimine', 'commentarialism'], 51, print_progress)
          ID: 51 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['carthame', 'ermelin', 'ungravelly', 'antilegomena'], 71, print_progress)
          ID: 71 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['autometric'], 57, print_progress)
          ID: 57 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import report_progress
      >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
