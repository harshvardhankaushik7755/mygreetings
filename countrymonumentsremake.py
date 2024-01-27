import json

def countryInput(country, monument):
    print(f"Welcome to {monument}.. a gem of {country}")
    
if __name__ == "__main__":
    with open("monuments.json", "r") as jsonfile:
        data = json.load(jsonfile)
        countrylist = list(data.keys())
        userinput = None
        while userinput!= "exit":
            inputascountry = input()
            checkey = False
            for country in countrylist:
                usercountry = inputascountry.lower()
                if usercountry == country:
                    countryInput(country, data[usercountry])
                    checkey = True
                else:
                    pass
            if usercountry == "exit":
                break
            elif checkey == False:
                print("Incorrect try again")
            