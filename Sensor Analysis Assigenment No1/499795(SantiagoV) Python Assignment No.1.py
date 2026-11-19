from io import StringIO
import random
import statistics
import sys
import matplotlib.pyplot as plt
import numpy as np
import csv
from PIL import Image
import time
import os
import winsound

boomerang = True


def threedotwait():
    time.sleep(.5)
    print(".")
    time.sleep(.5)
    print(".")
    time.sleep(.5)
    print(".")
    time.sleep(2)


while boomerang:
    print("Choose Sensor type, Temperature or Light")
    sensortype = input("Sensor type: ").strip().lower()

    while True:     # Only accepts temperature or light
        sensortype = input("Sensor type: ").strip().lower()

        if sensortype == "temperature" or sensortype == "light":
            print(
                f"Epic, you chose a {sensortype} sensor, now we can move on to the next grouling step...")
            threedotwait()
            print("Fill out the following information broski:")
            break  # Correctly breaks only when a valid choice is made!
        else:
            print("WTF, dude I don't recognise this shit 💔")
            print("This isn't working, I think we need to breakup. Try again bbg 💋")

    recognise = False
    boomerang = False

    while True:  # making sure that they don't mess up the min and max values
        # these shall only be intergerssss
        while True:  # this will ONLY accept strings as an input
            try:
                min_val = int(input("Choose a minimum value: "))
                break
            except ValueError:
                print("Homiesauce, give me an interger, not a string💔")
        while True:  # this will ONLY accept strings as an input
            try:
                max_val = int(input("Choose a maximum value: "))
                break
            except ValueError:
                print("Homiesauce, give me an interger, not a string💔")

        if min_val < max_val:  # max value CANNOT BE LESS THAN Min value
            break
        else:
            print("Buddy...")
            threedotwait()
            print(f"""Did you fail math?
                                                            
            Beacause last time I checked {max_val} is NOT larger than {min_val}...
            """)

    while True:  # Makes sure readings is a valid integer within your rules
        try:
            readings = int(input("Number of readings: "))

            if readings <= 0:
                print("Homie... you need at least 1 reading. Try again 💔")
            elif readings > (max_val - min_val):
                print(
                    "That is NOT POSSIBLE, like you want more readings than there is range, try again bub 💔")
            else:
                break  # Everything is valid! Exit the loop.

        except ValueError:
            print("Homiesauce, give me an integer, not a string 💔")

    while True:  # Makes sure that threashhold is valid and shit
        while True:
            try:
                thresh = int(input("Please set your alert threshold: "))
                if thresh < max_val:
                    break
                else:
                    print(
                        "Bro... your threshold can't be larger than your max value. That's not how this shit works.")
            except ValueError:
                print("Homiesauce, give me an interger, not a string💔")
        break

    random.seed(1923)
    lista = random.choices(range(min_val, max_val+1), k=readings)

    # Chat remember that min & max are FUNCIONS IN PYTHON, so don't use them as variables since they, again, ARE FUNCIONS <3
    mean = sum(lista)/readings
    lowest = min(lista)
    highest = max(lista)
    deviation = statistics.stdev(lista)
    above_thresh = sorted(i for i in lista if i >= thresh)
    # len() will return the number of items in an object (Perfect for this situation!!!) :D
    num_over_thresh = len(above_thresh)

    print(f"""

For the values that you asked for, the following is some data you may need

All values: {lista}

Mean value: {mean}
Minimium value:{lowest}
Maximium value:{highest}
Standard Deviation: {deviation}
Values above threshold: {above_thresh}
Number of values that exceed threshold: {num_over_thresh}

""")

    fig, ax = plt.subplots()
    ax.plot(lista)

    ax.set(xlabel='x', ylabel='y',
           title=f'{sensortype} sensor')
    ax.grid()

    fig, ax = plt.subplots(1)
    x = np.random.normal(lista)
    plt.hist(x)
    plt.show()
    fig.savefig("test.png")
    plt.show()

# Save the sample numbers and readings to a CSV file using the csv module
    exportfile = str(
        input("Where tf do you want your CSV? (e.g., folder_name): "))

    os.makedirs(exportfile, exist_ok=True)
    file_path = os.path.join(exportfile, "results.csv")

    # Use file_path here instead of hardcoding 'results.csv'
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write a header row for your columns
        writer.writerow(["Sample", "Reading"])

        # Loop through your list and write each sample number with its reading
        for sample_num, reading in enumerate(lista, start=1):
            writer.writerow([sample_num, reading])

    print(f"Data successfully saved to {file_path}! 📁")

    script_dir = os.path.dirname(__file__)

    img_path = os.path.join(script_dir, "8gb942.jpg")
    im = Image.open(img_path)
    im.show()

    script_dir = os.path.dirname(__file__)
    sound_path = os.path.join(script_dir, "Bazinga! Sound Effect.wav")
    winsound.PlaySound(sound_path, winsound.SND_FILENAME)

    print("Sheldon: Ahhh, I see you have fallen intro my trap...")
    time.sleep(3)
    print("Sheldon: Choose, do you wish to generate new data?")
    time.sleep(3)
    print("Sheldon: ...")
    time.sleep(3)
    print("Sheldon: Or OPEN A CSV FILE?")
    time.sleep(1)

    evil_img_path = os.path.join(
        script_dir, "evil-sheldon-cooper-v0-hveypjkj2eta1.webp")
    im = Image.open(evil_img_path)
    im.show()

    boom_path = os.path.join(script_dir, "Vine boom sound effect.wav")
    winsound.PlaySound(boom_path, winsound.SND_FILENAME)

    print("MWHAHHAHAHA")
    print("Generate or Open CSV:")
    choice = str(input("Choose "))

    if choice == "Generate":
        recognise = False
        boomerang = True
        continue
    elif choice == "Open CSV":
        print("Yippie.")
        filepath = input("Please enter the filepath of the CSV bbg: ").strip()

        readings_from_csv = []

        try:
            # Open CSV file
            with open(filepath, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    readings_from_csv.append(float(row[1]))

            print(f"Successfully loaded readings: {readings_from_csv}")

            fig, ax = plt.subplots()
            ax.plot(readings_from_csv)
            ax.set(xlabel='Sample Number', ylabel='Reading Value',
                   title='Loaded CSV Sensor Readings')
            ax.grid()
            plt.show()

        except FileNotFoundError:
            print(
                f"Oppsie, couldn't find '{filepath}'. Check your path and try againnnn.")
        except Exception as e:
            print(
                f"Oopsie woopsie! An error occurred while reading the file: {e}")
        break
