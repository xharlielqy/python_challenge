# python challenge 2: Map
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb." + \
    " rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb" + \
    " sqgle qrpgle.kyicrpylq() gq pcamkkclbcb." + \
    " lmu ynnjw ml rfc spj."
text_2 = 'map'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']
new_text = ''
for letter in text:
    if letter in alphabet:
        new_letter_position = alphabet.index(letter) + 2
        if new_letter_position > 25:
            new_letter_position = new_letter_position - 26
            new_text = new_text + alphabet[new_letter_position]

        else:
            new_text = new_text + alphabet[new_letter_position]

    else:
        new_text = new_text + letter

print(new_text)
#  try string.maketrans()
text_3 = 'abcedfghijklmnopqrstuvwxyz'
text_4 = 'cdefghijklmnopqrstuvwxyzab'
table = ''.maketrans(text_3, text_4)
print(text_2.translate(table))
