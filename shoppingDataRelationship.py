#Zack Barnett 11621044

def processData():
    with open('.//browsing-data.txt', 'r') as browsingData:
        outfile = open('.//outfile.txt', 'w')
        line = browsingData.readline()

        #part a variables
        firstPassDict = {}          #contains all individual items as keys and the number of times they appear as their value
        secondPassDict = {}         #contains (item1, item2) as a key and the number of times they appear as their value
        confidenceDict = {}         #contains confidence as a key and (item1, item2) as values meaning item1 -> item2 
        topFiveConfidence = {}      #contains top five pairs and confidence values
        topFiveScores = [0,0,0,0,0] #contains top five confidence values
        itemsAboveSupport = []      #contains all individual items above support threshold
        pairsAboveSupport = []      #contains all pairs above support threshold

        #part b variables
        tripleCountDict = {}                #contains (item1, item2, item3) as keys and count as value
        tripleConfidenceDict = {}           #contains confidence as a key and (item1, item2, item3) as values meaning item1 & item2 -> item3 
        topFiveTripleConfidence = {}        #contains top five triples and confidence values
        topFiveTripleScores = [0,0,0,0,0]   #contains top five confidence values of triples 
        triplesAboveSupport = []            #contains all tripples above support threshold

        while line: 
            lineArray = line.split(' ')
            lineArray.pop()
            for items in lineArray:
                if items in firstPassDict:
                    firstPassDict[items] += 1
                else:
                    firstPassDict[items] = 1
            
            #outfile.write(str(lineArray)+ "\n")

            line = browsingData.readline()
        #outfile.write(str(firstPassDict))
        for items, count in firstPassDict.items():
            if count >= 100:
                itemsAboveSupport.append(items)

        #outfile.write(str(itemsAboveSupport))
        browsingData.seek(0, 0)
        line = browsingData.readline()
        while line:
            lineArray = line.split(' ')
            lineArray.pop()
            for i in range(len(itemsAboveSupport)):
                if itemsAboveSupport[i] in lineArray:
                    for j in range(i+1, len(itemsAboveSupport)):
                        if itemsAboveSupport[j] in lineArray:
                            if (itemsAboveSupport[i], itemsAboveSupport[j]) in secondPassDict:
                                secondPassDict[(itemsAboveSupport[i], itemsAboveSupport[j])] += 1
                            else:
                                secondPassDict[(itemsAboveSupport[i], itemsAboveSupport[j])] = 1

            line = browsingData.readline()
        for pairs, count in secondPassDict.items():
            if count >= 100:
                pairsAboveSupport.append(pairs)
        #outfile.write(str(pairsAboveSupport))
        for pairs in pairsAboveSupport:
            item1 = pairs[0]
            item2 = pairs[1]
            item1TotalCount = firstPassDict[item1]
            item2TotalCount = firstPassDict[item2]
            pairCount = secondPassDict[pairs]
            confidenceDict[round(pairCount/item1TotalCount, 4)] = (item1, item2)
            confidenceDict[round(pairCount/item2TotalCount, 4)] = (item2, item1)

        for confidence, pair in confidenceDict.items():
            if confidence > topFiveScores[0]:
                topFiveScores[4] = topFiveScores[3]
                topFiveScores[3] = topFiveScores[2]
                topFiveScores[2] = topFiveScores[1]
                topFiveScores[1] = topFiveScores[0]
                topFiveScores[0] = confidence
            elif confidence > topFiveScores[1]:
                topFiveScores[4] = topFiveScores[3]
                topFiveScores[3] = topFiveScores[2]
                topFiveScores[2] = topFiveScores[1]
                topFiveScores[1] = confidence
            elif confidence > topFiveScores[2]:
                topFiveScores[4] = topFiveScores[3]
                topFiveScores[3] = topFiveScores[2]
                topFiveScores[2] = confidence
            elif confidence > topFiveScores[3]:
                topFiveScores[4] = topFiveScores[3]
                topFiveScores[3] = confidence
            elif confidence > topFiveScores[4]:
                topFiveScores[4] = confidence

        for items in topFiveScores:
            topFiveConfidence[confidenceDict[items]] = items

        outfile.write("OUTPUT A\n")
        for pair, value in topFiveConfidence.items():
            outfile.write(pair[0] + " " + pair[1] + " " + str(value))
            outfile.write("\n")

        ############################################# part B ###############################################

        browsingData.seek(0,0)
        line = browsingData.readline()
        while line:
            lineArray = line.split(' ')
            lineArray.pop()

            for i in range(len(itemsAboveSupport)):
                if itemsAboveSupport[i] in lineArray:
                    for j in range(i+1, len(itemsAboveSupport)):
                        if itemsAboveSupport[j] in lineArray:
                            for k in range(j+1, len(itemsAboveSupport)):
                                if itemsAboveSupport[k] in lineArray:
                                    if (itemsAboveSupport[i], itemsAboveSupport[j], itemsAboveSupport[k]) in tripleCountDict:
                                        tripleCountDict[(itemsAboveSupport[i], itemsAboveSupport[j], itemsAboveSupport[k])] += 1
                                    else:
                                        tripleCountDict[(itemsAboveSupport[i], itemsAboveSupport[j], itemsAboveSupport[k])] = 1
            
            line = browsingData.readline()
        for triples, count in tripleCountDict.items():
            if count >= 100:
                triplesAboveSupport.append(triples)
        for triples in triplesAboveSupport:
            item1 = triples[0]
            item2 = triples[1]
            item3 = triples[2]
            item1TotalCount = firstPassDict[item1]
            item2TotalCount = firstPassDict[item2]
            item3TotalCount = firstPassDict[item3]
            tripleCount = tripleCountDict[triples]

            tripleConfidenceDict[round(tripleCount/item1TotalCount, 4)] = (item2, item3, item1)
            tripleConfidenceDict[round(tripleCount/item2TotalCount, 4)] = (item1, item3, item2)
            tripleConfidenceDict[round(tripleCount/item3TotalCount, 4)] = (item1, item2, item3)

        for confidence, triple in tripleConfidenceDict.items():
            if confidence > topFiveTripleScores[0]:
                topFiveTripleScores[4] = topFiveTripleScores[3]
                topFiveTripleScores[3] = topFiveTripleScores[2]
                topFiveTripleScores[2] = topFiveTripleScores[1]
                topFiveTripleScores[1] = topFiveTripleScores[0]
                topFiveTripleScores[0] = confidence
            elif confidence > topFiveTripleScores[1]:
                topFiveTripleScores[4] = topFiveTripleScores[3]
                topFiveTripleScores[3] = topFiveTripleScores[2]
                topFiveTripleScores[2] = topFiveTripleScores[1]
                topFiveTripleScores[1] = confidence
            elif confidence > topFiveTripleScores[2]:
                topFiveTripleScores[4] = topFiveTripleScores[3]
                topFiveTripleScores[3] = topFiveTripleScores[2]
                topFiveTripleScores[2] = confidence
            elif confidence > topFiveTripleScores[3]:
                topFiveTripleScores[4] = topFiveTripleScores[3]
                topFiveTripleScores[3] = confidence
            elif confidence > topFiveTripleScores[4]:
                topFiveTripleScores[4] = confidence


        for item in topFiveTripleScores:
            topFiveTripleConfidence[tripleConfidenceDict[item]] = item
        outfile.write("OUTPUT B\n")
        for triple, value in topFiveTripleConfidence.items():
            outfile.write(triple[0] + " " + triple[1] + " " + triple[2] + " " + str(value))
            outfile.write("\n")


    browsingData.close()
    outfile.close()

if __name__ == "__main__":
    processData()