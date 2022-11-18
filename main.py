# --------------------------------------MORSE CODE CONVERTER---------------------------- #


# Variables
morse_code = {"a": "._",
              "b": "_...",
              "c": "_._.",
              "d": "_..",
              "e": ".",
              "f": ".._.",
              "g": "__.",
              "h": "....",
              "i": "..",
              "j": ".___",
              "k": "_._",
              "l": "._..",
              "m": "__",
              "n": "_.",
              "o": "___",
              "p": ".__.",
              "q": "__._",
              "r": "._.",
              "s": "...",
              "t": "_",
              "u": ".._",
              "v": "..._",
              "w": ".__",
              "x": "_.._",
              "y": "_.__",
              "z": "__..",
              "1": ".____",
              "2": "..___",
              "3": "...__",
              "4": "...._",
              "5": ".....",
              "6": "_....",
              "7": "__...",
              "8": "___..",
              "9": "____.",
              "0": "_____",
              " ": "|"}

# User Set up
words = input("This is your text to Morse Code converter\n\nPut your desired text here:\n> ").lower()

# -----------------------------------------CONVERT TEXT TO MORSE CODE---------------------------------- #

# Convert user input
code = " ".join(morse_code[i] for i in words if i in morse_code)
clean_text = "".join(i for i in words if i in morse_code)


if "|" in code:
    print(f"\nConverted:\n{code}\n('|' =  Word separator)\n\nYour text:\n{clean_text.title()}")

else:
    print(f"\nConverted:\n{code}\n\nYour text:\n{clean_text.title()}")
