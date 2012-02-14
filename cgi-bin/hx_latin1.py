"""
módulo hx_latin1

utilitários para conversão entre:
    caracteres Latin-1,
    entidades HTML,
    caracteres ASCII,
    caracteres UTF-8
"""

#19/01/2000: inclusao de cars2utf8 - LR
#10/02/2000: inclusao de cars2ascii e codepage 1252 (parcial) - LR
#19/04/2000: LR
#	- reimplementação de cars2ascii com translate
#	- criação de constantes com tabelas para translate

from string import join, find, replace, maketrans, translate, lower, upper

car_latin1 = {
    'À' : ('Agrave', 'A'),
    'Á' : ('Aacute', 'A'),
    'Â' : ('Acirc', 'A'),
    'Ã' : ('Atilde', 'A'),
    'Ä' : ('Auml', 'A'),
    'Å' : ('Aring', 'A'),
    'Æ' : ('AElig', 'A'),
    'Ç' : ('Ccedil', 'C'),
    'È' : ('Egrave', 'E'),
    'É' : ('Eacute', 'E'),
    'Ê' : ('Ecirc', 'E'),
    'Ë' : ('Euml', 'E'),
    'Ì' : ('Igrave', 'I'),
    'Í' : ('Iacute', 'I'),
    'Î' : ('Icirc', 'I'),
    'Ï' : ('Iuml', 'I'),
    'Ð' : ('ETH', 'E'),
    'Ñ' : ('Ntilde', 'N'),
    'Ò' : ('Ograve', 'O'),
    'Ó' : ('Oacute', 'O'),
    'Ô' : ('Ocirc', 'O'),
    'Õ' : ('Otilde', 'O'),
    'Ö' : ('Ouml', 'O'),
    '×' : ('times', '*'),
    'Ø' : ('Oslash', 'O'),
    'Ù' : ('Ugrave', 'U'),
    'Ú' : ('Uacute', 'U'),
    'Û' : ('Ucirc', 'U'),
    'Ü' : ('Uuml', 'U'),
    'Ý' : ('Yacute', 'Y'),
    'Þ' : ('THORN', 'T'),
    'ß' : ('szlig', 's'),
    'à' : ('agrave', 'a'),
    'á' : ('aacute', 'a'),
    'â' : ('acirc', 'a'),
    'ã' : ('atilde', 'a'),
    'ä' : ('auml', 'a'),
    'å' : ('aring', 'a'),
    'æ' : ('aelig', 'a'),
    'ç' : ('ccedil', 'c'),
    'è' : ('egrave', 'e'),
    'é' : ('eacute', 'e'),
    'ê' : ('ecirc', 'e'),
    'ë' : ('euml', 'e'),
    'ì' : ('igrave', 'i'),
    'í' : ('iacute', 'i'),
    'î' : ('icirc', 'i'),
    'ï' : ('iuml', 'i'),
    'ð' : ('eth', 'e'),
    'ñ' : ('ntilde', 'n'),
    'ò' : ('ograve', 'o'),
    'ó' : ('oacute', 'o'),
    'ô' : ('ocirc', 'o'),
    'õ' : ('otilde', 'o'),
    'ö' : ('ouml', 'o'),
    '÷' : ('divide', '/'),
    'ø' : ('oslash', 'o'),
    'ù' : ('ugrave', 'u'),
    'ú' : ('uacute', 'u'),
    'û' : ('ucirc', 'u'),
    'ü' : ('uuml', 'u'),
    'ý' : ('yacute', 'y'),
    'þ' : ('thorn', 't'),
    'ÿ' : ('yuml', 'y'),
    # Windows codepage 1252
    '‘' : ('lsquo',"'"),
    '’' : ('rsquo',"'"),
    '“' : ('ldquo','"'),
    '”' : ('rdquo','"'),
    '•' : ('bull', '-'),
    '–' : ('ndash', '-'),
    '—' : ('mdash', '-'),
    '˜' : ('tilde', '~'),
}

