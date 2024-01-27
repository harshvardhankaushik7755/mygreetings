import json

def countryInput(country, input):
    print(f"Welcome to {country.lower()}.. a famous monument of {input.upper()}")
    
if __name__ == "__main__":
    with open("monuments.json", "r")as jsonfile:
        data = json.load(jsonfile)
        keylist = list(data.keys())
        userinput = None
        while userinput !="exit":
            userinputascountry = input()
            checkey = False
            for country in keylist:
                usercountry = userinputascountry.lower()
                if country == usercountry:
                    countryInput(data[usercountry], country)
                    checkey = True
                else:
                    pass
            if userinputascountry =="exit":
                break
            elif checkey == False:
                print("Incorrect try again")
                