import re
bestCold = ""
worstCold = ""
hotLow = coldLow = 100
hotHigh = coldHigh = hotSum = hotCount = coldCount = coldSum = 0
bestHot = ""
worstHot = ""

input = input("Enter file name: ")
fileHandle = open(input)

for line in fileHandle:
    if line.startswith("name,") : continue
    # Finds the name of the cereal
    name = re.findall("^(.+?),[AGKNPQR]", line)
    # Finds the rating of the cereal
    rating = re.findall(",([0-9.]+$)", line)
    # Finds the type of cereal
    type = re.findall(",([HC]),", line)
    print(type)

    # Determines the best and worst "cold" cereals and their respective ratings and names
    if type[0] == "C":
        coldCount = coldCount + 1
        coldSum = coldSum + float(rating[0])
        if float(rating[0]) > coldHigh:
            coldHigh = float(rating[0])
            bestCold = name[0].strip()
        if float(rating[0]) < coldLow:
            coldLow = float(rating[0])
            worstCold = name[0].strip()
    # Determines the best and worst "hot" cereals and their respective ratings and names
    else:
        hotCount = hotCount + 1
        hotSum = hotSum + float(rating[0])
        if float(rating[0]) > hotHigh:
            hotHigh = float(rating[0])
            bestHot = name[0].strip()
        if float(rating[0]) < hotLow:
            hotLow = float(rating[0])
            worstHot = name[0].strip()

hotAverage = hotSum / hotCount
coldAverage = coldSum / coldCount

print("Cereal type: Cold")
print(worstCold + " has the worst rating - ", coldLow)
print(bestCold, " have the best rating - ", coldHigh)
print("The average rating for cold cereals is ", coldAverage)
print("Cereal type: Hot")
print(worstHot + " has the worst rating - ", hotLow)
print(bestHot, " has the best rating - ", hotHigh)
print("The average rating for hot cereal is - ", hotAverage)