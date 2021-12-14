test = {
  'name': 'Problem 3',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> accuracy("12345", "12345") # This should return 100.0 (not the integer 100!)
          100.0
          >>> accuracy("a b c", "a b c")
          100.0
          >>> accuracy("a  b  c  d", "b  a  c  d")
          50.0
          >>> accuracy("a b", "c d e")
          0.0
          >>> accuracy("Cat", "cat") # the function is case-sensitive
          0.0
          >>> accuracy("a b c d", "a d")
          25.0
          >>> accuracy("abc", " ")
          0.0
          >>> accuracy("a b \tc" , "a b c") # Tabs don't count as words
          100.0
          >>> accuracy("abc", "")
          0.0
          >>> accuracy("", "abc")
          0.0
          >>> accuracy("a b c d", "b c d")
          0.0
          >>> accuracy("cats.", "cats") # punctuation counts
          0.0
          >>> accuracy("", "") # Returns 100.0
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> accuracy('Cute Dog!', 'Cute Dog.')
          50.0
          >>> accuracy('A Cute Dog!', 'Cute Dog.')
          0.0
          >>> accuracy('cute Dog.', 'Cute Dog.')
          50.0
          >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
          50.0
          >>> accuracy('Cute', 'Cute Dog.')
          100.0
          >>> accuracy('', 'Cute Dog.')
          0.0
          >>> accuracy('', '')
          100.0
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
          >>> round(accuracy(typed_string2, reference_text), 1)
          97.7
          >>> round(accuracy(typed_string3, reference_text), 1)
          100.0
          >>> round(accuracy(typed_string4, reference_text), 1)
          98.9
          >>> round(accuracy(typed_string5, reference_text), 1)
          49.7
          >>> round(accuracy(typed_string6, reference_text), 1)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('stere>ochromy teindable ur]ox]in anima\\dversiona(l haversine) silvered }shiftingly subassociation bra>nk', 'stere>ochromy teindable ur]ox]in anima\\dversiona(l haversine)'), 2)
          55.56
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('media,n nettlefish quadricostate p{isky ascr=y tympanism applicative thermom%=etrical', 'media,n nettlefish quadricostate p{isky ascr=y tympanism applicative thermom%=etrical \\pulsellum'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('sq)uamig,erous bulbocavernosus: brea?{cher sus%pen+ders dur_n"', 'sq)uamig,erous bulbocavernosus: brea?{cher sus%pen+ders dur_n"'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('gentlewomanly lot|to comit*atus electro?techn!ical unhostile tw_in suppression', 'gentlewomanly lot|to comit*atus electro?techn!ical unhostile'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("oxypropionic reburia_l greenwit\\h\\e obno'xiousn-ess commissioners lettab@le rugge]dn#ess", "oxypropionic reburia_l greenwit\\h\\e obno'xiousn-ess commissioners lettab@le"), 2)
          85.71
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('doomsman ;scouse` unlapped scelido@saur retter unmo:ckingly whispered}^ a}narchy', 'doomsman ;scouse` unlapped scelido@saur retter'), 2)
          62.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('cixiid sm:s ten"nisy d_umb in"stipul%ate peddlingly se&eker|', 'cixiid sm:s ten"nisy d_umb in"stipul%ate peddlingly'), 2)
          85.71
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("accredit o\\utba)n bemaddening ;apologe%te goma'>vel legific ;congruency ripienist strikin%gn'ess", "accredit o\\utba)n bemaddening ;apologe%te goma'>vel legific"), 2)
          66.67
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("pseudolite&rary polymorphous unspaded p{remorbidness c-auda` sor#bin postscri'|be demonstrational", "pseudolite&rary polymorphous unspaded p{remorbidness c-auda` sor#bin postscri'|be demonstrational shockable("), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('spec"io|logy zoografting acanthocephalous cyca|d hamperedness refusal catenulate co{mputab+le unhealthfully', 'spec"io|logy zoografting acanthocephalous cyca|d hamperedness'), 2)
          55.56
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('interlardment inquilinity p;olyemia spermatocyte concord %int>eraccuse', 'interlardment inquilinity p;olyemia spermatocyte concord %int>eraccuse s,uburbanho]od elenchi bargai>nor'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('u\\nintrigued .crut]ch cincture servulate trino"-dine helleboraceous', 'u\\nintrigued .crut]ch cincture servulate trino"-dine'), 2)
          83.33
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('pur#blindly overweeningly educa<tionabl?e [arginineph,osphoric postliminy apopetalo=us p%aintb$all mikie', 'pur#blindly overweeningly educa<tionabl?e [arginineph,osphoric postliminy apopetalo=us p%aintb$all mikie'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('scrawler epitritic se?ven}th supposabl+e unexerted paintroot a@,tmidalbumin', 'scrawler epitritic se?ven}th supposabl+e unexerted'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('po^chay( ;terp|in unfumb\\ling accountably lentiscine papa!li+zer mossiness cytosin)e', 'po^chay( ;terp|in unfumb\\ling accountably lentiscine'), 2)
          62.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('undeleted n[ebulosity erythrocyte nervous agar>', 'undeleted n[ebulosity erythrocyte nervous agar> cryptoscope s]o:rryhearted intendit c,a#pitaldom'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('kath`al pronumber radknight dynamic =?shudderingly #head?line', 'kath`al pronumber radknight dynamic =?shudderingly #head?line'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('osmotic[ irreligiousness g/ratuitousness mesotron an$~y pimplo^', 'osmotic[ irreligiousness g/ratuitousness mesotron an$~y pimplo^'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('i}ncendiarism fi)ctiona#lly mart@ineta satire labyrinth$ibranch hemospas{tic unwrung', 'i}ncendiarism fi)ctiona#lly mart@ineta satire labyrinth$ibranch hemospas{tic unwrung clashingly+'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('scriver an]te[prandial dutymon=[ger faradocon,tractility fridsto&ol ce<recloth thickene\\r', 'scriver an]te[prandial dutymon=[ger faradocon,tractility fridsto&ol'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("cavern bra?t !ranc[e indemnificatory 'splendes}cent ro~mbowline no,nsuit rha,mnoni|c", "cavern bra?t !ranc[e indemnificatory 'splendes}cent ro~mbowline no,nsuit"), 2)
          87.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('plimsoll endognath zoospori<fe~rous patibulate cubici*ty prepossess', 'plimsoll endognath zoospori<fe~rous patibulate cubici*ty'), 2)
          83.33
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('saponify nonl?umin,ous {mashi/e em(ployment underdeck stylohyoide:us r=oguing bre>adbox photoalbu+m\\', 'saponify nonl?umin,ous {mashi/e em(ployment underdeck stylohyoide:us r=oguing bre>adbox photoalbu+m\\'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('gelatinizability unguess-ed pyelot>omy u-nquibbled &bristletail interleave a^ct}inomeric dacryohemorrhea', 'gelatinizability unguess-ed pyelot>omy u-nquibbled &bristletail'), 2)
          62.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('u<ranophane arrested con`,fined bushing= beza~nt c~-lark a<lkyli"dene', 'u<ranophane arrested con`,fined bushing= beza~nt c~-lark a<lkyli"dene ast+uteness'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('indu[lt tolu) vult~ure end(orsee amidoaldehyde [bondholding reti;red %challenge@ jibbah', 'indu[lt tolu) vult~ure end(orsee amidoaldehyde [bondholding reti;red'), 2)
          77.78
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('_dissolvableness scatosc<opy nama^ycush chargeless diammo+n:ium', '_dissolvableness scatosc<opy nama^ycush chargeless diammo+n:ium sinistrogyrate'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('cataphyllum r]f le#rp bel%lyp<inch itc@!hweed cy}clopo-id ungeometric #meteyard', 'cataphyllum r]f le#rp bel%lyp<inch itc@!hweed'), 2)
          62.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('inc?orp!orable bidder giddybra)in stegoce{p,halous an.thropothei/sm teenty', 'inc?orp!orable bidder giddybra)in stegoce{p,halous an.thropothei/sm teenty'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('a)ccresc!e nephroto}my crookne?cked buddage ~neb(alian unanimousness scripturie-nc/y cler\\icalist', 'a)ccresc!e nephroto}my crookne?cked buddage ~neb(alian unanimousness scripturie-nc/y cler\\icalist untotaled'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('e@sophagomalac`ia men<iscitis endotr?achel?itis }differenti`al dapifer c\\onfelicity jurisdictio^n)alism participa,ncy keratome"try', 'e@sophagomalac`ia men<iscitis endotr?achel?itis }differenti`al dapifer c\\onfelicity jurisdictio^n)alism participa,ncy keratome"try'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('benj_\\y densim_etri{c e}quimu^ltiple calaminary supermanho<o?d co$ttage$rs uncombatable', 'benj_\\y densim_etri{c e}quimu^ltiple calaminary supermanho<o?d'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('archaic nystagmic wellh^ole$ s$hootable protyl po+i?sonproof schizoste&le barthite,', 'archaic nystagmic wellh^ole$ s$hootable protyl po+i?sonproof schizoste&le barthite, heteroepic?'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('par*ap^sychical cam+pa{na patheticly~ scapigerous gr;oss; separatist standstill tri$chophytia i(n$hibitable', 'par*ap^sychical cam+pa{na patheticly~ scapigerous gr;oss;'), 2)
          55.56
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('colly[ harrowment, extraphenomen=al enfelon zygo@[morphous und?&erusher', 'colly[ harrowment, extraphenomen=al enfelon zygo@[morphous und?&erusher unbullet~ined'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('-clodpated purana gramophonically unpitie-}dly mi-crosaurian unsequentia.l', '-clodpated purana gramophonically unpitie-}dly mi-crosaurian unsequentia.l kirkya]rd e}xaugurate ^k}elp'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("p_imp-le strata g'entisin[ incunabula huron unoped^ super.infinite", "p_imp-le strata g'entisin[ incunabula huron"), 2)
          71.43
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('saiga ri$z_zle trinal confounder succulentn]es-s sandnecker counterflange and+rogenesis', 'saiga ri$z_zle trinal confounder succulentn]es-s sandnecker counterflange and+rogenesis oligostemonous'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('nonassortment e"nn\\ui mis"t+ressdom r.|ab leptodermatou`s, oligocystic}/', 'nonassortment e"nn\\ui mis"t+ressdom r.|ab leptodermatou`s, oligocystic}/ snag:ger pra`+gmatical'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('uninterlocked $nou`menalism sheer} iota <aqu?ation reannouncement', 'uninterlocked $nou`menalism sheer} iota <aqu?ation reannouncement'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('di-pheno"l >undersuck\\ synostos*e amphidis:c/ophoran lingu>a wh&ereunto geek}$ per,ichete', 'di-pheno"l >undersuck\\ synostos*e amphidis:c/ophoran lingu>a'), 2)
          62.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('e"ar;tab overcrowdedne_ss dermatophyte pich\'u;ric depickle>', 'e"ar;tab overcrowdedne_ss dermatophyte pich\'u;ric depickle> politzerize ob@pyriform< vasemaking'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('liqu(i{dly phronti+ste[rium o@utfla?nk t&rophopathy nike viscerotonia@ p_ander} pa|narthrit|is', 'liqu(i{dly phronti+ste[rium o@utfla?nk t&rophopathy nike viscerotonia@ p_ander} pa|narthrit|is diplopterous'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('_cinnabarine di`senvelop di!s\\promise k" moss@$ery acanthoc-ephalan acetonic lightmouthed #generator', '_cinnabarine di`senvelop di!s\\promise k" moss@$ery'), 2)
          55.56
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('remonetize peroxi\\d]ic oatl.@ike spermoph/orium oxyproline va%letud*inarist erectility) jolt;ine>ss a{lnic=o', 'remonetize peroxi\\d]ic oatl.@ike spermoph/orium oxyproline va%letud*inarist erectility) jolt;ine>ss'), 2)
          88.89
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("photomezzotype pre@completion o]hia convolut[ely subprofessor fonduk amphibiology diad'ochokinetic", "photomezzotype pre@completion o]hia convolut[ely subprofessor fonduk amphibiology diad'ochokinetic"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('heterochthon,ous| gu!e) bi#nuk#au instellation ro{;e', 'heterochthon,ous| gu!e) bi#nuk#au instellation ro{;e brigander structure m{acrodont unappraised'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('bandicoot macarism thunder<ball p=arapl,egy perviability', 'bandicoot macarism thunder<ball p=arapl,egy perviability'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("podgily collectivism 'mitotically# [embryulcia~ bo:)wstring", "podgily collectivism 'mitotically# [embryulcia~ bo:)wstring g+lo@ss im`pervestiga{ble inter{<cale"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("haema=tosepsi?s di{s<cernible inspectingly y'east` diesel unsubduedly naturalist", "haema=tosepsi?s di{s<cernible inspectingly y'east` diesel"), 2)
          71.43
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("ratt}lebox deweyl'ite tem:p(erature j'oke_let hyperp!yrexi*a", "ratt}lebox deweyl'ite tem:p(erature j'oke_let hyperp!yrexi*a"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('subsi;de potting auto&/ecy holo{metab+olous heptahydrated" putresce', 'subsi;de potting auto&/ecy holo{metab+olous heptahydrated"'), 2)
          83.33
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('{dipl\\oglossate d$u$dishness <cinerarium uninvolved capit+|ol isosei%st chromy trac,tiferous irrevoluble', '{dipl\\oglossate d$u$dishness <cinerarium uninvolved capit+|ol isosei%st chromy trac,tiferous'), 2)
          88.89
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('~?whacky acronyx exi=m&ious convivial^it\\y sno\\bd}om squamella', '~?whacky acronyx exi=m&ious convivial^it\\y sno\\bd}om squamella +ci=vically recordant'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('posthexaplaric waistcoat\'hole sprangly underoxidize ?[fiar exequa"tu=r strongy<]lidosis', 'posthexaplaric waistcoat\'hole sprangly underoxidize ?[fiar exequa"tu=r'), 2)
          85.71
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('profa|nism [inpardonable lamet}er| hysteri@a tra(sh| ur.ethroplas,tic strepent', 'profa|nism [inpardonable lamet}er| hysteri@a tra(sh|'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('ren/abl*y pseudomnesia m\\yxedem:ic ,isoc,itric patta^ble credence mi*sbetide thrif;t =dentilo-quy', 'ren/abl*y pseudomnesia m\\yxedem:ic ,isoc,itric patta^ble'), 2)
          55.56
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('zoosporangiophore &davach alco #appointe paleos&tyl%y', 'zoosporangiophore &davach alco #appointe paleos&tyl%y su)mpi~tan subgo-d'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('prete/rmitter rhizostomo"us sacramentum {co+ffeetime avadana furtive \'parsoning laterotemporal', 'prete/rmitter rhizostomo"us sacramentum {co+ffeetime avadana'), 2)
          62.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('^prefacer optotechnics accredita}te so?ft maidho,od n=%ondenunciation', '^prefacer optotechnics accredita}te so?ft maidho,od n=%ondenunciation ro*undel fomites ref|igh^t'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('toxic t#ugurium swif|)t fascisticization palmiped planktologist', 'toxic t#ugurium swif|)t fascisticization palmiped planktologist re$e:dily'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("earthly b#rangl`ing ent:ellus roadwise thea>t:ron antic>ombinati+on fe'b.rific p*:yoid", "earthly b#rangl`ing ent:ellus roadwise thea>t:ron antic>ombinati+on fe'b.rific"), 2)
          87.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('polariscopy> mast<erman v&esiculotympanic phr)enodynia nervelessn!ess psychest@hetic+ gregarinifor"m', 'polariscopy> mast<erman v&esiculotympanic phr)enodynia nervelessn!ess'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('!b<rushed nap{hthalol unsacrif_icing dharmasutra monocyanogen calden undue*nes(s dentilabial xylidic', '!b<rushed nap{hthalol unsacrif_icing dharmasutra monocyanogen calden undue*nes(s dentilabial xylidic'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("overkind; )th|inghood sync#op%e thermogalvan`ometer anergy motet+tist ch'amp-ion exq,uisi_te unperceptible", 'overkind; )th|inghood sync#op%e thermogalvan`ometer anergy motet+tist'), 2)
          66.67
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('sperm"ali\'st dextrad misinformant_ deiformi_ty_ unfeignably', 'sperm"ali\'st dextrad misinformant_ deiformi_ty_ unfeignably'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('pleth:oreti.cal regener.atrix; thiosulphon`ic br!+ewst unreveal`edne!ss doublehan-d*ed lifestyle vi}(leness endocorpus{cular', 'pleth:oreti.cal regener.atrix; thiosulphon`ic br!+ewst unreveal`edne!ss doublehan-d*ed lifestyle vi}(leness endocorpus{cular'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('spermatopho*re app^rov.ed crotch$ hushel in".rush predictation glo@ch*idian ka`rst{ic', 'spermatopho*re app^rov.ed crotch$ hushel in".rush predictation glo@ch*idian'), 2)
          87.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('gangrenous doctrinarian nonphosphorized moments warfarer unarduous" coad"unativ_ely', 'gangrenous doctrinarian nonphosphorized moments warfarer unarduous" coad"unativ_ely gan\\g{ remunerator'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('polarly p*ostt]oxic radioanaphylaxis nymp+holept $semirustic residuary between chokerm_an', 'polarly p*ostt]oxic radioanaphylaxis nymp+holept $semirustic residuary'), 2)
          75.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('renominate stays@ail revisualization confiding upbubble finlike hierogrammate', 'renominate stays@ail revisualization confiding upbubble'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('tarsoplasty ~myrmicoid" myc}etophilid pyrenocarpous kalymmaukion multicus;pid urethrectomy; p;reagitate=', 'tarsoplasty ~myrmicoid" myc}etophilid pyrenocarpous kalymmaukion multicus;pid urethrectomy; p;reagitate='), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('fibri&nate} traveler@ess patamar breediness" hypodiatessaron', 'fibri&nate} traveler@ess patamar breediness" hypodiatessaron week post)adjun|ct k$eeve^'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("stockwrigh't twitt%ery dallying hom@opetalous amp?l%ificatory venous d-rumlike", "stockwrigh't twitt%ery dallying hom@opetalous amp?l%ificatory venous d-rumlike"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('to*ot%hy gas$troblennorrhea accom}:modations unsente>nc$ed s/hoplifter is%acoust?ic f*a(irm anthe(*rless', 'to*ot%hy gas$troblennorrhea accom}:modations unsente>nc$ed s/hoplifter is%acoust?ic'), 2)
          75.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy(')uncontentedness #phenanthroline< tim>ba|ng sclerocauly eruc;!ic', ')uncontentedness #phenanthroline< tim>ba|ng sclerocauly eruc;!ic'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('re"achie:ve phal{)angean managerial?ly de[cid>uoma pentland@ite- hono?re;e', 're"achie:ve phal{)angean managerial?ly de[cid>uoma pentland@ite-'), 2)
          83.33
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy(']wapp met-astatically pent%[adecylic col+loca:l daed^al<oid photochromy o)utflourish cruiv>e% {sloe', ']wapp met-astatically pent%[adecylic col+loca:l daed^al<oid photochromy o)utflourish cruiv>e% {sloe'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('lovably sheepmonger $ha-te unblade art!is\\try', 'lovably sheepmonger $ha-te unblade art!is\\try messil\\y'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('wambly capillose monstricid\\e rh:ymemaking. co?mbi~ned spectatorshi;p: searcloth', 'wambly capillose monstricid\\e rh:ymemaking. co?mbi~ned spectatorshi;p: searcloth hete#ropat[hy'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('pleioni[$an pa&radoxicalness circuitman unakin{ proficient pedicell$a{tion philodox! >pl(acemanship un=curably', 'pleioni[$an pa&radoxicalness circuitman unakin{ proficient pedicell$a{tion philodox! >pl(acemanship'), 2)
          88.89
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('o,bs,tupefy r+at sti%gmarian ?a+zimuthally v?estryize h%yperdemocr}acy unremorseful `interbring', 'o,bs,tupefy r+at sti%gmarian ?a+zimuthally v?estryize h%yperdemocr}acy'), 2)
          75.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('cithar|a m/azopathia; pos,tillator tipc&at asperat^e grat>ifyingly fibrositis nonoperative', 'cithar|a m/azopathia; pos,tillator tipc&at asperat^e grat>ifyingly fibrositis'), 2)
          87.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('beseem pasmo )herm%itship shiningly exec:ra=ble /apelet tardi*grade', 'beseem pasmo )herm%itship shiningly exec:ra=ble'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('agamid cellulipetal buffer! p_reoffen%se ^aethered. clif.;tonite #aca\\udal', 'agamid cellulipetal buffer! p_reoffen%se ^aethered. clif.;tonite'), 2)
          85.71
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('subscience nag?yagite cahot]" arzrun\\`ite trousers d(odding sulphantimonate\'', 'subscience nag?yagite cahot]" arzrun\\`ite trousers'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('raise virtualism epiboulangerit-e ingratiato<ry calfkill postthalamic cuesta ?malconformat<ion ]ungenteelness', 'raise virtualism epiboulangerit-e ingratiato<ry calfkill'), 2)
          55.56
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('phelloder>ma!l hermaean/ lustrant un[simplify leucocyt>openia credensiveness babi|rusa^ trivantly(', 'phelloder>ma!l hermaean/ lustrant un[simplify leucocyt>openia credensiveness babi|rusa^ trivantly('), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('cate+rcorner ;trifo"ld stee,ly misreco(gnize tap|em[an', 'cate+rcorner ;trifo"ld stee,ly misreco(gnize tap|em[an'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('sw,arfer& turjit`e( podat?<us ophtha["lmocopia enw~rapment <vimen kappland sovrant;y', 'sw,arfer& turjit`e( podat?<us ophtha["lmocopia enw~rapment <vimen kappland sovrant;y pa"rt'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('unilocularity tan!+trum =l.inking ~orthogneis)s ;dyslog*y at/omize" ovenm)an a=r;eometrical', 'unilocularity tan!+trum =l.inking ~orthogneis)s ;dyslog*y at/omize" ovenm)an'), 2)
          87.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('ratt/lejack agape{+ sacramen<tally term=inology inde<ntatio|n terminologi|st mu%ltifor|m', 'ratt/lejack agape{+ sacramen<tally term=inology inde<ntatio|n terminologi|st mu%ltifor|m'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('boycott\'ism, ungr_ound"able unslapped nil fo`rfa=rs v:aliant hera%ld', 'boycott\'ism, ungr_ound"able unslapped nil fo`rfa=rs v:aliant hera%ld'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('@agrobiological pala?eoethnic unpenitent<ness fetalism venue overdominat&e, co<nvex nuclear', "@agrobiological pala?eoethnic unpenitent<ness fetalism venue overdominat&e, co<nvex nuclear sei'smatical"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('te$n piccadil^l )explora;ble aphidicolous_ ho)oly prophetless conch vid_ya', 'te$n piccadil^l )explora;ble aphidicolous_ ho)oly prophetless conch'), 2)
          87.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('te#mp&larlikeness feasibleness big<e)minum ato:,merg pseudoministerial j@ose#', 'te#mp&larlikeness feasibleness big<e)minum ato:,merg pseudoministerial j@ose# warehouse h-emigl#yph'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('fungous ra"is pe`n hexe&#ne in|seam nevel a(am chondrocele duchy', 'fungous ra"is pe`n hexe&#ne in|seam nevel a(am'), 2)
          77.78
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('imm(usical rooklet some>wise kirimon woolshed .differe|nt ingrain', 'imm(usical rooklet some>wise kirimon woolshed .differe|nt ingrain superexam}iner'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('wett"ish co#nfric*ation wi@chtje pentyne$ fluorite chatterbox cause*[less', 'wett"ish co#nfric*ation wi@chtje pentyne$ fluorite chatterbox cause*[less'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('stilted disadvantageously autotetraploid a\\$ppellative forwea`n oophorotomy', 'stilted disadvantageously autotetraploid a\\$ppellative forwea`n oophorotomy -!rouper viragin`'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import accuracy
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
