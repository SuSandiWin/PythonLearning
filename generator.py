with open('./test.txt') as file:
    paragraph= file.read();
    paragraphCount = int(input('Enter paragraph no : '));

for count in range(paragraphCount):
    with open('./generator.txt','a') as write_file:
        write_file.write(paragraph+'\n\n');
  