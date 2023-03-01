import random
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
# tupla

hitzak = ('pepe', 'españa', 'boloñesa', 'bernardo', 'patxikito', 'peregrino', 'aguacil', 'ermenegildo', 'berberecho', 'tataratatarabuelo', 'bogota', 'bmw', 'tetera', 'kilobyte', 'jacobo', 'jamon', 'balcanico', 'trambolico', 'berenjena', 'franco')
# hitz hauek erabiliko ditugu ahorcadoan
# lista

# """ 'pepe españa boloñesa bernardo patxikito peregrino aguacil ermenegildo berberecho tataratatarabuelo bogota bmw tetera kilobyte jacobo jamon balcanico trambolico berenjena franco'.split() """


def auzazkoHitzaHautatu(hitzenLista):
    # auzazko hitz bat bueltatuko digu funtzio honek
    auzazkoHitza = random.randint(0, len(hitzenLista) - 1)
    return hitzenLista[auzazkoHitza]


def erakutziJokoa(AHORCADO, izkiaEzdago, izkiaBadago, hitzSekretua):
    print(AHORCADO[len(izkiaEzdago)])
    print("")
    amaiera = ""
    print('Ez dauden izkiak:', amaiera)
    for izkia in izkiaEzdago:
        print(izkia, amaiera)
    print("")
    hutsuneak = '_' * len(hitzSekretua)
    for i in range(len(hitzSekretua)):
        # Emen hutsuneak ongi dauden izkiengaitik aldatzen dira
        if hitzSekretua[i] in izkiaBadago:
            hutsuneak = hutsuneak[:i] + hitzSekretua[i] + hutsuneak[i+1:]
    for izkia in hutsuneak:
        # Hitz seketutua izkien arteen hustuneekin erakusten du
        print(izkia, amaiera)
    print("")

def izkiaHautatu(izkiBat):
    # Emen izkia esanda dagoen ala egokia dela komprobatzen dugu
    while True:
        print('Sartui izki bat:')
        izkia = input()
        izkia = izkia.lower()
        if len(izkia) != 1:
            print('Sartu izki bat bakarrik')
        elif izkia in izkiBat:
            print('Izki hori lehenagotik esana duzu. Saiatu berri batekin!')
        elif izkia not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Hori ez da izki bat!')
        else:
            return izkia

def jokoaHasi():
    # funtzio honetan jokalariak nahi badu berriz jolastu True jasotzen du du bestela False
    print('Berriz jokatu nahi? (Bai ala Ez)')
    return input().lower().startswith('b')
    #idatzitako karaktetrea minuskulaz gorde eta idatzitakoaren lehen izkia "b" bada True bezela jasotzen du bestela False 

print('A H O R C A D O')
izkiaEzdago = ""
izkiaBadago = ""
hitzSekretua = auzazkoHitzaHautatu(hitzak)
jokuaAmaitu = False

while True:
    erakutziJokoa(AHORCADO, izkiaEzdago, izkiaBadago, hitzSekretua)
    # Jokalariak izki bat hautatzen du
    izkia = izkiaHautatu(izkiaEzdago + izkiaBadago)
    if izkia in hitzSekretua:
        izkiaBadago = izkiaBadago + izkia
        # izkia hitz sektretuan badago idatzi
        aurkitutakoIzkiak = True
        for i in range(len(hitzSekretua)):
            if hitzSekretua[i] not in izkiaBadago:
                aurkitutakoIzkiak = False
                break
        if aurkitutakoIzkiak:
            print('Oso ondo! Hitz sektretua "' +hitzSekretua+'" da! Irabazi duzu!')
            jokuaAmaitu = True
    else:
        izkiaEzdago = izkiaEzdago + izkia
        # jokalariak sartu dituen izki kopurua rebisatu eta galdu duen esan
        if len(izkiaEzdago) == len(AHORCADO)-1:
            erakutziJokoa(AHORCADO, izkiaEzdago, izkiaBadago, hitzSekretua)
            print('Izki gabe gelditu zara!\n '+str(len(izkiaEzdago)) +' izki txarrren eta '+ str(len(izkiaBadago))+' izki egokiren ondoren. Hitz sektretua "' + hitzSekretua+'" zen.')
            jokuaAmaitu = True
    # galdetu berriz jokatu nahi den
    if jokuaAmaitu:
        if jokoaHasi():
            izkiaEzdago = ""
            izkiaBadago = ""
            jokuaAmaitu = False
            hitzSekretua = auzazkoHitzaHautatu(hitzak)
        else:
            break
