import mnemonic
import secrets

while True:
    # Input a number of words
    numbers = input("How many words in your mnemonic? (12, 15, 18, 21, 24): ")
    if numbers=="12":byte=16
    elif numbers=="15":byte=20
    elif numbers=="18":byte=24
    elif numbers=="21":byte=28
    elif numbers=="24":byte=32
    else : 
        print("Not a valid input!")
        break

    # Define the BIP39 word list language
    language = 'english'  # You can choose a different language if desired

    # Generate a random seed of 16 bytes, 20 bytes, 24 bytes, 28 bytes or 32 bytes
    seed = secrets.token_bytes(byte)

    # Create a BIP39 mnemonic using the random seed and language
    mnemo = mnemonic.Mnemonic(language)
    mnemonic_words = mnemo.to_mnemonic(seed)

    # Split the mnemonic into individual words
    mnemonic_word_list = mnemonic_words.split()

    # Print the generated mnemonic
    print("Generated Mnemonic:")
    print(" ".join(mnemonic_word_list))

print("Bye!")
