class Text:
    def __init__(self, text, topic):
        self.text = text
        self.topic = topic
    def text_len(self):
        return len(self.text)

    def count_of_letter(self, letter, letter2):
        text = ''
        for i in self.text:
            if i == letter:
                text += letter2
            else:
                text += i
        return text

    def space_counter(self):
        x = 0
        for i in self.text:
            if i == ' ':
                x += 1
        return x

    def delete_word(self, index):
        text = ''
        array = self.text.split(' ')
        array.pop(index-1)
        for i in array:
            text += i
            text += ' '
        return text