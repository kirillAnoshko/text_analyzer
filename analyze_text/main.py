import re
import pymorphy3
from typing import NoReturn

class TextAnalyze:
    def __init__(self, file_name=None):
        if file_name is None:
            raise Exception("Не указан файл для анализа!")
        self.read_file(file_name)
        self.check_empty_text()
        self.prepare_text()
        self.make_analyzed_words()
        self.print_text()

    def read_file(self, file_name) -> None | NoReturn:
        """ пытается открыть файл и считать его в строку """
        try:
            with open(file_name, "r", encoding="UTF-8") as content:
                self.file = content  # здесь получается файловый объект
                self.text = self.file.read()  # здесь получается строка текста
        except FileNotFoundError:
            raise Exception(f"Файл {file_name} не найден!")

    def check_empty_text(self):
        if not self.text:
            raise RuntimeError(f"Файл {self.file} пуст, попробуйте другой файл")

    def prepare_text(self):
        self.words = self.text.split()
        self.text = self.text.lower()
        self.clean_text = ''.join(re.findall(r'[\w\s-]', self.text))

    def make_analyzed_words(self, part_of_speech=["VERB", "NOUN"]) -> list:
        self.analyzed_words = []
        morph = pymorphy3.MorphAnalyzer()
        for word in self.words:
            parsed_word = morph.parse(word)[0]
            if parsed_word.tag.POS in part_of_speech:
                self.analyzed_words.append(parsed_word.normal_form)
                    
    def print_text(self):
        """ выводит строку текста на экран """
        print(self.clean_text)
        print(f"Проанализированные слова: {self.analyzed_words}")
        print(f"В этом тексте {len(self.words)} слов")
        print(f"В этом тексте {len(self.analyzed_words)} проанализированных слов")


TextAnalyze(file_name="text.txt")

                
            

                
