from json import dumps
from string import punctuation


class WordFrequency:
    def __init__(self, paragraph: list[str, ...]):
        self.paragraph: list[str, ...] = paragraph

    @staticmethod
    def format_word(word: str) -> str:
        return ''.join([char for char in word if char not in punctuation]).lower()

    def word_frequency(self) -> dict[str, int]:
        result: dict[str, int] = {}
        for sentence in self.paragraph:
            for raw_word in sentence.split():
                word: str = self.format_word(word=raw_word)
                result[word]: int = result.get(word, 0) + 1
        return result

    def __call__(self) -> dict:
        return self.word_frequency()


if __name__ == '__main__':
    paragraph_: list[str, ...] = [
        "The quick brown fox",
        "jumps over the lazy dog.",
        "The dog barks,",
        "and the fox runs away."
    ]
    print('Input:', dumps(obj=paragraph_, indent=3), sep='\n', end='\n\n')
    word_frequency: WordFrequency = WordFrequency(paragraph=paragraph_)
    frequency: dict[str, int] = word_frequency()
    print('Output:', dumps(obj=frequency, indent=3), sep='\n')
