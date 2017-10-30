import os, sys

# Write a Python function to read a text file and print the the number of lines, the number of words, and the number of characters present in that file.

def read_file(filepath):
    if os.path.exists(filepath):

        line_counter = 0
        word_counter = 0
        char_counter = 0

        file_object = open(filepath,'r')
        for line in file_object:
            word_counter += len (line.split())
            line_counter += 1
            for word in line.split():
                char_counter += len(list(word))

        if line_counter > 1:
            line_counter_msg = "lines"
        else:
            line_counter_msg = "line"

        if word_counter > 1:
            word_counter_msg = "words"
        else:
            word_counter_msg = "word"

        if char_counter > 1:
            char_counter_msg = "characters"
        else:
            char_counter_msg = "character"
        
        print ("This file contains {0} {1}, {2} {3}, and {4} {5} in total.".format(line_counter,line_counter_msg, word_counter, word_counter_msg, char_counter, char_counter_msg))
    else:
       print ("'{0}' was not found!".format(filepath))

read_file(os.path.join(os.path.dirname(__file__), "SampleFile.txt"))