ent_latin1 = {
    'Agrave' : ('À', 'A'),
    'Aacute' : ('Á', 'A'),
    'Acirc' : ('Â', 'A'),
    'Atilde' : ('Ã', 'A'),
    'Auml' : ('Ä', 'A'),
    'Aring' : ('Å', 'A'),
    'AElig' : ('Æ', 'A'),
    'Ccedil' : ('Ç', 'C'),
    'Egrave' : ('È', 'E'),
    'Eacute' : ('É', 'E'),
    'Ecirc' : ('Ê', 'E'),
    'Euml' : ('Ë', 'E'),
    'Igrave' : ('Ì', 'I'),
    'Iacute' : ('Í', 'I'),
    'Icirc' : ('Î', 'I'),
    'Iuml' : ('Ï', 'I'),
    'ETH' : ('Ð', 'E'),
    'Ntilde' : ('Ñ', 'N'),
    'Ograve' : ('Ò', 'O'),
    'Oacute' : ('Ó', 'O'),
    'Ocirc' : ('Ô', 'O'),
    'Otilde' : ('Õ', 'O'),
    'Ouml' : ('Ö', 'O'),
    'times' : ('×', '*'),
    'Oslash' : ('Ø', 'O'),
    'Ugrave' : ('Ù', 'U'),
    'Uacute' : ('Ú', 'U'),
    'Ucirc' : ('Û', 'U'),
    'Uuml' : ('Ü', 'U'),
    'Yacute' : ('Ý', 'Y'),
    'THORN' : ('Þ', 'T'),
    'szlig' : ('ß', 's'),
    'agrave' : ('à', 'a'),
    'aacute' : ('á', 'a'),
    'acirc' : ('â', 'a'),
    'atilde' : ('ã', 'a'),
    'auml' : ('ä', 'a'),
    'aring' : ('å', 'a'),
    'aelig' : ('æ', 'a'),
    'ccedil' : ('ç', 'c'),
    'egrave' : ('è', 'e'),
    'eacute' : ('é', 'e'),
    'ecirc' : ('ê', 'e'),
    'euml' : ('ë', 'e'),
    'igrave' : ('ì', 'i'),
    'iacute' : ('í', 'i'),
    'icirc' : ('î', 'i'),
    'iuml' : ('ï', 'i'),
    'eth' : ('ð', 'e'),
    'ntilde' : ('ñ', 'n'),
    'ograve' : ('ò', 'o'),
    'oacute' : ('ó', 'o'),
    'ocirc' : ('ô', 'o'),
    'otilde' : ('õ', 'o'),
    'ouml' : ('ö', 'o'),
    'divide' : ('÷', '/'),
    'oslash' : ('ø', 'o'),
    'ugrave' : ('ù', 'u'),
    'uacute' : ('ú', 'u'),
    'ucirc' : ('û', 'u'),
    'uuml' : ('ü', 'u'),
    'yacute' : ('ý', 'y'),
    'thorn' : ('þ', 't'),
    'yuml' : ('ÿ', 'y'),
    # Windows codepage 1252
    'lsquo' : ('‘',"'"),
    'rsquo' : ('’',"'"),
    'ldquo' : ('“','"'),
    'rdquo' : ('”','"'),
    'bull' : ('•', '-'),
    'ndash' : ('–', '-'),
    'mdash' : ('—', '-'),
    'tilde' : ('˜', '~'),
}

ACENTOS_UPPER = 'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞß' 
ACENTOS_LOWER = 'àáâãäåæçèéêëìíîïðñòóôõöøùúûüýþß'
ASCIIS_UPPER  = 'AAAAAAACEEEEIIIIDNOOOOOOUUUUYTS'
ASCIIS_LOWER  = 'aaaaaaaceeeeiiiidnoooooouuuuyts'

