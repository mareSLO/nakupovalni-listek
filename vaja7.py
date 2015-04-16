# -*- coding: UTF-8 -*-
listek = []
odgovor = "fgc"
while odgovor != "ne":
    odgovor = raw_input("zelis dodat izdelek (da/ne)")
    if odgovor == "da":
        item = raw_input("Dodaj izdelek: ")
        listek.append(item)


    elif odgovor == "ne":
        print("Hvala za nakup")
        for x in listek:
            print(x)

    else:
        print ("Poskusi z da/ne")









