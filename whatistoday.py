import json

def occasionOfDay(input):
    print(input)   

        
if __name__ == "__main__":
    with open("occasion.json", "r") as jsonfile:
        data = json.load(jsonfile)
        keylist = list(data.keys())
        # print(keylist)
    # print(data)
    userinput = None
    while userinput!="exit":
        userdate = input()
        checkey = False
        for key in keylist:
            if key == userdate:
                occasionOfDay(data[userdate])
                checkey = True
            else:
                pass
            
        if userdate=="exit":
            break
        elif (checkey == False):
            print("Incorrect try again.")
        