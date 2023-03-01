#MENU NAGUSIA, joko bakoitza funtzio baten zortuko da.
import jolasa.tribial

def MENU_NAGUSIA():
    while True:
        print("\nMENUA")
        print("======================")
        print("1 Lehenengo jokoa")#gerson 
        print("2 Tribial(Aritz)")
        print("3 Hirugarren jokoa")
        print("0- Irten")

        print("")
        aukera = int(input("Zein eragiketa egin nahi duzu? "))

        if aukera == 1:
            jokoa1()        
            break

        elif aukera == 2:
            jokoa2()
            break
        elif aukera == 3:
            jokoa3()
            break
        elif aukera == 0:
            print("ESKERRIK ASKO, AGUR!")
            exit()
            break
            
        else:
            print("SARTUTAKO AUKERA EZ DU BALIO.")

#------------------------------------------------------------------------
#GERSON
def jokoa1():
    #JOKO codea
    MENU_NAGUSIA()
#------------------------------------------------------------------------   
#ARITZ
def jokoa2():
    #JOKO codea
    jolasa.tribial.menua()
#------------------------------------------------------------------------

def jokoa3():
    #JOKO codea
    MENU_NAGUSIA()
    
#------------------------------------------------------------------------

MENU_NAGUSIA()