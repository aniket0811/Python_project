class ReadWriteFile:

    def readFileContent(self):
        with open("Test.txt", 'r') as file:
            for line in file.readlines():
                # file = open("Test.txt")
                # print(file.read())
                # while line != "":
                #     print(line.strip())
                # line = file.readline()
                print(line.strip())

    def writeFile(self):
        with open("Test.txt", 'r') as reader:
            list_content = reader.readlines()
            reversed(list_content)
            with open("Test.txt", 'w') as writer:
                for line in reversed(list_content):
                    writer.write(line)
                    print(line.strip())


rf = ReadWriteFile()
# rf.readFileContent()
rf.writeFile()
