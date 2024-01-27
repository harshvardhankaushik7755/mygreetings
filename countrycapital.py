import json


def countryInput(input):
    print(input)
    
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
                    countryInput(data[usercountry])
                    checkey = True
                else:
                    pass
            if userinputascountry == "exit":
                break
            elif checkey == False:
                print("Incorrect try again")
