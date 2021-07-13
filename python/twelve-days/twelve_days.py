index = ['first', 
         'second', 
         'third',
         'fourth',
         'fifth',
         'sixth',
         'seventh',
         'eighth',
         'ninth',
         'tenth',
         'eleventh',
         'twelfth']

lyrics = ['a Partridge in a Pear Tree.',
          'two Turtle Doves,',
          'three French Hens,',
          'four Calling Birds,',
          'five Gold Rings,',
          'six Geese-a-Laying,',
          'seven Swans-a-Swimming,',
          'eight Maids-a-Milking,',
          'nine Ladies Dancing,',
          'ten Lords-a-Leaping,',
          'eleven Pipers Piping,',
          'twelve Drummers Drumming,']

def recite(start_verse, end_verse):
    verses = []
    for i in range(start_verse-1, end_verse):
        verse = ["On the {} day of Christmas my true love gave to me:".format(index[i])]
        for j in range(i,-1,-1):
            if j == 0 and i != 0:
                verse.append('and ' + lyrics[j])
            else:
                verse.append(lyrics[j])
        verses.append(' '.join(verse))
    return verses