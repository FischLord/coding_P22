schallter = True
line = "#######################################"

#Fixksten der Firma
start_duration = 53 #minuten
cost_per_hour = 5913 #dollar
rental_cost = start_duration/60 * cost_per_hour
#Kosten per Quality
quality_additional_price = [16,12,10,8,6,5,4.5,4,3.5,3,2.5,2,1.5]

def space(x):
 for x in range(x):
     print()


while schallter == True:
    print(line)
    print("Welcome to the 'Lounchpad Rental' Service by 'Fischzentrale'")
    print("This Phyton Script will calculate the cost")
    print("The calculation behind my service is that, you send me the rocket for an Price")
    print("I will add the launch cost to it ad devide it into the ASR the rocket generates")
    print("Then i will add a additional price per ASR, based on the Quality of the rocket, duo there is an chance of failure")
    print(line)
    space(2)

    print("Please input the type of rocket you want to launch.")
    abfrage = False
    while not abfrage == True:
        rocket_type = str(input("SOR/1  or  BFR/2 --> "))
        if rocket_type == "SOR" or rocket_type == "BFR" or rocket_type == "1" or rocket_type == "2":
            abfrage = True
            space(2)
            if rocket_type == "1":
                rocket_type == "SOR"
            elif rocket_type == "2":
                rocket_type == "BFR"
        else:
            print("Please input 'SOR' or 'BFR'!")
            space(1)
        if rocket_type == "BFR":
            asr_amount = 2800
        elif rocket_type == "SOR":
            asr_amount = 400

    print("Which Quality does your",rocket_type,"have?")
    abfrage = False
    while not abfrage == True:
        rocket_quality = int(input("Quality 2/3/4/... --> "))
        try:
            rocket_quality =int(rocket_quality)
        except ValueError:
            print("Please input a Number!")
        else:
            if rocket_quality > 13 or rocket_quality < 0:
                print("Please input an Quality in range of 0-12")
        abfrage = True
        rocket_quality = int(rocket_quality)
        quality_price = quality_additional_price[rocket_quality]

    print("Which price you are able to sell your",rocket_type,"at?")
    print("#####  Hint normal prices are: SOR 100.000$ -- BFR 800.000$  #####")
    abfrage = False
    while not abfrage == True:
        rocket_price = input("Price --> ")
        try:
            rocket_price = int(rocket_price)
        except ValueError:
            print("Please input a Number!")
        else:
            if rocket_price <= 0:
                print("Please input an Number above 0$")
        abfrage = True
    #Rechnung
    cost_per_rocket = rocket_price + rental_cost
    asr_end_price = cost_per_rocket / asr_amount + quality_price
    print("You will get",asr_amount,"ASR, at",asr_end_price,"$ per unit.")
    