import re
import csv

class day:
    """A day contains information about that particular (numerical) day (i.e 'day_1' and 'day_230')

    Atributes:
        Date:  a string of the date "30-Apr"
        Day:  a string of the day "Monday"
        Temp-Range (°F):  a tuple storing the recorded high and low temps (low, high)
        Precipitation (inches):  a tuple of a float [and a qualifier if it exists] (inches, [qualifier like 'T'])
        Bridge: a dictionary. key:val = name_of_bridge:num_commuters
        Total: total float given by data (which is USUALLY equal to sum of all commuters from each bridge)
        """

    def __init__(self, data):
        self.labels = self.constructLabels(data)
        self.date = data[0]
        self.day = data[1]
        self.temp = (float(data[2]), float(data[3]))
        self.precipitation = self.addPrecitipation(data)
        self.bridge = self.addBridges(data)
        self.total = data[9]

    def constructLabels(self, data):
        return [x for x in data]

    def addPrecitipation(self, data):
        precipitation_string = str(data[4])  # we need to format this string
        mo1 = re.match(r"(\d+\.\d+)", precipitation_string) # match object 1
        mo2 = re.match(r"(\(\w?)?([A-Z])(\))?", precipitation_string) # match object 2
        if mo1 is mo2 and mo1 is None:
            qualifier = "Error"
            inches = -9999
        elif mo1 is None:
            qualifier = mo2.string
            inches = 0
        elif mo2 is None:
            qualifier = None
            inches = float(mo1.string)
        else:
            qualifier = mo2.string
            inches = float(mo1.string)

        return (inches, qualifier)

    def addBridges(self, data):
        bridge_dict = {}
        string_data = str(data)
        bridge_list = re.findall(r"[A-Z](\w+)(\s)?[b|B]ridge", string_data) # find number of word bridge
        iterat = 0
        for bridge in bridge_list:
            self.bridge.update({bridge : data[iterat]})
            iterat += 1
        return bridge_dict

    @property
    def __str__(self):
        return f"{self.date}"

    def __repr__(self):
        return "Day Object"

    def format(self):
        print(f"{self.labels}")

    def printDay(self):
        print(f"{self.date}, {self.day}, ({self.temp[0]}, {self.temp[1]}), {self.bridge}, {self.total}")

if __name__ == "__main__":
    with open('NYC_Bicycle_Counts_2016_Corrected.csv') as csvfile:
        i = 0
        arrayData = []
        readObject = csv.reader(csvfile)

        for row in readObject:
            arrayData.append(list(readObject))

            #arrayData.append(day(row))
            #arrayData[i].printDay()
            #print(arrayData)
            #i+=1

        print(arrayData[0])