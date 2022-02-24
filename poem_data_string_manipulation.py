highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

# Split the string by the commas and sort them into a list.
highlighted_poems_list = highlighted_poems.split(',')

print(highlighted_poems_list)

# Strip whitespace from each element within the list.
highlighted_poems_stripped = []

for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())

print(highlighted_poems_stripped)

# Split into easier to read details.
highlighted_poems_details = []

for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))

print(highlighted_poems_details)

# Sort the different data types into lists.
titles = []
poets = []
dates = []

for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])

print(titles)
print(poets)
print(dates)

# Attached strings to all poems in the list using the ' .format' method.
for poem in highlighted_poems_details:
  title = poem[0]
  poet = poem[1]
  date = poem[2]
  print("The poem {} was published by {} in {}".format(title, poet, date))
