test = {
  'name': 'Problem 5',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> abs_diff = lambda w1, w2, limit: abs(len(w2) - len(w1))
          >>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 10)
          'cult'
          >>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 0)
          'cul'
          >>> autocorrect("wor", ["worry", "car", "part"], abs_diff, 10)
          'car'
          >>> first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0
          >>> autocorrect("wrod", ["word", "rod"], first_diff, 1)
          'word'
          >>> autocorrect("inside", ["idea", "inside"], first_diff, 0.5)
          'inside'
          >>> autocorrect("inside", ["idea", "insider"], first_diff, 0.5)
          'idea'
          >>> autocorrect("outside", ["idea", "insider"], first_diff, 0.5)
          'outside'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
          >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
          'butter'
          >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
          >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
          'testing'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> matching_diff = lambda w1, w2, limit: sum([w1[i] != w2[i] for i in range(min(len(w1), len(w2)))]) # Num matching chars
          >>> autocorrect("tosting", ["testing", "asking", "fasting"], matching_diff, 10)
          'testing'
          >>> autocorrect("tsting", ["testing", "rowing"], matching_diff, 10)
          'rowing'
          >>> autocorrect("bwe", ["awe", "bye"], matching_diff, 10)
          'awe'
          >>> autocorrect("bwe", ["bye", "awe"], matching_diff, 10)
          'bye'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> words_list = sorted(lines_from_file('data/words.txt')[:10000])
          >>> autocorrect("testng", words_list, lambda w1, w2, limit: 1, 10)
          'a'
          >>> autocorrect("testing", words_list, lambda w1, w2, limit: 1, 10)
          'testing'
          >>> autocorrect("gesting", words_list, lambda w1, w2, limit: sum([w1[i] != w2[i] for i in range(min(len(w1), len(w2)))]) + abs(len(w1) - len(w2)), 10)
          'getting'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('stereochromy', ['stereochromy'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'stereochromy'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('ascry', ['meroplankton', 'foremilk', 'nettlefish', 'artery', 'quadricostate', 'subsident', 'pisky', 'spleet', 'boss', 'septum'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'pisky'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('gromatics', ['sair', 'heterodromy', 'butylene', 'gromatics', 'sprayfully', 'denial', 'bulbocavernosus'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'gromatics'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('foelike', ['nonpublication'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'foelike'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('whissle', ['surmaster', 'thingstead', 'downbeard', 'ruggedness', 'radulate', 'phaenomenism', 'unwatchfully', 'myelopetal'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'whissle'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('lunged', ['extracted'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'lunged'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('meliphagidan', ['singlehandedness', 'fumiferous', 'inescapable'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'meliphagidan'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('deltation', ['deltation', 'esophagomalacia', 'gramineal', 'kiteflier', 'outban', 'theah', 'exormia'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'deltation'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('cauda', ['electroextraction', 'polymorphous', 'cooperative', 'unspaded', 'uncontradictedly', 'premorbidness', 'unuxorious', 'contemptibleness', 'bronchoegophony', 'cauda'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'cauda'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('ampullar', ['fogon', 'intercommunion', 'artful', 'chirapsia', 'nonconfidential'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'ampullar'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('mackenboy', ['inquilinity'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'inquilinity'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('misdemeanor', ['elderwood', 'arachnean', 'luminist', 'sigger', 'bandhook', 'cincture', 'probachelor', 'servulate'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'probachelor'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('parter', ['mismotion', 'counterpuncture', 'prevolitional'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'parter'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('yarding', ['scrawler'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'yarding'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('tripody', ['concurringly', 'glyoxaline', 'terpin', 'kinetoscopic', 'chloralism', 'obvelation', 'unfumbling', 'tripody'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'tripody'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('bluffer', ['subrogation', 'lownly', 'nebulosity', 'capricci', 'compelling', 'bluffer'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'bluffer'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('autodetector', ['supercargoship', 'keelblock', 'celiosalpingectomy', 'pronumber', 'costotomy', 'radknight'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'supercargoship'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('stonable', ['coalhole', 'osmotic', 'barnard', 'irreligiousness', 'nitrobacteria', 'cellarless', 'gratuitousness'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'coalhole'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('perisystole', ['saphie', 'bracket', 'quayman'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'perisystole'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('anteprandial', ['workhouse', 'scriver', 'chilicothe'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'chilicothe'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('panichthyophagous', ['involucriform', 'excecate', 'patrist', 'rhamnohexite'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'panichthyophagous'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('enhanced', ['hanse', 'endognath', 'cluck', 'zoosporiferous', 'stegosaurian'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'endognath'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('nonluminous', ['bakerless'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'bakerless'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('stereochromically', ['meat'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'stereochromically'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('subaffluent', ['citriculturist', 'installing', 'earthquaking'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'subaffluent'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('pimperlimpimp', ['novaculite', 'tolu', 'arrhizous', 'kinchin', 'pimperlimpimp', 'vulture', 'hirudinize', 'exscriptural'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'pimperlimpimp'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('dissolvableness', ['unratable'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'unratable'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('intraclitelline', ['rf', 'intraclitelline', 'automatism', 'hagbush', 'lerp', 'mesoarium', 'myelocytic', 'bamboula', 'clevis'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'intraclitelline'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('akcheh', ['elicitory', 'nonrevelation', 'conducting', 'chromogenesis', 'projectile', 'bidder'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'bidder'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('nephrotomy', ['unreproachableness', 'incomputable', 'sulphosuccinic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'incomputable'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('meniscitis', ['contuse', 'esophagomalacia', 'investigatorial', 'tassard', 'probational'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'probational'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('antianthropomorphism', ['calaminary', 'supermanhood', 'passless', 'calculate', 'corruptibleness', 'unsoul', 'cottagers', 'aspects'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'antianthropomorphism'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('shootable', ['nystagmic', 'refute', 'wellhole', 'tallowlike', 'lumen', 'definable', 'misaccentuation', 'incluse', 'snipperty'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'nystagmic'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('ganger', ['parapsychical', 'revengement', 'unappendaged', 'ganger', 'projiciently', 'campana', 'superius', 'stodgery', 'cambial'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'ganger'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('churchful', ['underheaven', 'harrowment', 'chapless', 'reaminess', 'patriarchate', 'reputation', 'extraphenomenal'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'reaminess'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('vasculated', ['digestment', 'hierocratic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'digestment'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('rachicentesis', ['pimple', 'unbundled', 'bencite', 'unfrustrably', 'thirteenth', 'strata', 'prancer', 'gentisin', 'mono'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'unfrustrably'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('thresh', ['squatwise', 'nonplastic', 'lucernal', 'holarctic', 'trinal', 'thresh', 'menaccanite'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'thresh'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('salvableness', ['uneducable', 'ennui', 'asdic', 'nonruminant'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'nonruminant'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('lionization', ['scrotectomy', 'noumenalism', 'botryomycoma', 'sphingometer', 'sensibilize', 'deconsecration', 'impersonatrix', 'sheer', 'murshid', 'sterhydraulic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'scrotectomy'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('iridodiagnosis', ['unboat', 'choate', 'disallowance', 'upcover'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'iridodiagnosis'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('demagnetization', ['manioc', 'demagnetization', 'superglacial'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'demagnetization'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('histomorphology', ['talisay'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'histomorphology'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('orlop', ['orlop', 'ovolo'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'orlop'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('crustation', ['remonetize', 'crustation'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'crustation'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('handhold', ['precompletion'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'handhold'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('gue', ['dioestrous', 'heterochthonous', 'supraseptal', 'heading', 'serpuline', 'nomothetic', 'quantum', 'suprasquamosal', 'autographometer'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'heading'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('spheroconic', ['osmate'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'spheroconic'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('collectivism', ['collectivism', 'mitotically'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'collectivism'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('gamogenetically', ['tarsus', 'starlitten', 'ut', 'subcortically', 'ureameter', 'detruncation', 'expressible', 'controversialism', 'subtropical'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'gamogenetically'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('domiciliary', ['domiciliary', 'octodactylous'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'domiciliary'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('amphilogy', ['overdemocracy'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'amphilogy'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('inlooker', ['disquietedness', 'manufactural', 'geitonogamous', 'hyoscyamine', 'dudishness', 'carbonitride', 'unmonistic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'dudishness'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('timeliine', ['strack', 'whacky', 'stationery', 'shee', 'rebutter', 'yellows'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'stationery'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('underoxidize', ['posthexaplaric', 'dinglebird', 'waistcoathole', 'agleaf', 'overscepticism', 'wollastonite', 'sprangly', 'untinted'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'wollastonite'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('compone', ['profanism', 'pachysalpingitis', 'overweather', 'polyfold', 'inpardonable', 'hypercivilization', 'chamberlainry', 'lameter', 'dirndl'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'lameter'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('sorn', ['renably'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'renably'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('cystorrhaphy', ['pannierman', 'swampwood'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'cystorrhaphy'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('rhizostomous', ['nonactinic', 'retransmit', 'rhizostomous', 'tubba', 'intertrochanteric', 'sacramentum', 'noiseless', 'coffeetime', 'bombyciform', 'latterkin'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'rhizostomous'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('etiolin', ['nonscandalous', 'moneyflower', 'optotechnics', 'gollar', 'nonconceiving', 'accreditate'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'gollar'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('hydroforming', ['toxic', 'sphaeristerium', 'sexualization', 'tugurium', 'epineurium', 'engineership', 'swift'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'engineership'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('vitamin', ['subverticillate', 'counterannouncement'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'vitamin'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('audacity', ['phytometric', 'trephiner'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'audacity'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('actionize', ['peenge', 'equid', 'saltcatch', 'underpayment', 'ladyfy', 'actionize', 'colostric', 'naphthalol'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'actionize'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('automatous', ['crimple', 'soother', 'overkind', 'cinnamaldehyde', 'veretilliform', 'goldtit', 'automatous', 'thinghood'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'automatous'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('heptarchist', ['provisionalness', 'unconscientiously'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'heptarchist'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('superioress', ['electrotechnology', 'superioress', 'phenomenist', 'telencephalon'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'superioress'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('crotch', ['sapping', 'untriced', 'kerogen', 'approved', 'unfairness', 'unhypothetical', 'entomophytous', 'philosophastry'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'sapping'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('destructivism', ['swimmingly', 'gonnardite', 'darlingness', 'worldy', 'excyst', 'deservedness', 'reignite', 'acquitment', 'finement', 'decemvir'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'destructivism'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('architectress', ['beachy'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'architectress'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('frenetically', ['fascicular'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'frenetically'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('spermology', ['myrmicoid', 'nonofficial', 'prinky', 'metaphony', 'subacromial', 'mycetophilid', 'chemolyze', 'ungroundedness', 'nonopposition'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'myrmicoid'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('chrismation', ['underbuy', 'mopla', 'footplate', 'traveleress', 'gemmiparously', 'chrismation'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'chrismation'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('respond', ['philosopher', 'tarn', 'storeman', 'styleless', 'hemiglossitis', 'rangership', 'implantation', 'sabalo', 'dhaura'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'respond'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('ultraviolent', ['sufflate', 'everduring', 'drawly', 'ephphatha', 'onwards'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'ultraviolent'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('planetography', ['teacher', 'upwrought', 'planetography', 'phenanthroline'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'planetography'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('teaboy', ['sismotherapy', 'reachieve', 'unwavering', 'jestproof', 'overleisured', 'phalangean', 'parvoline', 'invariantly'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'reachieve'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('schoolboydom', ['pitfall', 'bardel', 'shieldlessness', 'metastatically', 'schoolboydom', 'arvicolous'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'schoolboydom'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('underwage', ['yoven', 'lovably', 'sheepmonger', 'molave', 'hate', 'walloon', 'homostylism', 'decumbiture'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'lovably'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('downlooked', ['hydrotechnic', 'capillose', 'unfaultfinding', 'monstricide', 'associationalist'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'capillose'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('magistratically', ['pleionian', 'guige', 'tellureted', 'magistratically'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'magistratically'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('stigmarian', ['activity', 'rat', 'driftpin', 'sledder'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'activity'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('redeploy', ['phylacterical', 'nonoccupation', 'underconcerned', 'counterquery', 'importantly', 'aecial'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'redeploy'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('obfuscable', ['interestingness', 'toheroa', 'biternately', 'afternose', 'jerm', 'paetrick', 'tripartition', 'uncolouredly', 'ponica', 'canonics'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'obfuscable'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('manifested', ['bribe'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'manifested'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('questionlessly', ['fleawood', 'semiharden', 'beglerbeg', 'washery', 'equibiradiate', 'superarrogant', 'sphingoid', 'panchway', 'ex', 'esterlin'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'questionlessly'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('closecross', ['dirigibility', 'epiboulangerite', 'closecross', 'tech'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'closecross'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('impreventable', ['patible', 'fribby', 'unfulfilled', 'jako', 'herbaged', 'unrebukably', 'myrabalanus', 'varnishment', 'baikerite'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'impreventable'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('differentiate', ['impermanency', 'differentiate'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'differentiate'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('radiologic', ['creirgist', 'pedicular', 'reordination', 'tristigmatose', 'coinhabit'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'radiologic'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('choristry', ['retaker', 'gashful', 'tantrum', 'podzolic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'podzolic'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('wordably', ['conciliator', 'indentation', 'globiferous'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'wordably'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('elaboratory', ['compromission', 'forfars', 'wud'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'elaboratory'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('dermad', ['zaphara', 'unlessoned', 'nuclidic', 'unidiomatic', 'palaeoethnic', 'platitudinarian', 'noncontinuance', 'psammous', 'unpenitentness'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'zaphara'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('unexuberant', ['homogenization', 'ramuscule', 'aphidicolous', 'tm', 'transuranian', 'ferry', 'monocarbonic', 'hooly', 'unassented'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'unexuberant'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('pericapsular', ['buffball', 'bigeminum'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'pericapsular'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('coplanar', ['cleeked', 'coplanar', 'pen', 'laundryowner', 'procarrier'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'coplanar'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('inappropriateness', ['nontyrannical', 'translocate', 'palaestra', 'ashamedly', 'flack', 'bulimia', 'headrent', 'backscraper'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'inappropriateness'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('objectively', ['weepered', 'spavied'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'objectively'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('mumpishly', ['sensorivascular', 'disadvantageously', 'hungarite', 'autotetraploid', 'enamdar', 'appellative', 'entoconid', 'obstreperosity', 'anartismos', 'prankish'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'hungarite'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import autocorrect, lines_from_file
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
