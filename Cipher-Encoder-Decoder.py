alphabets = [
    "a","b","c","d","e","f","g","h","i","j",
    "k","l","m","n","o","p","q","r","s","t",
    "u","v","w","x","y","z"
]
EnADe=input("Type encode to encrypt and decode to decrypt:").lower()
input_text=input("Input Text to Encode or Decode:").lower()
shift=int(input("Input shift numer:"))


def ceasar(original_text,shift_num,Direction):
    encrypted_text=""
    if EnADe=="decode":
        shift_num*=-1
    for letter in original_text:
        shifted_letters=alphabets.index(letter)+shift_num
        shifted_letters%=len(alphabets)
        encrypted_text+=alphabets[shifted_letters]
    print(f"the encoded text is {encrypted_text}")

ceasar(original_text=input_text,shift_num=shift,Direction=EnADe)




def encode(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decode(text, shift=3):
    return encode(text, -shift)


# User input
message = input("Enter a name or sentence: ")

encoded = encode(message)
decoded = decode(encoded)

print("Encoded Text:", encoded)
print("Decoded Text:", decoded)
