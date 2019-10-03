#Import JSON file and then swap it's keys and values only if they consist of alphabetical characters
#Ensure that the JSON file is flat (Only has 1 level)

#Import json library
import json

#Create variables
output_dict = {}

#Read the example JSON file and load it as a variable
with open('example.json') as f:
    input_dict = json.load(f)

print(input_dict)

#Parse through JSON file and switch keys and values which consist of only alphabetical characters
for key in input_dict: 
    if(key.isalpha() and input_dict[key].isalpha()):
       output_dict.update({input_dict[key] : key})
    else: 
       output_dict.update({key : input_dict[key]})

#Print the new JSON file
print(output_dict)
