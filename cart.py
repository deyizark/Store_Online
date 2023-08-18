panye_vid = []

from products import pwodui
#from main import kantite

# lis_av = ["Jeep Wrangler","Hummer", "Lamborghini Verona"]

# choix = input("Ekri non w pwodui w chwazi a : ")
# while choix not in lis_av:
#     choix = input("Byen ekri non w pwodui w chwazi a : ")

# kantite = input("Konbyen wap achte : ")
# while not kantite.isdigit():
#     kantite = input("Konbyen wap achte : ")
# kantite = int(kantite)

def ajoute_panye(a, kantit):
    lis = []
    for i in pwodui:
        lis.append(i["name"])
    end = lis.index(a) 
    panye_vid.append({"name" : a, "price" : pwodui[end]["price"],"quantity" : kantit})

#ajoute_panye("Jeep Wrangler")

def total():
    l = 1
    for k in panye_vid:
        print(f"Pwodui nimewo {l}")
        print("===========")
        for end, vale in k.items():
            print(f"{end} : {vale}")
        print("===========")
        l += 1
    paye = []
    for i in panye_vid:
        paye.append(i["price"]*i["quantity"])
    print(f"W ap peye {sum(paye)} dola")