with open("/Users/wsy_956559_/Desktop/软件工程专题/python/exercise 1/file_to_read.txt", "r") as file:
    content = file.read()
word_count = content.count("terrible")

def replace_word(word, i):
    if i % 2 == 0:
        return "pathetic"
    else:
        return "marvellous"

def replace_write_text(file_path, result_txt, word):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        count = 0
        for i in range(len(words)):
            if words[i].strip('.,?!') == word:
                count += 1
                replacement = replace_word(word, count)
                words[i] = replacement

        new_text = ' '.join(words)

    with open(result_txt, 'w') as new_file:
        new_file.write(new_text)


file_path = '/Users/wsy_956559_/Desktop/软件工程专题/python/exercise 1/file_to_read.txt'
result_txt = "/Users/wsy_956559_/Desktop/软件工程专题/python/exercise 1/result.txt"
word = "terrible"

replace_write_text(file_path, result_txt, word)
print("The number of times the word terrible appears：", word_count)
print("The replacement text has been written in result.txt")