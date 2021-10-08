words=['apple','banana','orange','pineapple','mango']
from random import randint;
def randomSentenceGenerator(word):
    randomNo= randint(0,len(words)-1);
    return f'{words[randomNo]} {word}'

with open('./test.txt') as file:
    paragraph = file.read();
    wordLists= paragraph.split();
    sentenceLists = list(map(randomSentenceGenerator, wordLists))
    # print(sentenceLists)

    paraCount= int(input('Enter Paragraph Count'));
    for count in range(paraCount):
        with open('./generator.txt','a') as write_file:
            write_file.write(''.join(sentenceLists)+'\n\n');
    