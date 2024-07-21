input = input("Enter file name: ")
fileHandle = open(input)
bestCold = ""
worstCold = ""
hotLow = coldLow = 100
hotHigh = coldHigh = hotSum = hotCount = coldCount = coldSum = 0
bestHot = ""
worstHot = ""

# This line skips the first line in the file, so I can work with data I need
fileHandle.readline()

for line in fileHandle :
    # I decided to split the file line by "_" because some cereal names include commas, so I will get rid 
    # of commas in cereal names before I work with the rest of the data 
    pre_Parts = line.split("_")
    cleanLine = ""
    for link in pre_Parts:
        # This part of the code gets rid of the commas in the name of the cereals
        if link.endswith(","):
            link = link[:len(link)-1]
            # This code assembles the file line back together, but now there is no commas in cereal names
        cleanLine = cleanLine + " " + link
        # Splits file lines by "," , so I can work with the necessary data
    post_Parts = cleanLine.split(",")
    # Determines the best and worst "cold" cereals and their respective ratings and names
    if post_Parts[2] == "C":
        coldCount = coldCount + 1
        coldSum = coldSum + float(post_Parts[15])
        if float(post_Parts[15]) > coldHigh:
            coldHigh = float(post_Parts[15])
            bestCold = post_Parts[0].strip()
        if float(post_Parts[15]) < coldLow:
            coldLow = float(post_Parts[15])
            worstCold = post_Parts[0].strip()
    # Determines the best and worst "hot" cereals and their respective ratings and names
    else:
        hotCount = hotCount + 1
        hotSum = hotSum + float(post_Parts[15])
        if float(post_Parts[15]) > hotHigh:
            hotHigh = float(post_Parts[15])
            bestHot = post_Parts[0].strip()
        if float(post_Parts[15]) < hotLow:
            hotLow = float(post_Parts[15])
            worstHot = post_Parts[0].strip()

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