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

hitzak = "pepe españa boloñesa bernardo patxikito peregrino aguacil ermenegildo berberecho tataratatarabuelo bogota bmw tetera kilobyte jacobo jamon balcanico trambolico berenjena franco".split()
#hitz hauek erabiliko ditugu ahorcadoan
def auzazkoHitzaHautatu(hitzenLista):
    #auzazko hitz bat bueltatuko digu funtzio honek
    auzazkoHitza = random.randint(0, len(hitzenLista) - 1)
    return hitzenLista[auzazkoHitza]

def erakutziJokoa(AHORCADO, izkiaEzdago, izkiaBadago, hitzSekretua):
    print(AHORCADO[len(izkiaEzdago)])
    print("")
    amaiera = ""
    print ("Ez dauden izkiak:",amaiera)
    for izkia in izkiaEzdago:
        print(izkia, amaiera)
    print("")
    hutsuneak = "_" * len(hitzSekretua)
    for i in range(len(hitzSekretua)): 
    #Emen hutsuneak ongi dauden izkiengaitik aldatzen dira
        if hitzSekretua[i] in izkiaBadago:
            hutsuneak = hutsuneak[:i] + hitzSekretua[i] + hutsuneak[i+1:]
        for izkia in hutsuneak: 
        #Hitz seketutua izkien arteen hustuneekin erakusten du
            print(izkia,amaiera)
        print("")
    
    def izkiaHautatu(izkiBat):
        #Emen izkia esanda dagoen ala egokia dela komprobatzen dugu
        while True :
            print("Sartui izki bat:")
            izkia = input()
            izkia = izkia.lower()
            if len(izkia) != 1:
                print ("Sartu izki bat bakarrik")
            elif izkia in izkiBat:
                print ("Izki hori lehenagotik esana duzu. Saiatu berri batekin!")
            elif izkia not in "abcdefghijklmnopqrstuvwxyz":
                print ("Hori ez da izki bat!")
            else:
                return izkia