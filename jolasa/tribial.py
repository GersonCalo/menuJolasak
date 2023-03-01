import project

def artes():
    puntuak = 0
    print("********************************************************************************")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                              ARTEAK GALDETEGIA                               *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("* Ondo erantzun dako galdera bakoitza 10 puntu eta gaizki erantzundakoak -5\n  *")
    print("********************************************************************************")
    #1.galdera
    print("1.Nola du izena belarria moztu zuen margolariak? ")
    print("a) Henri de Toulouse-Lautrec")
    print("b) Paul Cézanne")
    print("c) Salvador Dalí")
    print("d) Vicent van gogh.")

    erantzuna = input("Sartu erantzuna: ")

    if erantzuna.lower() == "d":
        print("Erantzuna ondo sartu duzu")
        puntuak += 10
    else:
        print("Gaixki erantzun duzu")
        puntuak -= 5

    #2.galdera
    print("\n2.Horietako nor EZ zen izan muralista mexikar bat?")
    print("a) Pedro Lira.")
    print("b) Diego Rivera")
    print("c) David Alfaro Siqueiros")
    print("d) Jose Clemente Orozco")

    erantzuna = input("Sartu erantzuna: ")

    if erantzuna.lower() == "a":
        print("Erantzuna ondo sartu duzu")
        puntuak += 10
    else:
        print("Gaixki erantzun duzu")
        puntuak -= 5

    #3.galdera
    print("\n3.Nork margotu zuen \"Guernica\"")
    print("a) M. C. Escher")
    print("b) Diego Rivera")
    print("c) Pablo Picasso.")
    print("d) Henri Matisse")

    erantzuna = input("Sartu erantzuna: ")

    if erantzuna.lower() == "c":
        print("Erantzuna ondo sartu duzu")
        puntuak += 10
    else:
        print("Gaixki erantzun duzu")
        puntuak -= 5
        
    #4.galdera
    print("\n4.Artista hauetako nor ez zen Espainiakoa?")
    print("a) El Greco")
    print("b) Rufino Tamayo.")
    print("c) Pablo Picasso")
    print("d) Remedios Varo")

    erantzuna = input("Sartu erantzuna: ")

    if erantzuna.lower() == "b":
        print("Erantzuna ondo sartu duzu")
        puntuak += 10
    else:
        print("Gaixki erantzun duzu")
        puntuak -= 5

    #5.galdera
    print("\n5.Horietako nor ez zen izan margolari ospetsu bat?")
    print("a) Leonora Carrington")
    print("b) Remedios Varo")
    print("c) Frida Kahlo")
    print("d) Virginia Woolf.")

    erantzuna = input("Sartu erantzuna: ")

    if erantzuna.lower() == "d":
        print("Erantzuna ondo sartu duzu")
        puntuak += 10
    else:
        print("Gaixki erantzun duzu")
        puntuak -= 5

    print("Lortutako puntuak: ", puntuak)
def Zientziak():
    puntuak = 0
    print("********************************************************************************")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                           ZIENTZIAK GALDETEGIA                               *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("* Ondo erantzun dako galdera bakoitza 10 puntu eta gaizki erantzundakoak -5\n  *")
    print("********************************************************************************")
    
    #1.Galdera
    print("\n1.Zer izen du altueraren beldurrak?")
    print("a) Akrofobia.")
    print("b) Tanatofobia")
    print("c) Hipokondria")
    print("d) Niktofobia")

    erantzuna = input("Sartu erantzuna: ")

    if erantzuna.lower() == "a":
        print("Erantzuna ondo sartu duzu")
        puntuak += 10
    else:
        print("Gaixki erantzun duzu")
        puntuak -= 5
    #2.galdera
    print("Zein da argiaren abiadura?(kilometro segunduko)")
    aukerak = 0
    argia = 300000
    
    while aukerak < 5:
        galdera = int(input("Sartu erantzuna: "))
        if galdera == argia:
            print("Ondo erantzun duzu")
            puntuak += 10
            break
        elif galdera > argia:
            print ("Erantzuna txikiagoa da")
        else:
            print("Erantzuna handiagoa da")
            aukerak += 1
    else:
        print("Barkatu, zure 5 saiakerak agortu dituzu. Erantzuna: ", argia)
    #3.galdera
    print("\n3.Zer zientzia ikasten du odolak?")
    print("a) Hematologia.")
    print("b) kosmologia")
    print("c) neurozientzia")
    print("d) osteologia")

    erantzuna = input("Sartu erantzuna: ")

    if erantzuna.lower() == "a":
        print("Erantzuna ondo sartu duzu")
        puntuak += 10
    else:
        print("Gaixki erantzun duzu")
        puntuak -= 5
    #4.galdera
    print("Zenbat elementu ditu taula periodikoak?")
    aukerak = 0
    tabla = 118
    
    while aukerak < 3:
        galdera = int(input("Sartu erantzuna: "))
        if galdera == tabla:
            print("Ondo erantzun duzu")
            puntuak += 10
            break
        elif galdera > tabla:
            print ("Erantzuna txikiagoa da")
        else:
            print("Erantzuna handiagoa da")
            aukerak += 1
    else:
        print("Barkatu, zure 3 saiakerak agortu dituzu. Erantzuna: ", tabla)
    #5.galdera
    print("Zein hilabetetan dago eguzkia Lurretik hurbilen?")
    
    erantzuna = input("Sartu zure erantzuna: ")

    if erantzuna.lower() == "abendua":
        print("Erantzuna ondo sartu duzu")
        puntuak += 10
    else:
        print("Sartu duzun erantzuna gaizki dago -5 puntu")
        puntuak -= 0
    
    print("Lortutako puntuak hauek dira: ", puntuak)
