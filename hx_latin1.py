#!/usr/bin/env python
# -*- coding: iso-8859-1 -*- 
"""
hx_latin1 2.1
utilities to convert between:
    Latin-1 characters (ISO-8859-1 and Windows codepage 1252),
    HTML entities,
    pure ASCII characters,
    UTF-8 characters
author: Luciano Ramalho
this code is in the public domain
"""

#12/12/2002: added several non-alphabetic chars (&copy; etc)
#19/04/2000: reimplemented cars2ascii with translate
#10/02/2000: added cars2ascii and most of codepage 1252
#19/01/2000: added cars2utf8

from string import join, find, replace, maketrans, translate, lower, upper

car_latin1 = {
    '�' : ('Agrave', 'A'),
    '�' : ('Aacute', 'A'),
    '�' : ('Acirc', 'A'),
    '�' : ('Atilde', 'A'),
    '�' : ('Auml', 'A'),
    '�' : ('Aring', 'A'),
    '�' : ('AElig', 'A'),
    '�' : ('Ccedil', 'C'),
    '�' : ('Egrave', 'E'),
    '�' : ('Eacute', 'E'),
    '�' : ('Ecirc', 'E'),
    '�' : ('Euml', 'E'),
    '�' : ('Igrave', 'I'),
    '�' : ('Iacute', 'I'),
    '�' : ('Icirc', 'I'),
    '�' : ('Iuml', 'I'),
    '�' : ('ETH', 'E'),
    '�' : ('Ntilde', 'N'),
    '�' : ('Ograve', 'O'),
    '�' : ('Oacute', 'O'),
    '�' : ('Ocirc', 'O'),
    '�' : ('Otilde', 'O'),
    '�' : ('Ouml', 'O'),
    '�' : ('times', '*'),
    '�' : ('Oslash', 'O'),
    '�' : ('Ugrave', 'U'),
    '�' : ('Uacute', 'U'),
    '�' : ('Ucirc', 'U'),
    '�' : ('Uuml', 'U'),
    '�' : ('Yacute', 'Y'),
    '�' : ('THORN', 'T'),
    '�' : ('szlig', 's'),
    '�' : ('agrave', 'a'),
    '�' : ('aacute', 'a'),
    '�' : ('acirc', 'a'),
    '�' : ('atilde', 'a'),
    '�' : ('auml', 'a'),
    '�' : ('aring', 'a'),
    '�' : ('aelig', 'a'),
    '�' : ('ccedil', 'c'),
    '�' : ('egrave', 'e'),
    '�' : ('eacute', 'e'),
    '�' : ('ecirc', 'e'),
    '�' : ('euml', 'e'),
    '�' : ('igrave', 'i'),
    '�' : ('iacute', 'i'),
    '�' : ('icirc', 'i'),
    '�' : ('iuml', 'i'),
    '�' : ('eth', 'e'),
    '�' : ('ntilde', 'n'),
    '�' : ('ograve', 'o'),
    '�' : ('oacute', 'o'),
    '�' : ('ocirc', 'o'),
    '�' : ('otilde', 'o'),
    '�' : ('ouml', 'o'),
    '�' : ('divide', '/'),
    '�' : ('oslash', 'o'),
    '�' : ('ugrave', 'u'),
    '�' : ('uacute', 'u'),
    '�' : ('ucirc', 'u'),
    '�' : ('uuml', 'u'),
    '�' : ('yacute', 'y'),
    '�' : ('thorn', 't'),
    '�' : ('yuml', 'y'),
    # Windows codepage 1252
    '�' : ('lsquo',"'"),
    '�' : ('rsquo',"'"),
    '�' : ('ldquo','"'),
    '�' : ('rdquo','"'),
    '�' : ('bull', '-'),
    '�' : ('ndash', '-'),
    '�' : ('mdash', '-'),
    '�' : ('tilde', '~'),
}


ent_latin1 = {
    'Agrave' : ('�', 'A'),
    'Aacute' : ('�', 'A'),
    'Acirc' : ('�', 'A'),
    'Atilde' : ('�', 'A'),
    'Auml' : ('�', 'A'),
    'Aring' : ('�', 'A'),
    'AElig' : ('�', 'A'),
    'Ccedil' : ('�', 'C'),
    'Egrave' : ('�', 'E'),
    'Eacute' : ('�', 'E'),
    'Ecirc' : ('�', 'E'),
    'Euml' : ('�', 'E'),
    'Igrave' : ('�', 'I'),
    'Iacute' : ('�', 'I'),
    'Icirc' : ('�', 'I'),
    'Iuml' : ('�', 'I'),
    'ETH' : ('�', 'E'),
    'Ntilde' : ('�', 'N'),
    'Ograve' : ('�', 'O'),
    'Oacute' : ('�', 'O'),
    'Ocirc' : ('�', 'O'),
    'Otilde' : ('�', 'O'),
    'Ouml' : ('�', 'O'),
    'times' : ('�', '*'),
    'Oslash' : ('�', 'O'),
    'Ugrave' : ('�', 'U'),
    'Uacute' : ('�', 'U'),
    'Ucirc' : ('�', 'U'),
    'Uuml' : ('�', 'U'),
    'Yacute' : ('�', 'Y'),
    'THORN' : ('�', 'T'),
    'szlig' : ('�', 's'),
    'agrave' : ('�', 'a'),
    'aacute' : ('�', 'a'),
    'acirc' : ('�', 'a'),
    'atilde' : ('�', 'a'),
    'auml' : ('�', 'a'),
    'aring' : ('�', 'a'),
    'aelig' : ('�', 'a'),
    'ccedil' : ('�', 'c'),
    'egrave' : ('�', 'e'),
    'eacute' : ('�', 'e'),
    'ecirc' : ('�', 'e'),
    'euml' : ('�', 'e'),
    'igrave' : ('�', 'i'),
    'iacute' : ('�', 'i'),
    'icirc' : ('�', 'i'),
    'iuml' : ('�', 'i'),
    'eth' : ('�', 'e'),
    'ntilde' : ('�', 'n'),
    'ograve' : ('�', 'o'),
    'oacute' : ('�', 'o'),
    'ocirc' : ('�', 'o'),
    'otilde' : ('�', 'o'),
    'ouml' : ('�', 'o'),
    'divide' : ('�', '/'),
    'oslash' : ('�', 'o'),
    'ugrave' : ('�', 'u'),
    'uacute' : ('�', 'u'),
    'ucirc' : ('�', 'u'),
    'uuml' : ('�', 'u'),
    'yacute' : ('�', 'y'),
    'thorn' : ('�', 't'),
    'yuml' : ('�', 'y'),
    # Windows codepage 1252
    'lsquo' : ('�',"'"),
    'rsquo' : ('�',"'"),
    'ldquo' : ('�','"'),
    'rdquo' : ('�','"'),
    'bull' : ('�', '-'),
    'ndash' : ('�', '-'),
    'mdash' : ('�', '-'),
    'tilde' : ('�', '~'),
}

ACENTOS_UPPER = '�������������������������������'
ACENTOS_LOWER = '�������������������������������'
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
    if find(texto, '&') == -1: #n�o existem entidades html no texto
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
    # Mascara UTF-8 valida na faixa 0x80 a 0x7FF: 110x xxab   10cd efgh
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

    cars = 'Em�lio N�O ca�a pav�es.'

    '''
    #teste_cars('B��������')
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
