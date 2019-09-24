import csv
import json
from vncorenlp import VnCoreNLP

annotator = VnCoreNLP(address="http://127.0.0.1", port=9000)

title_data = 'title - Copy.csv'
title_txt = 'title_txt.txt'
tokenizer_result = 'tokenizer.csv'

# with open(title_data, encoding='utf-8') as file:
#     reader = csv.reader(file)
#     print(type(reader))
#     for row in reader:
#         word_segmented_text = annotator.tokenize(row)
#         print(word_segmented_text)

with open(title_data, encoding='utf-8') as file:
    titles = file.readlines()
    fieldnames = 'title'
    with open(tokenizer_result, 'w', encoding='utf-8') as output:
        for title in titles:
            word_segmented_text = annotator.tokenize(title)
            # print(word_segmented_text)
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writerow(word_segmented_text)

#
# # To perform word segmentation, POS tagging, NER and then dependency parsing
# # annotated_text = annotator.annotate(text)
#
# To perform word segmentation only


# writer = csv.writer(open("friends.csv", "ab"), delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
# writer.writerow(word_segmented_text)
