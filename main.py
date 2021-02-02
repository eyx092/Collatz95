print("Loading save file...")
file = open("store.txt", "r")
counter = int(file.read())
file.close()

print("Press Control-C to quit.")
while True:
    try:
        print("Checking "+str(counter)+"... ", end="")
        number = counter
        while number != 1:
            if number % 2 == 0:
                number /= 2
            elif number % 2 == 1:
                number = number * 3 + 1
        print("Done. ")
        counter += 1
    except KeyboardInterrupt:
        break


print("Saving data... ",end="")
file = open("store.txt", "w")
file.write(str(counter))
file.close()
print("Done.")