def kirolak():
    puntuak = 0
    print("********************************************************************************")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                           KIROLAK  GALDETEGIA                                *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("* Ondo erantzun dako galdera bakoitza 10 puntu eta gaizki erantzundakoak -5\n  *")
    print("********************************************************************************")
    #1.galdera
    print("\n1.Noiz ospatu zen lehen munduko futbol txapelketa?")
    print("a) 1928ko apirilaren 16an")
    print("b) 1930eko uztailaren 13an.")
    print("c) 1933ko urtarrilaren 28an")
    print("d) 1935eko urtarrilaren 2an")

    erantzuna = input("Sartu erantzuna: ")

    if erantzuna.lower() == "b":
        print("Erantzuna ondo sartu duzu")
        puntuak += 10
    else:
        print("Gaixki erantzun duzu")
        puntuak -= 5
    #2.galdera
    print("\n2.Zenbat kilometroko distantzia du maratoi batek?")
    print("a) 41.85 km")
    print("b) 42.16 km.")
    print("c) 43.77 km")
    print("d) 43.45 km")

    erantzuna = input("Sartu erantzuna: ")

    if erantzuna.lower() == "b":
        print("Erantzuna ondo sartu duzu")
        puntuak += 10
    else:
        print("Gaixki erantzun duzu")
        puntuak -= 5
    #3.galdera
    print("\n3.Zeintzuk dira Joko Olinpikoetako eraztunaren bost koloreak?")
    print("a) Urdina, gorria, horia, berdea eta beltza.")
    print("b) Urdina, gorria, horia, berdea eta morea")
    print("c) horia, gorria, morea, berdea eta beltza")
    print("d) Urdina, gorria, horia, laranja eta berdea")

    erantzuna = input("Sartu erantzuna: ")

    if erantzuna.lower() == "a":
        print("Erantzuna ondo sartu duzu")
        puntuak += 10
    else:
        print("Gaixki erantzun duzu")
        puntuak -= 5
    #4.galdera
    print("\n4.\"Manny Pacquiao\" zein herrialdetako boxeolari mitikoa da?")
    print("a) Corea")
    print("b) Filipinas.")
    print("c) China")
    print("d) México")

    erantzuna = input("Sartu erantzuna: ")

    if erantzuna.lower() == "b":
        print("Erantzuna ondo sartu duzu")
        puntuak += 10
    else:
        print("Gaixki erantzun duzu")
        puntuak -= 5
    #5.galdera
    print("enbat aldiz irabazi zituen Michael Jordanek txapelketak Chicago Bullsentzat?")
    aukerak = 0
    kopak = 6
    
    while aukerak < 3:
        galdera = int(input("Sartu erantzuna: "))
        if galdera == kopak:
            print("Ondo erantzun duzu")
            puntuak += 10
            break
        elif galdera > kopak:
            print ("Erantzuna txikiagoa da")
        else:
            print("Erantzuna handiagoa da")
            aukerak += 1
    print("Lortutako puntuak hauek dira: ", puntuak)
