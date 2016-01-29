import bible, sys, csv

tsk = []

with open('tskxref.txt') as csvFile:
    csvReader = csv.DictReader(csvFile, delimiter='\t')
    for row in csvReader:
        tsk.append(row)

referenceArgs = sys.argv[1:]
referenceString = ' '.join(referenceArgs)
reference = bible.Verse(referenceString)

print
print '# {0}'.format(reference.format())
print

for row in tsk:
    if int(row['book']) == reference.book \
    and int(row['chapter']) == reference.chapter \
    and int(row['verse']) == reference.verse:
        print '## {0}'.format(row['words'])
        print

        refs = row['refs'].split(';')
        cleanRefs = ''
        for ref in refs:
            reference = bible.Verse(ref)
            print reference.format()

        print