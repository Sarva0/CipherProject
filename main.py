import time

##Ceaser Cipher, made with class
#Ceaser Encrypt

def encrypt():
    message = input("Enter a message: ")
    shift = input("Enter a shift value: ")

    if shift.isnumeric():
        shiftInt = int(shift)
        newMessage = ""

        for letter in message:
            letterAsNum = ord(letter)

            if 97 <= letterAsNum <= 122:
                newLetterAsNum = (letterAsNum - 97 + shiftInt) % 26 + 97
                newLetter = chr(newLetterAsNum)
                newMessage += newLetter
            else:
                newMessage += letter

        print(newMessage)
        print("")
        time.sleep(1)
        begin()
    else:
        print("")
        print("Please enter an integer")
        time.sleep(1)
        encrypt()

#Ceaser Decrypt

def decrypt():
    encrypted_message = input("Enter the encrypted message: ")
    shift = input("Enter the shift value: ")

    if shift.isnumeric():
        shift = int(shift)
        decrypted_message = ""

        for letter in encrypted_message:
            letter_as_num = ord(letter)

            if 97 <= letter_as_num <= 122:
                new_letter_as_num = letter_as_num - shift % 26
                if new_letter_as_num < 97:
                    new_letter_as_num += 26
                new_letter = chr(new_letter_as_num)
                decrypted_message += new_letter
            else:
                decrypted_message += letter

        print("Decrypted Message: " + decrypted_message)
        print("")
        time.sleep(1)
        begin()
    else:
        print("Please enter an integer.")
        decrypt()

# Start ceasercipher
def ceaserStart():
  start = input("Do you want to ENCRYPT or DECRYPT? ").lower()
  if start == "encrypt":
    print("")
    encrypt()
  elif start == "decrypt":
    print("")
    decrypt()
  else:
    print("")
    ceaserStart()




######################################################################
##Fractionated Morse Cipher
#Encryption option

def encryption():
  def toMorseCode(text):
    code = {'A': '.-',
              'B': '-...',
              'C': '-.-.',
              'D': '-..',
              'E': '.',
              'F': '..-.',
              'G': '--.',
              'H': '....',
              'I': '..',
              'J': '.---',
              'K': '-.-',
              'L': '.-..',
              'M': '--',
              'N': '-.',
              'O': '---',
              'P': '.--.',
              'Q': '--.-',
              'R': '.-.',
              'S': '...',
              'T': '-',
              'U': '..-',
              'V': '...-',
              'W': '.--',
              'X': '-..-',
              'Y': '-.--',
              'Z': '--..',
              '1': '.----',
              '2': '..---',
              '3': '...--',
              '4': '....-',
              '5': '.....',
              '6': '-....',
              '7': '--...',
              '8': '---..',
              '9': '----.',
              '0': '-----',
              ' ': 'x' }
    morseCode = ''
    for letter in text:
      morseCode += code[letter.upper()]
    return morseCode

  def fractionMorse(out, key_list):

    fractionCode = { '...': key_list[0],
                     '..-': key_list[1],
                     '..x': key_list[2],
                     '.-.': key_list[3],
                     '.--': key_list[4],
                     '.-x': key_list[5],
                     '.x.': key_list[6],
                     '.x-': key_list[7],
                     '.xx': key_list[8],
                     '-..': key_list[9],
                     '-.-': key_list[10],
                     '-.x': key_list[11],
                     '--.': key_list[12],
                     '---': key_list[13],
                     '--x': key_list[14],
                     '-x.': key_list[15],
                     '-x-': key_list[16],
                     '-xx': key_list[17],
                     'x..': key_list[18],
                     'x.-': key_list[19],
                     'x.x': key_list[20],
                     'x-.': key_list[21],
                     'x--': key_list[22],
                     'x-x': key_list[23],
                     'xx.': key_list[24],
                     'xx-': key_list[25]}
    translated_string = ''
    for letter in out:
      translated_string += fractionCode.get(letter.lower(), letter)
    return translated_string


  #asking for Key
  def askKey():
    key = input("Please enter a 26 letter alphabet key (Do not repeat the same letter twice): ")
    keyUpper = key.upper()
    global key_list
    key_list = [char for char in keyUpper]
    if len(key_list) == 26:
      #print(key_list)
      pass
    else:
      askKey()
  ####

  #Message
  text = input("Enter a message: ")
  #step 2
  askKey()
  #
  text1 = text.replace('', ' ')
  newText = text1[1:]
  text2 = toMorseCode(newText)

  

  #Split morse code into groups of 3
  #
  string = text2.replace('xxx', 'xx')
  n = 3
  #print(string)
  out = [(string[i:i+n]) for i in range(0, len(string), n)]
  #print(out)

  #length of array
  outLength = len(out) - 1

  #counting the letters in each string

  count = [len(i.replace(" ","")) for i in out]

  #adding extra dot if last group doesn't have 3
    #counting the last elements' character
  codeLength = len(out)
  #print(codeLength)
    #adding morse code if the element is too short
  if codeLength == 3:
    result_string = ''.join(out)
    fractionMorse(result_string, key_list)
  elif codeLength == 2:
    out[outLength] += '.'
    result_string = ''.join(out)
  elif codeLength == 1:
    out[outLength] += '.'
    out[outLength] += '.'
    result_string = ''.join(out)

  #output
  print ("")
  print("Here's your encrypted message: " + fractionMorse(out, key_list))
  print("")
  time.sleep(1)
  begin()


