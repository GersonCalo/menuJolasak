import random
aukerak = ["harria", "papera", "guraizak"]
ordenagailua = random.choice(aukerak)
pertzona = False
ordenagailua_puntuak = 0
pertzonan_puntuak = 0
while True:
    pertzona = input("harria, papera edo   guraizak?")
    if pertzona == ordenagailua:
        print("Empate!")
    elif pertzona == 'harria':
        if ordenagailua == "papera":
            print("Galdu egin duzu!", ordenagailua, "biltzen du", pertzona)
            ordenagailua_puntuak+=1
        else:
            print("Irabazi egin duzu!", pertzona, "apurtzen du", ordenagailua)
            pertzonan_puntuak+=1
    elif pertzona == "papera":
        if ordenagailua == "guraizak":
            print("Galdu egin duzu!", ordenagailua, "mozten du", pertzona)
            ordenagailua_puntuak+=1
        else:
            print("Irabazi egin duzu!", pertzona, "biltzen du", ordenagailua)
            pertzonan_puntuak+=1
    elif pertzona == "guraizak":
        if ordenagailua == "harria":
            print("Galdu egin duzu...", ordenagailua, "apurtzen du", pertzona)
            ordenagailua_puntuak+=1
        else:
            print("Irabazi egin duzu!", pertzona, "mozten du", ordenagailua)
            pertzonan_puntuak+=1
    elif pertzona=='E':
        print("Azken puntuazioak:")
        print(f"Ordenagailuak:{ordenagailua_puntuak}")
        print(f"Pertzona:{pertzonan_puntuak}")
        break
    else:
        print("Gaizki sartuta, saiatu berriro")
    ordenagailua = random.choice(aukerak)