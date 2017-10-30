# Author: Luis A. Vargas
# Solutions to exercises from Python Class
# 10/29/2017 

import os, sys

# EXERCISE 1:  Write a Python function to read a text file and print the the number of lines, the number of words, and the number of characters present in that file.

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

# EXERCISE 2: Define a function ‘csvWriter’ that takes in a list of records and stores the data in csv format.

def csvWriter(file_fullpath, record_dic):
    dir_tuple = os.path.split(file_fullpath)
    if dir_tuple[0] is '':
        parent_path = os.path.dirname(__file__)
    else:
        parent_path = dir_tuple[0]

    if os.path.exists (parent_path):
        file_tuple = os.path.splitext(file_fullpath)
        if file_tuple[1] != ".csv":
            file_name = file_tuple[0] + ".csv"
        else:
            file_name = file_tuple[0] + file_tuple[1]

        new_full_path = os.path.join(parent_path,file_name)

        header_file_output = ""
        content_file_output = ""
        counter = 0
        records_processed = 0
        for single_list in record_dic:
            records_processed += 1
            for key in sorted(single_list.keys()):
                if counter < 3:
                   header_file_output += key + ","
                content_file_output += str(single_list[key]) + ","
                counter += 1
            content_file_output = content_file_output.rstrip(',')
            content_file_output += "\n"
               
        header_file_output = header_file_output.rstrip(',')
        content_file_output = content_file_output.rstrip(',\n')
        content_file_output += "\n"

        output_file = open(new_full_path,"w")
        output_file.write(header_file_output + "\n")
        output_file.write(content_file_output)
        output_file.close

        print ("{0} records processed.".format(records_processed))
          
# EXERCISE 3 - In unix system, the '/etc/hosts' file contains 
# the mappings of IP addresses to host names. Each entry is an 
# individual line with the IP address on the first column followed 
# by the corresponding host name. Comments in the file are preceded by '#'. Sample /etc/hosts

def gethostname(ip_address_or_hostname):
    hosts_file = "hosts.txt"
    if os.path.exists(hosts_file):
        entry_dictionary = {}
        hosts_file_handle = open(hosts_file)
        for line in hosts_file_handle:
            if line[0] == "#":
               continue
            key_value = line.split()
            if '#' in key_value[0]:
                index_of_pound = int(key_value[0].index("#"))
                key_value[0] = key_value[0][:index_of_pound]
            if "#" in key_value[1]:
                index_of_pound = int(key_value[1].index("#"))
                key_value[1] = key_value[1][:index_of_pound]
            entry_dictionary[key_value[0]] = key_value[1]
        hosts_file_handle.close()

        host_found = 0

        if ip_address_or_hostname.find('.') > -1:
            for key in entry_dictionary.keys():
                if key == ip_address_or_hostname:
                    print (str(entry_dictionary[key]))
                    host_found = 1
                    
        else:
            for key in entry_dictionary.keys():
                if entry_dictionary[key] == ip_address_or_hostname:
                    print (key)
                    host_found = 1
        
        if host_found == 0:
            print ("Unknown host")

    else:
        print ("{0} file does not exist or could not be found in current directory".format("/etc/hosts"))



read_file(os.path.join(os.path.dirname(__file__), "SampleFile.txt"))

records = []

records.append({'x':1,'y':2,'z':3})
records.append({'z':6,'y':5,'x':4})
csvWriter("records.txt", records)

gethostname("127.0.0.1")
gethostname("192.168.2.253")
gethostname("192.168.2.254")
gethostname("pyschools")