# Decryption option


def decryption():
  #1st step dict
  def inverseFractionMorse(out, key_list):
      inverseFractionCode = {key_list[0]: '...', key_list[1]: '..-', key_list[2]: '..x', key_list[3]: '.-.', key_list[4]: '.--', key_list[5]: '.-x', key_list[6]: '.x.', key_list[7]: '.x-', key_list[8]: '.xx',
     key_list[9]: '-..', key_list[10]: '-.-', key_list[11]: '-.x', key_list[12]: '--.', key_list[13]: '---', key_list[14]: '--x', key_list[15]: '-x.', key_list[16]: '-x-', key_list[17]: '-xx',
     key_list[18]: 'x..', key_list[19]: 'x.-', key_list[20]: 'x.x', key_list[21]: 'x-.', key_list[22]: 'x--', key_list[23]: 'x-x', key_list[24]: 'xx.', key_list[25]: 'xx-'}
      decrypted_string = ''
      for letter in out:
        decrypted_string += inverseFractionCode[letter.upper()]
      return decrypted_string
  #2nd step dict
  def inverseMorseCode(decrypted_message1):
    inverseCode = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '  ': '', ' ': ' '
    }
    inversemorseCode = ''
    decrypts = decrypted_message1.split(' ')
    #print(decrypts)
    decrypts.pop()
   # print(decrypts)
    for letter in decrypts:
      inversemorseCode += inverseCode.get(letter, ' ')
    #print(inversemorseCode)
    return inversemorseCode
  #Ask for message
  encrypted_message = input("What's the encrypted message?: ").upper()
  #Ask for key
  def ask():
    key2 = input("Please enter the 26 letter alphabet key: ").upper()
    global key_list2
    key_list2 = [char for char in key2]
    if len(key_list2) == 26:
        pass
    else:
        ask()
  ask()
  # Decrypt the message
  decrypted_message = inverseFractionMorse(encrypted_message, key_list2)
  decrypted_message1 = decrypted_message.replace('x', ' ')
  #print(decrypted_message1)
  final_decrypt = inverseMorseCode(decrypted_message1)
  print("")
  print("Decrypted Message: " + final_decrypt)
  print("")
  time.sleep(1)
  begin()

#start function
def startList(): 
  start = input("Do you want to ENCRYPT or DECRYPT Fractionated Morse Cipher?: ").lower()
  if start == "encrypt":
    print("")
    print("")
    encryption()
  elif start == "decrypt":
    print("")
    print("")
    decryption()




