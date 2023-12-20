#test_str = "Because I could not stop for Death - The Dews drew quivering and Chill - For only Gossamer, my Gown - My Tippet - only Tulle - We paused before a House that seemed A Swelling of the Ground - The Roof was scarcely visible - The Cornice - in the Ground - Since then - tis Centuries - and yet Feels shorter than the Day I first surmised the Horses Heads Were toward Eternity -"

#test_str = "This latent mine--these unlaunch'd voices--passionate powers, Wrath, argument, or praise, or comic leer, or prayer devout, (Not nonpareil, brevier, bourgeois, long primer merely,) These ocean waves arousable to fury and to death, Or sooth'd to ease and sheeny sun and sleep, Within the pallid slivers slumbering."
test_str = "THIS is thy hour O Soul, thy free flight into the wordless, Away from books, away from art, the day erased, the lesson done, Thee fully forth emerging, silent, gazing, pondering the themes thou lovest best,Night, sleep, death and the stars."
#update: quads, caps
case_dict = {
    ' ': 400,
    'e': 400,
    'n': 336,
    'o': 336,
    'i': 304,
    'a': 304,
    't': 304,
    's': 304,
    'r': 304,
    'l': 200,
    'h': 200,
    'd': 176,
    'm': 160,
    'c': 160,
    'f': 160,
    'u': 160,
    '.': 160,
    ',': 160,
    'b': 128,
    'p': 120,
    'g': 120,
    'y': 120,
    'w': 120,
    'j': 72,
    'v': 72,
    'k': 72,
    'q': 48,
    'x': 48,
    'z': 48,
    '\'': 48,
    '\'': 48,
    '-': 40,
    'fi': 32,
    'ff': 32,
    'fl':24,
    'ffl': 24,
    'ffi': 24,
    'st': 24,
    'ct': 24,
    '"': 24,
    '"': 24,
    '?': 24,
    ']': 24,
    '[': 24,
    ')': 24,
    '(': 24,
    '!': 24,
    ';': 24,
    ':': 24,
    '&': 24,
    'A': 28,
    'B': 15,
    'C': 18,
    'D': 19,
    'E': 38,
    'F': 20,
    'G': 18,
    'H': 20,
    'I': 28,
    'K': 12,
    'L': 23,
    'M': 16,
    'N': 31,
    'O': 30,
    'P': 20,
    'Q': 7,
    'R': 20,
    'S': 20,
    'T': 38,
    'V': 13,
    'W': 12,
    'X': 6,
    'Y': 15,
    'Z': 8,
    'J': 10,
    'U': 15
}
count_dict = {}
minus_dict = {}
proportions_dict = {}
count = 0
#test_str = input("input text here [no caps]: ")
#convert string to list
char_list = list(test_str.strip())

#count up each sort in string
for char in char_list:
    if char in count_dict.keys():
        x = count_dict[char]
        count_dict[char] =  x + 1
    else:
        count_dict[char] = 1

print("\n sorts used:")
print(count_dict)

for key in count_dict:
    x = case_dict[key]
    minus_dict[key] = x - count_dict[key]

print("\n sorts remaining:")
print(minus_dict)
print("\n")

for key in count_dict:
    z = (count_dict[key] / case_dict[key]) 
    proportions_dict[key] = z

print ("\n proportions:")
print (proportions_dict)

with open('count_dict.txt','w') as data:  
      data.write(str(count_dict))