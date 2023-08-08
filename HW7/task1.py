def check_rhyme(sentence):
    num_syllables = []
    for word in sentence.split():
        if len(word) == 1:
            num_syllables.append(1)
        else:
            num_syllables.append(len(word))
    if num_syllables == [1] * len(num_syllables):
            return "Парам-пам"
    else:
        return "Пам-парам"

text = input("Введите стихотворение Винни-пуха: ")

print(check_rhyme(text))