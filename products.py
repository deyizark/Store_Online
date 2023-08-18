pwodui = [{"name":"Jeep Wrangler","price": 300_000,"quantity":2},
          {"name":"Hummer","price":330_000,"quantity":1},
          {"name":"Lamborghini Verona","price":500_000,"quantity":4}]

def afiche_pwodui():
    i = 1
    for pwod in pwodui:
        print(f"Pwodui nimewo {i}")
        print("===========")
        for end, vale in pwod.items():
            print(f"{end} : {vale}")
        print("===========")
        i += 1