text = input("Please enter a sentence:")
text = text.lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"
shift = 5 

cipherbet = {}

for i in range(len(alphabet)):
    old_letter = alphabet[i]
    position_shift = (i+shift)%26
    new_letter = alphabet[position_shift]
    cipherbet[old_letter]= new_letter

print("Cipher dictionary:", cipherbet)

coded_text = ""

for char in text:
    if char in cipherbet:
        coded_text += cipherbet[char]
    else:
        coded_text += char

print("Coded text:",coded_text)       
