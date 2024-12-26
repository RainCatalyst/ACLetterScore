"""The Animal Crossing letter scoring system based on https://jamchamb.net/projects/animal-crossing-letters"""

trigrams = {
    'a': 'blbobrbsccchcrctdddmdverfffrftgagegoheirlilllmlolrlsltlwm memondngninonsnypappprrergrmrrrtsisksltetmttudugutvevowa',
    'b': 'abacadagalanasate eaecedeeefegeheleseteyicigikiliritlaleloluoaodonooorotouoxoyrarerirouiurusutuyy ',
    'c': 'akalamanaparasatauenerhahehihohihuiritlalelilooaofoiolomonoooporosouovowreriroryupurusut',
    'd': 'adaiamanaratauayeaeceeefegelemenepesetevicidieifiginirisivo ocoeogolonooouowozrareriroruryueurusut',
    'e': 'acarasatduffggigitlelsmpndnengnjnontqurrspurvexaxcxexpye',
    'f': 'acaialamarasateaebedeeelewieifigilinirisivixlalelilolyolooorourareriroruulunut',
    'g': 'aiamarasataveneretirivlao odoionoootovrarerouaueuiun',
    'h': 'abadaialanaparasatave eaeieleri idigilimirisitolomonoporosotouowumunurus',
    'i': '  cedef mammmpn ncndnfnsntnvros slt ts',
    'j': 'anapoboiudulumunus',
    'k': "eeepeyicilinitneninoabadaiakanarasatauawayazeaedefegenesetevibieifigikiminisitivoconooosotouovowunyiacadagaiajakanaparataye eaedeeemenesetidigilinisodomonooorosotouovucumusy ysamarateaeceeeievewexicigino oboionooorosotovowumbj'cctf fffth ilkaldn ncnenlpepippr rardthurutvewn",
    'p': 'acagaiaparasatayeaeneoerhoicieiniplaleocoioloooposotouowrareriroubulupurusut',
    'q': 'uaueui',
    'r': 'acadaianapateaecedefegelemepeqeseticidiginisivoaocodolooosouowulunus',
    's': 'adafaialamanatavawaycechcicoeaeceeeleneperetevexhahehihohuicidigiliminisitixizkikylelilomamemimonoo oaocofoiolomonoooroupapepipoprqutatetitotrtutyubucudufugumunupurwawewiwuys',
    't': 'abakalasauaxeaeeelemenereshahehihohrhuicieilimirito odogolomonoooporotouowrareriroruryueurv wewiwoyiyp',
    'u': 'nancndninlntp pos sesu',
    'v': 'alaregerieilisoiolotaiakalanarasatavaye eaedeeeieleneresethahehihohyidifilinirisitivokomonooorouriroma',
    'y': 'areaelenesetou',
    'z': 'er'
}

punctuation = ['.', '?', '!']
alphabet = ' a b c d e f g h i j k l m n o p q r s t u v w x y z'.replace(' ', '')
alphabet_upper = alphabet.upper()

"""Utility functions"""
def has_capital_letter(text):
    for letter in alphabet_upper:
        if letter in text:
            return True
    return False

def is_letter(letter):
    return letter.lower() in alphabet

def is_punctuation(letter):
    return letter in punctuation

def has_trigram(word):
    letter = word[0].lower()
    if letter not in trigrams:
        return False
    word_start = word[:3].lower()
    trigram_str = trigrams[letter]
    for i in range(0, len(trigram_str), 2):
        trigram = letter + trigram_str[i:i+2]
        if word_start == trigram:
            return True
    return False

"""Scoring functions as described in the article"""  
def get_A(text):
    score = 0
    if is_punctuation(text[-1]):
        score += 20
    for i, letter in enumerate(list(text)):
        if is_punctuation(letter):
            if has_capital_letter(text[i + 1:i + 4]):
                score += 10
            else:
                score -= 10
    return score

def get_B(text):
    score = 0
    for word in text.split(' '):
        if len(word) < 3:
            continue
        if has_trigram(word):
            score += 1
    return score * 3

def get_C(text):
    for letter in text:
        if is_letter(letter):
            if letter == letter.upper():
                return 20
            else:
                return -10
    return 0

def get_D(text):
    last_c = ""
    last_count = 0
    for letter in text:
        if is_letter(letter):
            if letter == last_c:
                last_count += 1
                if last_count > 2:
                    return -50
            else:
                last_c = letter
                last_count = 1
        else:
            last_c = ""
            last_count = 0
    return 0

def get_E(text):
    space_count = 0
    for letter in text:
        if letter == ' ':
            space_count += 1
    nonspace_count = len(text) - space_count
    ratio = (space_count) * 100 // nonspace_count
    if ratio < 20:
        return -20
    return 20

def get_F(text):
    if len(text) < 75:
        return 0
    found_any = False
    for letter in text[:75]:
        if is_punctuation(letter):
            found_any = True
            break
    if not found_any:
        return -150
    return 0

def get_G(text):
    score = 0
    for i in range(0, len(text), 32):
        block = text[i:i+32]
        if ' ' not in block:
            score -= 20
    return score

"""Calculate score for the whole letter"""
def get_letter_score(text):
    score = 0
    score += get_A(text)
    score += get_B(text)
    score += get_C(text)
    score += get_D(text)
    score += get_E(text)
    score += get_F(text)
    score += get_G(text)
    return score