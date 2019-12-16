import os
import sys

path = sys.argv[1]
appName = path.split('\\')[-1]

production = {}
test = {}

for subdir, dirs, files in os.walk(path):
    for file in files:
        if(file.endswith(".java") and not file.endswith("Tests.java") and not file.endswith("Test.java")):
            production[file] = os.path.join(subdir, file)

for subdir, dirs, files in os.walk(path):
    for file in files:
        if(file.endswith("Test.java") or file.endswith("Tests.java") and (not file.endswith("TckTest.java"))): # tcktest is removed because there's no production file that corresponds.
            test[file] = os.path.join(subdir, file)

with open('input.csv', 'w') as f:
    for testFileName, testFilePath in test.items():
        if testFileName.endswith('Test.java'):
            name = testFileName.replace('Test.java','')
        elif testFileName.endswith('Tests.java'):
            name = testFileName.replace('Tests.java','')
        for productionFileName, productionFilePath in production.items():
            if name == productionFileName.replace('.java',''):
                print(appName +","+ testFilePath +","+ productionFilePath, file = f)

f.close()