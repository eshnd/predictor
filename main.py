import narwhal
import sage
import json
import os
import time

os.system("clear")

DATA = "data.json"

# so this is basically gonna get input features from user and then use data from file to eval results

action = input("What stock do you want to test? ")

if os.path.exists(DATA):
    with open(DATA, "r") as f:
        existing_data = json.load(f)
    prediction = narwhal.narwhal([sage.get_price(action), sage.get_market_cap(action), sage.get_market_open(action), sage.get_time()], existing_data)
    print("NARwhaL prediction: " + str(prediction))
    record = input("Do you want to record results? (y/n) ")
    if record == "y":
        length = float(input("How long do you want to wait before recording (minutes)? "))
        time.sleep(length*60)
        grade = float(input("How would you grade this stock out of 100? "))
        existing_data.append([price, mktcap, mktopn, minsmid, prediction, grade])
        with open(DATA, "w") as f:
            json.dump(existing_data, f)
else:
    log_stuff = input("No data found?? Do you want to log data? (y/n) ")
    if log_stuff == "y":
        num_logs = int(input("How many datapoints do you want to log? "))
        for i in range(num_logs):
            price = float(input("Price: "))
            mktcap = float(input("Market Cap: "))
            mktopn = float(input("Market Open: "))
            minsmid = float(input("Minutes Since Day Started (360 for 6:00 AM): "))
            pred = float(input("How much was the prediction? "))
            out = float(input("How would you grade the prediction accuracy out of 100? "))
            if os.path.exists(DATA):
                with open(DATA, "r") as f:
                    existing_data = json.load(f)
                existing_data.append([price, mktcap, mktopn, minsmid, pred, out])
                with open(DATA, "w") as f:
                    json.dump(existing_data, f)
            else:
                with open(DATA, "w") as f:
                    json.dump([[price, mktcap, mktopn, minsmid, pred, out]], f)