def geografia():
    puntuak = 0
    print("********************************************************************************")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                           GEOGRAFIA  GALDETEGIA                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("* Ondo erantzun dako galdera bakoitza 10 puntu eta gaizki erantzundakoak -5    *")
    print("********************************************************************************")
    
    #1.galdera
    print("\n1.Zein da Iberiar Penintsulako ibairik luzeena?(3 aukera dituzu gaixki egindako bakoitzean -2 puntu)")
    aukerak = 0

    while aukerak < 3:
        galdera = input("Sartu erantzuna: ")
        if galdera.lower() == "tajo":
            print("Ondo erantzun duzu")
            puntuak += 10
            break
        else:
            print("erantzuna gaixki dago")
            aukerak += 1
            puntuak -= 2
    #2.galdera
    print("\n2.Zenbat ozeano daude Lurrean?")
    aukerak = 0
    ozeanoak = 5
    
    while aukerak < 3:
        galdera = int(input("Sartu erantzuna: "))
        if galdera == ozeanoak:
            print("Ondo erantzun duzu")
            puntuak += 10
            break
        elif galdera > ozeanoak:
            print ("Erantzuna txikiagoa da")
        else:
            print("Erantzuna handiagoa da")
            aukerak += 1
    #3.galdera
    print("Zein herrialdek ez du ibairik?(erantzun bat baino gehiago daude)")
    aukerak = 0
    
    while aukerak < 5:
        galdera = input("Sartu zure erantzuna: ")
        if galdera.lower() == "malta":
            print("Ondo erantzun duzu")
            puntuak += 10
            break
        elif galdera.lower() == "qatar":
            print("Ondo erantzun duzu")
            puntuak += 10
            break
        elif galdera.lower() == "tuvalu":
            print("Ondo erantzun duzu")
            puntuak += 10
            break
        elif galdera.lower() == "comoras":
            print("Ondo erantzun duzu")
            puntuak += 10
            break
        else:
            print("Sartu berriro")
            aukerak += 1
    #4.galdera
    print("\n4.Zein herrialdetan hitz egiten dira hizkuntza gehiago?")
    print("a) Papúa Nueva Guinea.")
    print("b) uzbekistan")
    print("c) Timor Oriental")
    print("d) Suriname")

    erantzuna = input("Sartu erantzuna: ")

    if erantzuna.lower() == "a":
        print("Erantzuna ondo sartu duzu")
        puntuak += 10
    else:
        print("Gaixki erantzun duzu")
        puntuak -= 5
    #5.galdera
    print("\n5.Zer ibai igarotzen da herrialde gehiagotara?")
    print("a) El Danubio.")
    print("b) Amazonas ")
    print("c) Río Yeniséi")
    print("d) Rio Obi")

    erantzuna = input("Sartu erantzuna: ")

    if erantzuna.lower() == "a":
        print("Erantzuna ondo sartu duzu")
        puntuak += 10
    else:
        print("Gaixki erantzun duzu")
        puntuak -= 5
    print("Lortutako puntuak hauek dira: ", puntuak)
def historia():
    puntuak = 0
    print("********************************************************************************")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                           HISTORIA   GALDETEGIA                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("* Ondo erantzun dako galdera bakoitza 10 puntu eta gaizki erantzundakoak -5    *")
    print("********************************************************************************")
    
    #1.galdera
    print("1.Zenbat iraun zuen Ehun Urteko Gerrak?")
    aukerak = 0
    tabla = 116
    
    while aukerak < 3:
        galdera = int(input("Sartu erantzuna: "))
        if galdera == tabla:
            print("Ondo erantzun duzu")
            puntuak += 10
            break
        elif galdera > tabla:
            print ("Erantzuna txikiagoa da")
        else:
            print("Erantzuna handiagoa da")
            aukerak += 1
    #2.galdera
    print("2.Zein urtetan desegin zen Sobietar Batasuna?")
    aukerak = 0
    urtea = 1991
    
    while aukerak < 3:
        galdera = int(input("Sartu erantzuna: "))
        if galdera == urtea:
            print("Ondo erantzun duzu")
            puntuak += 10
            break
        elif galdera > urtea:
            print ("Erantzuna txikiagoa da")
        else:
            print("Erantzuna handiagoa da")
            aukerak += 1
    #3.galdera
    print("\n3.Zein hiritan bildu ziren Hitler eta Franco?")
    print("a) Colonia")
    print("b) Nantes")
    print("c) Madrid")
    print("d) hendaia.")

    erantzuna = input("Sartu erantzuna: ")

    if erantzuna.lower() == "d":
        print("Erantzuna ondo sartu duzu")
        puntuak += 10
    else:
        print("Gaixki erantzun duzu")
        puntuak -= 5
        
    #4.galdera
    print("4.Zenbat iraun zuen Espainiako Bigarren Errepublikak?")
    aukerak = 0
    urtea = 8
    
    while aukerak < 3:
        galdera = int(input("Sartu erantzuna: "))
        if galdera == tabla:
            print("Ondo erantzun duzu")
            puntuak += 10
            break
        elif galdera > tabla:
            print ("Erantzuna txikiagoa da")
        else:
            print("Erantzuna handiagoa da")
            aukerak += 1
    print("Lortutako puntuak hauek dira: ", puntuak)

def menua():
    bukle = True
    while(bukle):

        print("**********************************************")
        print("*  1.artes                                   *")
        print("*  2.Zientziak                               *")
        print("*  3.Kirolak                                 *")
        print("*  4.geografia                               *")
        print("*  5.historia                                *")
        print("*  0.MENUTIK IRTETZEKO                       *")
        print("**********************************************")

        menukoznb = int(input("Sartu zenbaki bat: "))


        if menukoznb == 1:
            artes()
        elif menukoznb == 2:
            Zientziak()
        elif menukoznb == 3:
            kirolak()
        elif menukoznb == 4:
            geografia()
        elif menukoznb == 5:
            historia()
        if menukoznb == 0:
            bukle = False
            print("Eskerrik asko menu hau ikusteagatik") 
            project.MENU_NAGUSIA()   
        else:
            print("Sartu berriz zenbakia")

