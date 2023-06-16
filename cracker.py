import hashlib
from urlib.request import urlopen

def readwordlist(url):
  try:
    wordlistfile = urlopen(url).read()
  except Exception as e:
    print("Hey there was an error while reading the wordlist. Error:")
    exit()
  return wordlistfile

def hash(password):
  result = haslib.sha1(password.encode())
  return result.hexdigest()

def bruteforce(guesspasswordlist, actual_password_hash):
  for guess_password in guesspasswordlist:
    if hash(guess_password) == actual_password_hash:
      print("Hey! Your password is:", guess_password,
            "\nPlease consider changing this because it was really easy to guess it :)")
      # If password is found, it should terminate the script here
      exit()
      
url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
actual_password = 'superhero'
actual_password_hash = hash(actual_password)

wordlist = readwordlist(url).decode('UTF-8')
guesspasswordlist = wordlist.split('\n')

# Running the Brute Force attack
bruteforce(guesspasswordlist, actual_password_hash)

# It would be executed if your password was not there in the wordlist
print("Hey! I couldn't guess this password, it was not in my wordlist. That means this is a good password! You win! :)")
