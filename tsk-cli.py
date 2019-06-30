#!/usr/bin/env python2.7

import bible
import csv
import sys
import re

if len(sys.argv) > 1:
    ref_args = sys.argv[1:]
    ref_string = ' '.join(ref_args)
else:
    ref_string = raw_input("Reference: ")

with open('tskxref.txt') as csvFile:
    csvReader = csv.DictReader(csvFile, delimiter='\t')
    tsk = list(csvReader)

reference = bible.Verse(ref_string)

print
print '# {0}'.format(reference.format())
print

for row in tsk:
    matches_book = int(row['book']) == reference.book
    matches_chapter = int(row['chapter']) == reference.chapter
    matches_verse = int(row['verse']) == reference.verse

    if matches_book and matches_chapter and matches_verse:
        print '## {0}'.format(row['words'])
        print

        # bible library chokes on mr as an abbreviation for Mark
        ref_string = re.sub(r'\bmr\b', r'Mark', row['refs'])
        refs = ref_string.split(';')
        for ref in refs:
            reference = bible.Verse(ref)
            print reference.format()

        print
