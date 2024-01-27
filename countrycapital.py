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
                if country == userinputascountry:
                    countryInput(data[userinputascountry])
                    checkey = True
                else:
                    pass
            if userinputascountry == "exit":
                break
            elif checkey == False:
                print("Incorrect try again")
