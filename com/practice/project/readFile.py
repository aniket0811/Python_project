class ReadFile:

    def readFileContent(self):
        file = open("Test.txt")
        # print(file.read())
        # while line != "":
        #     print(line.strip())
        # line = file.readline()
        for line in file.readlines():
            print(line.strip())
        file.close()


rf = ReadFile()
rf.readFileContent()