##########################################################
##My cipher
#MYCipher Start
def start():
  startask = input("Do you want to ENCRYPT or DECRYPT: ").lower()
  if startask == "encrypt":
    myEncrypt()
  elif startask == 'decrypt':
    myDecrypt()
  else:
    start()
#My cipher's encrypt

def myEncrypt():
  def toMorseCode(text, key_array):
    code = {  key_array[0]: 'Q',
              key_array[1]: 'W',
              key_array[2]: 'E',
              key_array[3]: 'R',
              key_array[4]: 'T',
              key_array[5]: 'Y',
              key_array[6]: 'U',
              key_array[7]: 'I',
              key_array[8]: 'O',
              key_array[9]: 'P',
              key_array[10]: 'A',
              key_array[11]: 'S',
              key_array[12]: 'D',
              key_array[13]: 'F',
              key_array[14]: 'G',
              key_array[15]: 'H',
              key_array[16]: 'J',
              key_array[17]: 'K',
              key_array[18]: 'L',
              key_array[19]: 'Z',
              key_array[20]: 'X',
              key_array[21]: 'C',
              key_array[22]: 'V',
              key_array[23]: 'B',
              key_array[24]: 'N',
              key_array[25]: 'M',
              ' ': ' '}
    morseCode = ''
    for letter in text:
      morseCode += code[letter.upper()]
    return morseCode

  def askKey():
    key = input("Please enter a 26 letter alphabet key (Do not repeat the same letter twice): ")
    keyUpper = key.upper()
    global key_array
    key_array = [char for char in keyUpper]
    if len(key_array) == 26:
      #print(key_list)
      pass
    else:
      askKey()
  ####

  #Message
  text = input("Enter a message: ")
  #step 2
  askKey()
  #
  encryptedMessage = toMorseCode(text, key_array)
  print("Your encrypted message: " + encryptedMessage)
  print("")
  time.sleep(1)
  begin()


#My Cipher's decrypt

def myDecrypt():
  def fromMorseCode(message, key_array):
    inversed_code = {'Q': key_array[0],
                      'W': key_array[1],
                      'E': key_array[2],
                      'R': key_array[3],
                      'T': key_array[4],
                      'Y': key_array[5],
                      'U': key_array[6],
                      'I': key_array[7],
                      'O': key_array[8],
                      'P': key_array[9],
                      'A': key_array[10],
                      'S': key_array[11],
                      'D': key_array[12],
                      'F': key_array[13],
                      'G': key_array[14],
                      'H': key_array[15],
                      'J': key_array[16],
                      'K': key_array[17],
                      'L': key_array[18],
                      'Z': key_array[19],
                      'X': key_array[20],
                      'C': key_array[21],
                      'V': key_array[22],
                      'B': key_array[23],
                      'N': key_array[24],
                      'M': key_array[25],
                      ' ': ' '}
    inversemorseCode = ''
    for letter in message:
      inversemorseCode += inversed_code[letter.upper()]
    return inversemorseCode


  def askKey():
      key = input("Please enter a 26 letter alphabet key (Do not repeat the same letter twice): ")
      keyUpper = key.upper()
      global key_array
      key_array = [char for char in keyUpper]
      if len(key_array) == 26:
          pass
      else:
          askKey()

  # Message
  message = input("Enter the Morse code to decrypt: ").upper()
  # Step 2
  askKey()
  decrypted_message = fromMorseCode(message, key_array)
  print("Your decrypted messge is: " + decrypted_message)
  print("")
  time.sleep(1)
  begin()
###################################################  



##Begin program

def begin():
  print("Welcome to my Cipher Program!")
  print("Please choose one of the following options:")
  print("1. Ceaser Cipher")
  print("2. Fractionated Morse Code")
  print("3. My cipher")
  choice = input("Enter your choice: ")
  if choice == "1":
    ceaserStart()
  elif choice == "2":
    startList()
  elif choice == "3":
    start()
  else:
    begin()
begin()