def acronym():
    words = raw_input("enter some words you want to turn into an acronym: ")
    # print words
    word_array = words.split()
    # print word_array
    acronym = ""
    for word in word_array:
        acronym += word[0].upper()
    print acronym

def test():
    print "expect the results of user input 'I want cookies' to be IWC"
    acronym()
test()
