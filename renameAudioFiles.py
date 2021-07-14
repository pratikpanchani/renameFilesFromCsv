import os
import csv

foo = {}

with open('list.csv', 'rt') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        foo[row[0] + '.wav'] = row[1] + '.wav'
    oldPath = 'oldAudioNames/'
    newPath = 'newAudioNames/'
    for oldname in os.listdir(oldPath):
        if oldname in foo:
            try:
                os.rename(os.path.join(oldPath, oldname), os.path.join(newPath, foo[oldname]))
            except:
                print('File ' + oldname + ' could not be renamed to ' + foo[oldname] + '!')