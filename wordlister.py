#
# script pour créer une worldlist a partir d'information récupéré sur quelqu'un ou quelque chose
#
print(
    "\n------------------------------\n----------Wordlister----------\n------------------------------\n"
)

#
# fonction 1 : entrée continue d'input jusqu'à que ce soit écrit 'Next'
#
user_input = ""
information_list = []

while user_input != "Next":
    user_input = input("Enter an information (? for help): ")
    if user_input == "?":
        print("date = xx/xx/xxxx \n'Next' afin de quitter l'interface\n")
    else:
        if user_input != "Next":
            information_list.append(user_input)

#
# fonction 2 bis : algorythme de changement
#
from operator import ne

# fonction pour transformer Mots en M0t5

# voyelles
def vowelNumbering(word):
    splited_word = list(word)
    new_word = ""
    for characters in splited_word:
        if characters == "I" or characters == "i":
            new_word += "1"
        elif characters == "A" or characters == "a":
            new_word += "4"
        elif characters == "O" or characters == "o":
            new_word += "0"
        elif characters == "E" or characters == "e":
            new_word += "3"
        else:
            new_word += characters
    return new_word


# consonnes
def consonantNumbering(word):
    splited_word = list(word)
    new_word = ""
    for characters in splited_word:
        if characters == "S" or characters == "s":
            new_word += "5"
        else:
            new_word += characters
    return new_word


# toutes les lettres
def allNumbering(word):
    splited_word = list(word)
    new_word = ""
    for characters in splited_word:
        if characters == "I" or characters == "i":
            new_word += "1"
        elif characters == "A" or characters == "a":
            new_word += "4"
        elif characters == "O" or characters == "o":
            new_word += "0"
        elif characters == "E" or characters == "e":
            new_word += "3"
        elif characters == "S" or characters == "s":
            new_word += "5"
        else:
            new_word += characters
    return new_word


#
# fonction 2 : création de la list
#
wordlist = []


def wordlisting(data):
    # data_array = data.split()
    for element in data:
        wordlist.append(element)
        if consonantNumbering(element) not in wordlist:
            wordlist.append(consonantNumbering(element))
        if vowelNumbering(element) not in wordlist:
            wordlist.append(vowelNumbering(element))
        if allNumbering(element) not in wordlist:
            wordlist.append(allNumbering(element))

        # algorythme de fusion des mots
        # par rapport au type d'information ?
        # traiter la date
    return wordlist


#
# fonction 3 : écriture de la list dans un fichier text (mettre le fichier dans le dossier courant)
#
def write_wordlist_in_txt_file(wordlist_arg):
    filename = input("comment voulez vous nommer votre fichier ? (.txt a la fin): ")
    filename += ".txt"
    print(filename)
    # ecrire me fichier dans dossier courant
    if filename == ".txt":
        filename = "wordlist"
    TXT_WORDLIST = open(filename, "w")
    for element in wordlist_arg:
        TXT_WORDLIST.write(element + "\n")
    TXT_WORDLIST.close()


#
# execution
#
if len(information_list) > 0:
    wordlisting(information_list)
    # print(wordlist)
    txt_user_input = input(
        "\nDo you want to write this list in a TXT file ? (Y or N): "
    )
    if txt_user_input == "Y" or txt_user_input == "y":
        write_wordlist_in_txt_file(wordlist)

print(
    "\n------------------------------\n-------------END.-------------\n------------------------------\n"
)
