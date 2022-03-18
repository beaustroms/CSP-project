LCGdefaults1 = [97, 2, 3, 0, 100]
def LCGgenerator(m, a, c, seed, length):
  oldval = seed
  outlist = []
  for i in range(length):
    newval = (a * oldval + c)%m
    outlist.append(newval)
    oldval = newval
  return(outlist)

def dictalign(list):
  outdict = {}
  list = list.split()
  for i in range(len(list)):
    e = i+1
    outdict[e] = list[i]
  return(outdict)
alphabet = dictalign('a b c d e f g h i j k l m n o p q r s t u v w x y z')
numbers = dictalign('1 2 3 4 5 6 7 8 9 0')
symbols = dictalign(r'- _ = + < , > . ? / : ; " \' { [ } ] \ | ` ~ ! @ # $ % ^ & * ( )')


numbersvals = numbers.values()
numberkeys = numbers.keys()
symbolvals = symbols.values()
symbolkeys = symbols.keys()
alphabetletters = alphabet.values()
alphabetnumbers = alphabet.keys()
inversealphabet = dict(zip(alphabetletters, alphabetnumbers))
inversenumbers = dict(zip(numbersvals, numberkeys))
inversesymbols = dict(zip(symbolvals, symbolkeys))

def shiftbylist(character, list, shift, cypher):
  pass

def cypher(message, alphabet, shift, cypher):
  alphabetletters = alphabet.values()
  alphabetnumbers = alphabet.keys()
  inversealphabet = dict(zip(alphabetletters, 
  alphabetnumbers))
  message = message.lower()
  for i in range(len(message)):
    newcharacter = message[i]
    if message[i] in alphabet.values():
      characterindex = inversealphabet[message[i]]
      if cypher == True:
        newcharacter = alphabet[((characterindex+shift[i])%len(alphabet))]
        try:
          newcharacter = alphabet[((characterindex+shift[i])%len(alphabet))]
        except:
          newcharacter = alphabet[(len(alphabet))]
      else:
        try:
          newcharacter = alphabet[(characterindex-shift[i])%len(alphabet)]
        except:
          newcharacter = alphabet[(len(alphabet) - 1)]
    message = message[:i] + newcharacter + message[i+1:]
  return(message)

seed = input("What would you like the seed to be? ")
message = input("What message would you like to encrypt/decrypt? ")
rnglist = LCGgenerator(97, 2, 3, int(seed), len(message))
#encryptdecrypt = '515125'
encryptdecrypt = input("Would you like to encrypt or decrypt this data? Type 1 or 2 ")
if encryptdecrypt == '1':
  message = cypher(message, alphabet, rnglist, True)
else:
  message = cypher(message, alphabet, rnglist, False)
  pass
print(message)