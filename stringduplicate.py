string_ = "Alef feels very very nice to get you on boad into Alef as you looks a very nice professional into the technical space we are working on."#input()
a = string_.split()

output = [] # to append the duplicates.
unique_words = []

# Duplicate words dictionary
duplicates = {}
# for i in a:
#     if i not in unique_words:
#         unique_words.append(i)
#     else:
#         output.append(i)

for word in string_.split():
    if word in duplicates:
        duplicates[word]+=1
    else:
        duplicates[word]=1

duplicateWords = []
print("Duplicate Elements are: {}".format(duplicates))
for keys, values in duplicates.items():
    if(values>1):
        duplicateWords.append(keys)

duplicateWords =  duplicateWords[::-1]
print("Duplicate Elements are: {}".format(duplicateWords))
outputstring = string_ + ' '.join(duplicateWords)
print(outputstring)


#reverse the duplicate array
output = output[::-1]


string1 = ' '.join(output)
final_string = string_ + " " + string1

# print(final_string)
