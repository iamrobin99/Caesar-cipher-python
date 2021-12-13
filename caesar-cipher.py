# -*- coding: utf-8 -*-

alphabet = 'abcdefghijklmnopqrstuvwxyz '

letter_to_index = dict(zip(alphabet, range(len(alphabet)))) # indexing each alphabet by using dictionary and zip

index_to_letter = dict(zip(range(len(alphabet)), alphabet)) # viceversa of the above

def encrypt(plain_text, shift):
    cipher = ''
    for char in plain_text:
        index = (letter_to_index[char] + shift) % len(alphabet)
        cipher += index_to_letter[index]
    return cipher

def decrypt(cipher, shift):
    plain = ''
    for char in cipher:
      index = (letter_to_index[char] - shift) % len(alphabet)
      plain += index_to_letter[index]
    return plain

message = input('Enter you message to encrypt: ')
shift = int(input('Enter your shift value: ' ))

def main(message, shift):
   message = message.lower()
   encrypted_message = encrypt(message, shift)
   decrypted_message = decrypt(encrypted_message, shift)
   print ('Encrypted msg: ' + encrypted_message)
   print ('Decrypted msg: ' + decrypted_message)
main(message, shift)

