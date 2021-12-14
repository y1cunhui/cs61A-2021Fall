test = {
  'name': 'Problem 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> wpm("12345", 3) # Note: wpm returns a float (with a decimal point)
          20.0
          >>> wpm("a b c", 20)
          3.0
          >>> wpm("", 10)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> wpm('hello friend hello buddy hello', 15)
          24.0
          >>> wpm('0123456789',60)
          2.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> wpm("a  b  c  d", 5)
          24.0
          >>> wpm("a b c", 120)
          0.5
          >>> wpm("abc", 1)
          36.0
          >>> wpm(" a b \tc" , 1)
          84.0
          >>> wpm("", 10)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> reference_text = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art."
          >>> typed_string1 = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art."
          >>> typed_string2 = "Abstraction, in general, is a fundamentl concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction usd in other fields such as art."
          >>> typed_string3 = "Abstraction,"
          >>> typed_string4 = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art. extra"
          >>> typed_string5 = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art. Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art. art"
          >>> typed_string6 = "abstraction"
          >>> round(wpm(typed_string1, 67), 1)
          99.2
          >>> round(wpm(typed_string2, 67), 1)
          98.9
          >>> round(wpm(typed_string3, 67), 1)
          2.1
          >>> round(wpm(typed_string4, 67), 1)
          100.3
          >>> round(wpm(typed_string5, 67), 1)
          199.3
          >>> round(wpm(typed_string6, 1), 1)
          132.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('newsstand stereochromy quinaldine invalidate japingly', 18.95), 2)
          33.56
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('unstatesmanlike median cueca meroplankton foremilk', 3.15), 2)
          190.48
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('lamellule unibranchiate introspectional squamigerous sair heterodromy butylene gromatics', 11.27), 2)
          93.7
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('gentlewomanly titillating counterquip lotto rejoicement acouometer wauns comitatus', 2.58), 2)
          381.4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('musiclike nonregarding oxypropionic postvide muncheel reburial interfinger', 5.67), 2)
          156.61
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('antinoise archcupbearer opisthotonoid', 5.27), 2)
          84.25
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('cixiid sms ultraplausible clankety tennisy hybridist turrical pillarlike dumb', 18.54), 2)
          49.84
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('crural accredit deltation esophagomalacia', 21.76), 2)
          22.61
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('basiradial pseudoliterary electroextraction', 29.18), 2)
          17.68
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('unamenable ratio speciology dimension incenseless', 1.02), 2)
          576.47
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('interlardment supercargo inquilinity mackenboy trauma polyemia centuplication anthracoid megalomelia', 4.92), 2)
          243.9
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('casual artist unintrigued janitor lenard helminthagogue disfigurative runrig crutch', 24.56), 2)
          40.55
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('purblindly chromo casson unpliableness overweeningly unsquandered', 13.28), 2)
          58.73
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('strigal scrawler', 94.27), 2)
          2.04
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('pochay negotiatrix attaintment concurringly glyoxaline terpin kinetoscopic chloralism', 27.33), 2)
          37.32
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('synizesis marble undeleted subrogation lownly nebulosity capricci compelling', 86.87), 2)
          10.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('pectous kathal supercargoship keelblock celiosalpingectomy pronumber costotomy radknight autodetector', 43.75), 2)
          27.7
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('campylometer', 72.27), 2)
          1.99
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('incendiarism carbamide families', 6.98), 2)
          53.3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('kitling workhouse scriver chilicothe anteprandial', 11.99), 2)
          49.04
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('infanglement cavern autotriploid', 80.48), 2)
          4.77
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('fiddley ungifted plimsoll hanse endognath cluck zoosporiferous stegosaurian enhanced', 10.14), 2)
          99.41
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('saponify bakerless nonluminous zonesthesia argumentatively', 3.93), 2)
          177.1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('overfrailty affair gelatinizability', 62.1), 2)
          6.76
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('toys uranophane', 1.28), 2)
          140.62
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('impercipient ali indult palmitic', 1.98), 2)
          193.94
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('rubberneck telangiectasy unratable dissolvableness redheadedly', 1.99), 2)
          373.87
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('nocturia cataphyllum alroot', 55.08), 2)
          5.88
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('undissenting', 32.5), 2)
          4.43
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('accresce during unreproachableness incomputable sulphosuccinic', 30.41), 2)
          24.47
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('unembraced counterprotection karyolysis contuse esophagomalacia', 42.35), 2)
          17.85
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('resay benjy', 60.34), 2)
          2.19
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('meant pantomime fumatory driftpiece archaic oreotragine nystagmic', 55.27), 2)
          14.11
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('uncurl lobulose parapsychical revengement', 7.78), 2)
          63.24
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('lintwhite', 61.86), 2)
          1.75
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('myristicaceous clodpated subcouncil digestment hierocratic vasculated purana semipinacolic gramophonically', 27.71), 2)
          45.9
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('swearingly pimple unbundled bencite unfrustrably', 1.83), 2)
          314.75
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('undistinguishableness squatwise nonplastic lucernal holarctic', 1.45), 2)
          504.83
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('rhymemaking', 74.91), 2)
          1.76
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('uninterlocked scrotectomy noumenalism botryomycoma sphingometer sensibilize deconsecration impersonatrix sheer', 17.82), 2)
          74.07
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('moly boldness uraniid inherently diphenol dermoskeleton', 3.1), 2)
          212.9
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('', 47.32), 2)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('probationism pargeboard liquidly nongentile metrification unseamanship', 3.43), 2)
          244.9
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('purloiner cinnabarine orlop ovolo', 6.79), 2)
          58.32
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('undersheriffship remonetize crustation syntypicism', 14.0), 2)
          42.86
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('photomezzotype durian precompletion', 1.6), 2)
          262.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('bloodstroke dioestrous heterochthonous supraseptal heading', 5.2), 2)
          133.85
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('cyphella actiniochrome reassimilation bandicoot nettlefoot macarism usurp', 64.94), 2)
          13.49
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('', 19.19), 2)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('haematosepsis apomecometry yrs briefly urinometric discernible zooparasite noneviction', 30.92), 2)
          33.38
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('', 2.67), 2)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('prophasis uncomplimented subside pseudandry saltcat potting anthoecological autoecy femininely', 69.26), 2)
          16.29
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('coconscious diploglossate fatalistic ow disquietedness', 69.53), 2)
          9.32
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('thunderousness carbomethoxyl dianilid strack whacky stationery shee rebutter yellows', 29.7), 2)
          33.94
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('heavenish dysmetria cl posthexaplaric dinglebird', 1.01), 2)
          570.3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('hectical profanism pachysalpingitis overweather polyfold inpardonable hypercivilization', 10.71), 2)
          97.48
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('scleranth perdricide renably sorn glutting', 13.56), 2)
          37.17
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('cardiectomy mien wellness antitobacconist zoosporangiophore sarcogenous', 66.0), 2)
          12.91
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('unidealistic pretermitter automatist', 25.61), 2)
          16.87
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('prefacer', 41.63), 2)
          2.31
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('toxic', 40.9), 2)
          1.47
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('appositionally earthly orchiocatabasis', 77.97), 2)
          5.85
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('americium polariscopy', 22.8), 2)
          11.05
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('brushed removedness peenge equid', 28.63), 2)
          13.41
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('humicubation hyperdulic crimple soother', 21.24), 2)
          22.03
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('parapsidal unattendance expirable wheelwright rind', 18.64), 2)
          32.19
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('oliguresis plethoretical plantlike electrotechnology', 7.19), 2)
          86.79
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('hubber patrology spermatophore', 39.57), 2)
          9.1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('miskindle deathbed', 34.88), 2)
          6.19
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('nummi undisparaged polarly baldachino strumae posttoxic', 32.51), 2)
          20.3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('wraprascal renominate quondam gullibility staysail unfleshly', 3.19), 2)
          225.71
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('unprincipal myrmicoid nonofficial prinky metaphony subacromial mycetophilid', 53.22), 2)
          16.91
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('empaistic fibrinate pillarlet widdendream underbuy mopla footplate traveleress', 35.56), 2)
          26.32
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('impanate undisinfected unnapkined stockwright nonconcern clandestineness', 25.3), 2)
          34.15
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('toothy achromatism uintathere horrorsome gastroblennorrhea pouringly procreatrix demipriest accommodations', 51.48), 2)
          24.71
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('baku uncontentedness teacher upwrought planetography phenanthroline apism thwarteous', 30.62), 2)
          32.92
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('unstoried', 68.07), 2)
          1.59
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('freedom transmutationist tomblet wapp matrix pitfall bardel', 1.76), 2)
          402.27
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('angiocholecystitis yoven lovably sheepmonger molave', 58.85), 2)
          10.4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('chaetophoraceous virify ferrohydrocyanic wambly hydrotechnic capillose unfaultfinding', 68.29), 2)
          14.94
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('lactase pleionian guige tellureted magistratically playwrightry', 47.94), 2)
          15.77
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('overstalled obstupefy predeparture', 88.07), 2)
          4.63
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('operated cithara apparent', 61.53), 2)
          4.88
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('translocate contradictive', 70.62), 2)
          4.25
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('agamid', 23.9), 2)
          3.01
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('', 26.9), 2)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('optotype raise placentitis virtualism', 2.27), 2)
          195.59
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('clanjamphrey belord vermeology wrive phellodermal weaponry', 6.8), 2)
          102.35
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('louseberry catercorner pelecan impermanency differentiate trifold snakewood ichneumonid', 52.02), 2)
          20.07
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('disensure flashing swarfer', 7.66), 2)
          40.73
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('unilocularity fumigant', 10.6), 2)
          24.91
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('coast stageably', 23.86), 2)
          7.54
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('yo tympanism untrigonometrical', 1.01), 2)
          356.44
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('gormed spry agrobiological zaphara unlessoned', 93.55), 2)
          5.77
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('ten kittendom', 48.59), 2)
          3.21
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('exhibitions durational templarlikeness boghole tersulphate slubby', 29.41), 2)
          26.52
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('blackishly fungous script rais', 1.07), 2)
          336.45
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('immusical azimine commentarialism', 2.55), 2)
          155.29
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('carthame ermelin ungravelly antilegomena', 60.78), 2)
          7.9
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('autometric', 24.82), 2)
          4.83
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import wpm
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
