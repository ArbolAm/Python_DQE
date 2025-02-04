import re


text = """ tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87. """


# make easy transformations at the beginning
b = text.lower().split(".")
b.pop()  # delete empty string generated from last "." split
print(b)


# make correct text structure
last_sentence_lst = []
for i in range(len(b) - 1):
    b[i] = b[i].strip().capitalize()
    last_sentence_lst.append(b[i].split()[-1])

print(b)


# create sentence with last words
b.append(" ".join(last_sentence_lst).capitalize())
print(b)


# construct final text
final_text = ". ".join(b)
print(final_text)


# make iz correct
final_text = re.sub(r'(?<=\s|\w)iz(?=\s|\w)', 'is', final_text)
print(final_text)


# count whitespaces
whitespace_count = len(re.findall(r'\s', text))
print(whitespace_count)
