class EvenOdd:

    def printEvenNumber(self, startIndex, endIndex):
        for index in range(startIndex, endIndex):
            if index % 2 == 0:
                print("{} {}".format(index, " is an even number"))
            else:
                print("{} {}".format(index, " is an odd number"))

    def divisibleBy3and5(self, startIndex, endIndex):
        for index in range(startIndex, endIndex):
            if index % 3 == 0 and index % 5 == 0:
                print("{} {}".format(index, "divisible by 3 & 5"))

            elif index % 3 == 0:
                print("{} {}".format(index, "divisible by 3"))
            elif index % 5 == 0:
                print("{} {}".format(index, "divisible by 5"))
            else:
                print("{} {}".format(index, "not divisible by 3 & 5"))

    def divideNumber(self, num):
        if num < 0:
            print("{} {}".format(num, " is a negative number"))

        elif num % 2 == 0:
            print("{} {}".format(num, " is an even number"))

        else:
            print("{} {}".format(num, " is an odd number"))

    def printHashColon(self, startIndex, endIndex, name):
        for index in range(startIndex, endIndex):
            if index % 2 == 0:
                print("{} {} {}".format(name, "-", index))
            else:
                print("{} {} {}".format(name, ":", index))


eo = EvenOdd()
eo.printEvenNumber(1, 10)
# eo.divisibleBy3and5(1, 20)
# eo.divideNumber(-22)
# eo.printHashColon(1, 10, "Aniket")
