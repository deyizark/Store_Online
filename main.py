import products,cart
while True:
    print("Byenvini nan store a,chwazi yon opsyon tanpri : ")
    print("1.Chache yon pwodui")
    print("2.Wè panye ak tout pri total")
    print("3.Fèmen")

    chwa = input("Ki nimewo ou chwazi : ")

    while chwa not in ["1","2","3"]:
        chwa = int(input("Ki nimewo ou chwazi : "))
    if chwa == "1":
        products.afiche_pwodui()
        antre = input("Tape 'w' si wap ajoute pwodui nan panye w oswa 'n' siw pap mete :  ").lower()
        while antre not in ["w", "n"]:
            antre = input("Tape 'w' si wap ajoute pwodui nan panye w oswa 'n' siw pap mete :  ").lower()
        if antre == "w":
            lis_av = ["Jeep Wrangler","Hummer", "Lamborghini Verona"]

            choix = input("Ekri non pwodui w chwazi a : ")
            while choix not in lis_av:
                choix = input("Byen ekri non pwodui w chwazi a : ")

            kantite = input("Konbyen wap achte : ")
            while not kantite.isdigit():
                kantite = input("Konbyen wap achte : ")
            kantite = int(kantite)
            cart.ajoute_panye(choix, kantite)
            var = True
            while var :
                antre = input("Tape 'w' si w ap mete ankò sinon 'n'").lower()
                while antre not in ["w", "n"]:
                    antre = input("Tape 'w' si w ap mete ankò sinon 'n'").lower()
                if antre == "w":
                    choix = input("Ekri non w pwodui w chwazi a : ")
                    while choix not in lis_av:
                        choix = input("Byen ekri non w pwodui w chwazi a : ")

                    kantite = input("Konbyen wap achte : ")
                    while not kantite.isdigit():
                        kantite = input("Konbyen wap achte : ")
                    kantite = int(kantite)
                    cart.ajoute_panye(choix, kantite)
                else:
                    var = False 
    elif chwa == "2":
        cart.total()
    else:
        print("Bye...")
        break