import os

appName = "RxJava"
productionPath = r"D:\Pesquisa\RxJava\src\main"
testPath = r"D:\Pesquisa\RxJava\src\test"

production = {}
test = {}

for subdir, dirs, files in os.walk(productionPath):
    for file in files:
        if(file.endswith(".java")):
            production[file] = os.path.join(subdir, file)


for subdir, dirs, files in os.walk(testPath):
    for file in files:
        if(file.endswith(".java") and (not file.endswith("TckTest.java"))): # tcktest is removed because there's no production file that corresponds.
            test[file] = os.path.join(subdir, file)

with open('input.csv', 'w') as f:
    for testFileName, testFilePath in test.items():
        name = testFileName.replace('Test.java','')
        for productionFileName, productionFilePath in production.items():
            if name == productionFileName.replace('.java',''):
                print(appName +","+ testFilePath +","+ productionFilePath, file=f)
f.close()