TRANS_2LOWER = maketrans(ACENTOS_UPPER,ACENTOS_LOWER)
TRANS_2UPPER = maketrans(ACENTOS_LOWER,ACENTOS_UPPER)
TRANS_2ASCII = maketrans(ACENTOS_UPPER+ACENTOS_LOWER,ASCIIS_UPPER+ASCIIS_LOWER)

def acentos():
    return ACENTOS_UPPER + ACENTOS_LOWER
    
def asciis():
    return ASCIIS_UPPER + ASCIIS_LOWER

def car2ent(car):
    if car_latin1.has_key(car):
        return '&' + car_latin1[car][0] + ';'
    else:
        return car
        
def car2ascii(car):
    if car_latin1.has_key(car):
        return car_latin1[car][1]
    else:
        return car
        
def ent2car(ent):
    ent = ent[1:-1]  #retirar & e ; antes de buscar
    if ent_latin1.has_key(ent):   
        return ent_latin1[ent][0]
    else:
        return ent
        
def html2cars(texto):
    if find(texto, '&') == -1: #não existem entidades html no texto
        return texto
    else:
        for ent in ent_latin1.keys():
            html_ent = '&' + ent + ';'
            if find(texto, html_ent) >= 0:
                texto = replace(texto, html_ent, ent_latin1[ent][0])
        return texto

def cars2html(texto):
    for car in acentos():
        if find(texto, car) >= 0:
            texto = replace(texto, car, '&' + car_latin1[car][0] + ';')
    return texto

def cx_baixa(texto):
    return translate(lower(texto), TRANS_2LOWER)

def cx_alta(texto): 
    # nao funciona corretamente com entidades!!!
    # &atilde; vira &ATILDE; e deveria virar &Atilde;
    return translate(upper(texto), TRANS_2UPPER)
    
def cars2utf8(texto):
    # Conversao de ISO-8859-1 para UTF-8
    # Máscara UTF-8 válida na faixa 0x80 a 0x7FF: 110x xxab   10cd efgh
    saida = []
    for car in texto:
        i = ord(car)
        if i < 0x80:
            saida.append(car)
        else:
            b1 = i >> 6 | 0xC0  # (1100 0000 -> 0000 0011) | 1100 0000
            b2 = i & 0xBF       # 1011 1111
            saida.append(chr(b1))
            saida.append(chr(b2))
    return join(saida,'')

def cars2ascii(texto):
    return translate(texto,TRANS_2ASCII)
    
###### testes

def teste_cars(cars):
    for car in cars:
        print car, car2ascii(car), car2ent(car)
    
def teste_ents(ents):
    for ent in ents:
        print ent, ent2car(ent)
        
if __name__ == '__main__':
    
    cars = 'Emílio NÃO caça pavões.' 

    '''
    #teste_cars('BÀà×÷ÇçÏÿ')
    #print '-' * 40
    #teste_ents(['&Agrave;','&Auml;','&aacute;','&ETH;','&eth;','&yuml;'])
    #print '-' * 40
    print acentos()        
    print asciis()
    
    html = 'Em&iacute;lio N&Atilde;O ca&ccedil;a pav&otilde;es.'
    print cars
    print cars2html(cars)
    print html2cars(cars2html(cars))
    print html
    print html2cars(html)
    print cars2html(html2cars(html))
    print html2cars('Texto SEM acento & cedilha algum.')
    print cars2html('Texto SEM acento & cedilha algum.')
    print cx_baixa(cars)
    print cx_alta(cars)
    print cx_baixa(html)
    print cx_alta(html)
    '''
    '''
    print cars2utf8(cars)     
    print cars2utf8('Texto SEM acento & cedilha algum.')
    '''
    '''
    print join(car_latin1.keys(),'')
    lin = []
    for car in join(car_latin1.keys(),''):
        lin.append(car_latin1[car][1])
    print join(lin,'')
    '''

    print cars
    print cars2ascii(cars)
