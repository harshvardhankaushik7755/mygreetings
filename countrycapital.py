import json


def countryInput(input, country):
    print(f"Welcome to {input.upper()}.. Capital of {country.upper()}..!!")
    #welcome to paris.. capital of France..!!
    #welcome to new delhi.. capital of india..!!
    
    
if __name__ == "__main__":
    with open("capitals.json", "r") as jsonfile:
        data = json.load(jsonfile)
        keylist = list(data.keys())    
        userinput = None
        while userinput!="exit":
            userinputascountry = input()
            checkey = False
            for country in keylist:
                usercountry = userinputascountry.lower()
                if country == usercountry:
                    countryInput(data[usercountry],country)
                    checkey = True
                else:
                    pass
            if userinputascountry == "exit":
                break
            elif checkey == False:
                print("Incorrect try again")
