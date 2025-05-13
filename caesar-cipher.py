#encryption
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
text = input("Please enter the text: ")
shift = int(input("Please enter the shift value: "))

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        #to make sure that the shifted position always remain within the range of the alphabets
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")
    return cipher_text  # Return the result so we can use it for decryption

#decryption
def decrypt(cipher_text, shift_amount):
    output_text = ""
    for letter in cipher_text:
        shifted_position = alphabet.index(letter) - shift_amount
        #to make sure that the shifted position always remain within the range of the alphabets
        # Using modulo properly for negative indices
        shifted_position = (shifted_position % len(alphabet))
        output_text += alphabet[shifted_position]
    print(f"Here is the decoded result: {output_text}")

# First encrypt the text
encrypted_text = encrypt(original_text=text, shift_amount=shift)
# Then decrypt the encrypted text
decrypt(cipher_text=encrypted_text, shift_amount=shift)