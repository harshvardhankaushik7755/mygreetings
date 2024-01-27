import json

def jsonfileImplementer(filename):
    with open(filename, "r") as jsonfile:
        data = json.load(jsonfile)
        countrykey = data.keys()
        countrylist = list(countrykey)
        return data, countrylist

def countryInput(country, headofnation):
    print(f"{country.capitalize()}'s head of nation is {headofnation}")
    
if __name__ == "__main__":
    print("Enter a country's name I will tell it's head of that nation")
    data, countrylist = jsonfileImplementer("headofnations.json")
    userinput = None
    while userinput != "exit":
            inputascountry = input()
            checkey = False
            for country in countrylist:
                inputcountry = inputascountry.lower()
                if inputcountry == country:
                    countryInput(country, data[inputcountry])
                    checkey = True
                else:
                    pass
            if inputcountry == "exit":
                break
            elif checkey == False:
                print("Incorrect try again") 
           
            