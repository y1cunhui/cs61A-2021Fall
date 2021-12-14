test = {
  'name': 'Problem 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> dogs = about(['dogs', 'hounds'])
          >>> dogs('A paragraph about cats.')
          False
          >>> dogs('A paragraph about dogs.')
          True
          >>> dogs('Release the Hounds!')
          True
          >>> dogs('"DOGS" stands for Department Of Geophysical Science.')
          True
          >>> dogs('Do gs and ho unds don\'t count')
          False
          >>> dogs("AdogsParagraph")
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
          >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
          'Cute Dog!'
          >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
          'Nice pup.'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import about
      >>> from cats import choose
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> ab = about(['neurine', 'statutably', 'quantivalent', 'intrarachidian', 'itinerantly', 'cloaklet'])
          >>> ab('unhollow simsim dcloakletB itinerantly cloakLet dQUaNtivalentJ gnEurinE fissiparity Mneurinel')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['unsimilar', 'conditioning', 'crystallogenical', 'mennom', 'foreannouncement', 'neomorph'])
          >>> ab('#crystallogenIcalW podded reorganizationist neomorPhf hneomorphj')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['newsstand', 'stereochromy', 'quinaldine', 'invalidate', 'japingly', 'clothesline'])
          >>> ab('stereochromy invalidate unewssTandq ste|reochromY/ Qstereochromy')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['unstatesmanlike', 'median', 'cueca', 'meroplankton', 'foremilk', 'nettlefish'])
          >>> ab('stickiness imprecatory bcuecan mcuec<a KMEroplanktonV gmedianY nettlefishs')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['lamellule', 'unibranchiate', 'introspectional', 'squamigerous', 'sair', 'heterodromy', 'butylene', 'gromatics', 'sprayfully'])
          >>> ab('answerer ksair JintrospectionaLm naphthosalol OsprayfuLly')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['gentlewomanly', 'titillating', 'counterquip', 'lotto', 'rejoicement', 'acouometer', 'wauns', 'comitatus', 'recidivous'])
          >>> ab('comitatu]s counterquip lanolin acouometer redawn laminose acou.omet%er dcomitatuS comitatus')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['musiclike', 'nonregarding', 'oxypropionic', 'postvide', 'muncheel', 'reburial', 'interfinger', 'masterman'])
          >>> ab('keratometer AnonReGardingY muNcheeLC proreduction ZoxyprOpionic musI_c|likeG RnoNr-egarding Nnonregardingj')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['antinoise', 'archcupbearer', 'opisthotonoid', 'nuggety'])
          >>> ab('rokey Farchcu$pbeare\\r furunculoid nonreactive uopisthotoNoid')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['sms', 'ultraplausible', 'clankety', 'tennisy'])
          >>> ab('continues uLt+raplausiblEk clankety bargeboard ultraplausible')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['crural', 'accredit', 'deltation', 'esophagomalacia', 'gramineal'])
          >>> ab("hebenon Ucr)ural s'acCr:editc precurtain aCcreDItj")
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['basiradial', 'pseudoliterary', 'electroextraction', 'polymorphous'])
          >>> ab('zbasiradial UPoLymorphousn captiousness basiradial |basIradial maddening po@L<ymorphoUs')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['unamenable', 'ratio', 'speciology', 'dimension', 'incenseless', 'fellside'])
          >>> ab('nincenseLess wspec"iolog@y cdimeNsi/onY Jd>imensionZ M,uNamena&blej vspeciologyx')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['interlardment', 'supercargo', 'inquilinity', 'mackenboy', 'trauma'])
          >>> ab('trAumA)T cleanable liquidation lesseeship traumag trauma perule tinamine interlardment')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['unintrigued'])
          >>> ab('preverify unintrigued irrationable uniNtriguedZ abscise uninebriating overblow buniNTrigue{d adulterize')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['purblindly', 'chromo', 'casson', 'unpliableness', 'overweeningly', 'unsquandered', 'educationable'])
          >>> ab('diapnotic chromod nectareous diffractive aeducationable DunpliablenEssa')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['strigal', 'scrawler', 'yarding'])
          >>> ab('Ostrigal trichology sTrIgal scRa?wLerV coeminency scrawler oscraWlerB oversqueak wscr>awler')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['pochay', 'negotiatrix', 'attaintment', 'concurringly', 'glyoxaline', 'terpin', 'kinetoscopic', 'chloralism', 'obvelation'])
          >>> ab('EkinetoscopiCH cOncurringlyL gcoNCurr:inglys DcOncurrIngL}]y pocha,ye')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['synizesis', 'marble', 'undeleted', 'subrogation', 'lownly', 'nebulosity', 'capricci', 'compelling', 'bluffer'])
          >>> ab('cherubically RMarBle synizesis genuflexuous bluffer PundelEteD')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['supercargoship', 'keelblock', 'celiosalpingectomy', 'pronumber', 'costotomy', 'radknight'])
          >>> ab('eceliosalpingEctomy su?percargO=shipF Ppronumb/(er pro[n]umberk AC@eliosalpingecToMyZ')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['campylometer', 'coalhole'])
          >>> ab('ocoa]lhol"eN desaurin RcamPyLome<ter labefact burghbote tenodesis')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['incendiarism', 'carbamide', 'families', 'subsequential'])
          >>> ab('pantotactic Wfamilies dincendiarism. ifamiliesd finceNdiari#]smV')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['kitling', 'workhouse', 'scriver', 'chilicothe', 'anteprandial', 'metosteon'])
          >>> ab("jkitlingM cortege Ochilicothe JwOrkh'ouse lchIl.icothee")
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['infanglement', 'cavern', 'autotriploid', 'brat'])
          >>> ab('paUtotriploidY deferrer parnas infanglement PbratD')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['plimsoll', 'hanse', 'endognath', 'cluck', 'zoosporiferous', 'stegosaurian', 'enhanced', 'microscopics', 'patibulate'])
          >>> ab('microscopics mhaNsef microscopiCs (st,egosaurian zoos)porI@ferousi')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['saponify', 'bakerless', 'nonluminous', 'zonesthesia', 'argumentatively', 'haikal'])
          >>> ab('kNonluminous vhaikalU mentohyoid anthropophagistic bha*ikalW')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['overfrailty', 'affair', 'gelatinizability', 'hygiene'])
          >>> ab('overfrailtY boverfrailty qaffa"ir/M hygiene gel,atiniZaBilitY overfraIlty#~ giganticidal moorup hygie%neD')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['toys', 'uranophane', 'whereso'])
          >>> ab('wher.E\'sOi sculpin uranophane santene matlockite uuRanophAne Wh"eres"ol')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['impercipient', 'ali', 'indult', 'palmitic', 'carbon'])
          >>> ab('phenylation carbon blossomed solemn palmitic carB/on impercipient Ppalmi?ticf jimpercIpIent;')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['rubberneck', 'telangiectasy', 'unratable', 'dissolvableness', 'redheadedly', 'recluse'])
          >>> ab('decurvature u.nratabl/eN YunRatable redheadedl@yo unRata.blem u{reclu^se Orec#lusea')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['nocturia', 'cataphyllum', 'alroot', 'unaffixed'])
          >>> ab("$(alroott daLroot phenosafranine ja'lroot<m mnocturiAd sternotribe")
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['undissenting', 'incorporable'])
          >>> ab('camstone mundisseNting mitotically in)cOrpOr>ableL gundIssenting fibromyositis inc+oRpOra.bleE')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['accresce', 'during', 'unreproachableness', 'incomputable', 'sulphosuccinic', 'nephrotomy'])
          >>> ab('convinced hnephroTomy accresce YUnreproacHablenEsS oaccresCe VDu_ring IunreproaChablenessu sulphosuccinic xunrepRoaChablenessA')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['unembraced', 'counterprotection', 'karyolysis', 'contuse', 'esophagomalacia', 'investigatorial'])
          >>> ab('unembraced i=nVesTigator<ial pcon#tu[sE demonstrator astrochemistry apotelesmatical')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['resay', 'benjy', 'ursolic'])
          >>> ab('resaY ursoli|c%F resay benjy ursolic overquiet ur,SOl`ict filate')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['meant', 'pantomime', 'fumatory', 'driftpiece', 'archaic', 'oreotragine', 'nystagmic', 'refute'])
          >>> ab('driftpiecE< drIftpiecef hor\\eotragIneC dr#iftpiEcej qar+chai{c Ldriftp<iece MeaNtP helianthic comburivorous')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['uncurl', 'lobulose', 'parapsychical', 'revengement', 'unappendaged'])
          >>> ab('paRapsycHicalU Xuncurlr revengement blobuloseH unappendagedz commemoratively IREvE,ngementG ZlObulose')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['lintwhite', 'colly'])
          >>> ab('cooking feedable colly microphotograph colly collyU')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['subcouncil', 'digestment', 'hierocratic', 'vasculated', 'purana', 'semipinacolic', 'gramophonically', 'preaffiliate'])
          >>> ab('litmus nastika Zd~igeStment PrEafFiliatez mgramOphOnicallyT charadrioid antipopular participiality')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['swearingly', 'pimple', 'unbundled', 'bencite', 'unfrustrably', 'thirteenth'])
          >>> ab('unbundled wb\\EnCiten lettsomite unfrustrably zunFrusTrably sweariNgly')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['undistinguishableness', 'squatwise', 'nonplastic', 'lucernal', 'holarctic', 'trinal'])
          >>> ab("nonplAst$icG pulpal holarctic (Ho{larcTicw HundisTinguishabl<enessp sprightfully dicodeine squatW@'iSec")
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['rhymemaking', 'nonassortment'])
          >>> ab('l rhymemaking detin finableness tallish')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['noumenalism'])
          >>> ab('thighed squaloid TnoumeNalism Fn`oumenal%ismE nouMenalIsMJ')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['moly', 'boldness', 'uraniid', 'inherently', 'diphenol', 'dermoskeleton', 'mound'])
          >>> ab('WdeRmosk^eleton inhere*ntLyP InheRentlyY nebuliferous SinhereNt~|Ly undervaluinglike NuraniidR vicecomes')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['parkward'])
          >>> ab('leatman threatfully xparkward>A nonulcerous casking albutannin ethnocracy untripe IparkW<ardC')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['probationism', 'pargeboard', 'liquidly', 'nongentile', 'metrification', 'unseamanship', 'despite'])
          >>> ab('YpargEboardn uNseama>nship unseamanshipt unbejuggled unseamanship Hunseamanshipv bparGeBoardf')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['purloiner', 'cinnabarine', 'orlop', 'ovolo', 'waistcoateer'])
          >>> ab('waistc;oateer cachaza ovarial cricothyreotomy orlopK')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['undersheriffship', 'remonetize', 'crustation', 'syntypicism', 'ne'])
          >>> ab('syntypicismG bne phenological capercut l@syntypi>cism')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['photomezzotype', 'durian', 'precompletion', 'handhold'])
          >>> ab('handhold hdurian phandhoLd unwoof lphotomezzotypeQ durian duriaNr recompress')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['bloodstroke', 'dioestrous', 'heterochthonous', 'supraseptal', 'heading', 'serpuline'])
          >>> ab('heteroCHtHonouS het[erochthonous$g unhazed gunj supraseptal RheteRochthonouSg')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['cyphella', 'actiniochrome', 'reassimilation', 'bandicoot', 'nettlefoot', 'macarism', 'usurp', 'thunderball'])
          >>> ab('Thunderball aThuNderbal{li usurp pulasan smacarismC')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['pemphigoid'])
          >>> ab("pemphigoid zpE=mph+igoid pemphigoid p'eMphigoi,dt disputatiousness root titulation")
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['haematosepsis', 'apomecometry', 'yrs', 'briefly', 'urinometric', 'discernible', 'zooparasite', 'noneviction', 'overmultitude'])
          >>> ab('discerNiblec uriNo\\metricO porpitoid fhaematosepSisn propaganda urIn?oMEtr$icZ QbrieFly settaine dis+cerniblem')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['lithosiid'])
          >>> ab("glitho'siId crumlet demoniacal comparatival pylangial standpatism lithosiid fewness")
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['uncomplimented', 'subside', 'pseudandry', 'saltcat', 'potting', 'anthoecological'])
          >>> ab('expatiatory msubside pseudaNdry saltcat subside gpSeudandryv octillionth uncomplimented T<poT+ting')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['coconscious', 'diploglossate', 'fatalistic', 'ow', 'disquietedness', 'manufactural'])
          >>> ab('plasmation XdisquietednessM ucocOnscious owm spryness Tma/nUfa+cturAlS weaverbird')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['dianilid', 'strack', 'whacky', 'stationery', 'shee', 'rebutter'])
          >>> ab("SsTra(c!k strack osteoporosis rstrackG ,strac'k shee Nrebut&tEr' smokelessly IsHee")
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['heavenish', 'dysmetria', 'cl', 'posthexaplaric', 'dinglebird', 'waistcoathole'])
          >>> ab('vwaIstcoathOle cl diminutal Ydinglebir|d received forger dinglebird Zhe-avenishm Ac~#LN')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['hectical', 'profanism', 'pachysalpingitis', 'overweather', 'polyfold', 'inpardonable', 'hypercivilization', 'chamberlainry'])
          >>> ab('profaniSmm hypercivilization w|hyperciviLizatioN inpardonable mhecticaLR mpr{o:fanismW profAnIsmc')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['scleranth', 'perdricide', 'renably', 'sorn', 'glutting', 'equalist'])
          >>> ab('Zrena_bl?y lgluttingx soRnu sorn gluttingY equal}istW')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['cardiectomy', 'mien', 'wellness', 'antitobacconist', 'zoosporangiophore', 'sarcogenous', 'davach'])
          >>> ab("TantitobacConisTC esarcogenous zo'oSporangiophoren cardiectomy absohm zooSporangioph&orE, gcArdiectOmyW qantitobaCconisTH")
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['unidealistic', 'pretermitter', 'automatist', 'nonactinic'])
          >>> ab('sunidEalis,tic nonactinic vnonactinic pRetermitteR summulist inonactinic cnonactinicD automatist')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['prefacer', 'parasynetic'])
          >>> ab("parAsyne^t(ic Parasynetick schoolgirlishness glucosamine pR'efacer patrice prefacer iprefaceR")
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['toxic', 'sphaeristerium'])
          >>> ab('lt#ox.icy pageless toxicc hydric mult')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['appositionally', 'earthly', 'orchiocatabasis', 'brangling'])
          >>> ab('NBr`angling+q prunetol fearthlyY honeymoonshine JeArthlyk')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['americium', 'polariscopy', 'malgovernment'])
          >>> ab('Jamerici_um pOlariscopY EaMeriCium^ subvassal polariscopy_ hoghide heavenly carrageenin malgOVerNment')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['brushed', 'removedness', 'peenge', 'equid', 'saltcatch'])
          >>> ab('overmellowness appledrane removednessu wsalTC]at_chU foliar')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['humicubation', 'hyperdulic', 'crimple', 'soother', 'overkind'])
          >>> ab('oxidational nonelectrical hypostomial overkind qh#ypErDulick')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['parapsidal', 'unattendance', 'expirable', 'wheelwright', 'rind', 'spermalist'])
          >>> ab('unparallelness palatal orbitofrontal expirableb monospermal')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['oliguresis', 'plethoretical', 'plantlike', 'electrotechnology', 'superioress'])
          >>> ab('superioress revalorize Nplant-Like plet-h&oretical oliguresis eOliguresis plethoretical electrotechnology')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['hubber', 'patrology', 'spermatophore', 'sapping'])
          >>> ab('utterance phyma OhUbber$.J console usPermaTophore thysanourous hu}bber gs^permatophore')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['miskindle', 'deathbed', 'gangrenous'])
          >>> ab('craniometer yes kdEathbedH AmIskindlE?a }misk;indleT unbetray characters ZdeathbEd divertedly')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['nummi', 'undisparaged', 'polarly', 'baldachino', 'strumae', 'posttoxic', 'cavernous'])
          >>> ab('equalist circumcentral unDIsparaGed perfumy strumaee strumae polygyn opolaRly')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['wraprascal', 'renominate', 'quondam', 'gullibility', 'staysail', 'unfleshly', 'styca'])
          >>> ab('AuNflesHlyQ wrapRascalT unfle%shlyH womenkind cre@nominaTe')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['unprincipal', 'myrmicoid', 'nonofficial', 'prinky', 'metaphony', 'subacromial', 'mycetophilid', 'chemolyze'])
          >>> ab('myrmicoiDV p:un.principal goosemouth rnonofficialB jingal rejerk')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['empaistic', 'fibrinate', 'pillarlet', 'widdendream', 'underbuy', 'mopla', 'footplate', 'traveleress', 'gemmiparously'])
          >>> ab('traveleress [Und!ErbuyQ fibri+-nateM footplatE heezy WidDeNdreAmI empaist~icl zGemmipaRouSly')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['impanate', 'undisinfected', 'unnapkined', 'stockwright', 'nonconcern', 'clandestineness', 'calcicolous'])
          >>> ab('fImpanaTEd unnapkinedL Xim_"panate hypometropia gunnapkined')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['horrorsome', 'gastroblennorrhea', 'pouringly', 'procreatrix', 'demipriest'])
          >>> ab('dittology HgastroblennorRhe:aA p)rocreat%rixF fproc[reatriXF horsekeeper altiloquent pprocreatriX!u')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['baku', 'uncontentedness', 'teacher', 'upwrought', 'planetography', 'phenanthroline', 'apism', 'thwarteous', 'melodrame'])
          >>> ab('upwroUghtJ uncontentedness Rba>kut zt~eac:her vplanetoGraphym xmelodramel')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['unstoried', 'funeralize'])
          >>> ab('ineloquence revegetation OunstorIed nonomad spinulosociliate stercorary preimbue falbala multilobed')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['freedom', 'transmutationist', 'tomblet', 'wapp', 'matrix', 'pitfall', 'bardel', 'shieldlessness'])
          >>> ab('amianthiform >pitfa[ll wappa freedom shieldlessnessF')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['angiocholecystitis', 'yoven', 'lovably', 'sheepmonger', 'molave', 'hate'])
          >>> ab('grassworm sheepmonger psychagogos muckerism molave Mh`a}te')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['chaetophoraceous', 'virify', 'ferrohydrocyanic', 'wambly', 'hydrotechnic', 'capillose', 'unfaultfinding', 'monstricide'])
          >>> ab('Wvirif*yc Tunfaultf>indin,gK Qchaetophoraceousn hydRotechnic capillOsee OwamblyK')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['lactase', 'pleionian', 'guige', 'tellureted', 'magistratically', 'playwrightry', 'paradoxicalness'])
          >>> ab('ymAgistra,tically playwright+R+yk plEionI=#an guige tellureted teleutospore Wguige')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['overstalled', 'obstupefy', 'predeparture', 'craft'])
          >>> ab('craft ob-s|tupefy predeparture crafT C:ra"ftf hypodorian W&crA*ft YPredepar,tureV')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['operated', 'cithara', 'apparent', 'natron'])
          >>> ab('ocithArAz skilfish uninthroned o/peraTedD natron operated')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['translocate', 'contradictive', 'beseem'])
          >>> ab('Ktranslocate beseemR KBes:eemr conjugative beseemX')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['agamid', 'septenar'])
          >>> ab('pyromancer chilostome heliocentricity septenarv agamid dentists')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['subscience'])
          >>> ab('unpleasable copperplate preindependently offtake propugnaculum oysterous floe phyllosoma Ssubsciencew')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['optotype', 'raise', 'placentitis', 'virtualism', 'dirigibility'])
          >>> ab('dirigibility optotype kraise"z Sd|irigibilityv ar-aiseN Nopto.^typeP virt\\ualism dirigib]ilityW halogenation')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['clanjamphrey', 'belord', 'vermeology', 'wrive', 'phellodermal', 'weaponry', 'intrajugular'])
          >>> ab('NweaPOnrY belord$)v wrive noncontroversial fbelOrdj Phe?lloderMal wr-ivel vermeology Wri[~ve')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['louseberry', 'catercorner', 'pelecan', 'impermanency', 'differentiate', 'trifold', 'snakewood', 'ichneumonid', 'acrophony'])
          >>> ab('LtrifOldW DifferentiAte<h bournless amphioxus QDifferentiate(@y dpeLeCaNr')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['disensure', 'flashing', 'swarfer', 'threap'])
          >>> ab('Fd(isenSu[rer sarcocyst spermatozoal flashingJ threap flashinG')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['unilocularity', 'fumigant', 'retaker'])
          >>> ab('fagine f>umigantS retakerI reta|ker%Q guardian fumIgantY oology hypothetist OuniLocular#i#tyx')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['coast', 'stageably', 'rattlejack'])
          >>> ab('insupportably coast velvetwork unwastable cOAst co+astm suprachoroidal impressiveness')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['yo', 'tympanism', 'untrigonometrical', 'unurging'])
          >>> ab('centriscid Hyo TU"nurgin<gp tympanism uNtrigonometriCalh suNur-gin<gu')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['gormed', 'spry', 'agrobiological', 'zaphara', 'unlessoned', 'nuclidic'])
          >>> ab('Sagr#obiological[d gnuclidi!c disaccustomed ureteroradiography Kg|~ormedO')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['ten', 'kittendom', 'supercatastrophe'])
          >>> ab('valueless consumptional untreasured wsUperc,atAstrOpheR Gte^n telekinetic Rsupe+rcatastrophe At$:Eng')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['exhibitions', 'durational', 'templarlikeness', 'boghole', 'tersulphate', 'slubby', 'lovesickness'])
          >>> ab("duraTiOnalu Vtempla^/rlikenessG mesoscutellum YlovEsick\\ne'ssy Tslub(by(m t;bogholE~L")
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['blackishly', 'fungous', 'script', 'rais', 'cleeked'])
          >>> ab('script Sfungo@u#s fcleeKEd fun_gous c#lEEk^edw Mcle#eK[eD tinampipi')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['immusical', 'azimine', 'commentarialism', 'compelling'])
          >>> ab('mcommeNtarialism merwoman crushed tcomment"aRialism strongyloid azimi(n:eG')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['carthame', 'ermelin', 'ungravelly', 'antilegomena', 'dichroitic'])
          >>> ab('diChroitic mutsuddy unmissionary antilegomena ermelin')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['autometric', 'stilted'])
          >>> ab('BAutomet%ricJ MaUtOm`etric perissosyllabic Dauto%metr"icF esterellite aut}ometricF')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import about
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
