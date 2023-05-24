# Test Task from GIS-Point

---

## Task
You are given a list of strings representing a paragraph of text. Your task is to write a Python function called 
word_frequency that takes in this list as an argument and returns a dictionary where the keys are unique words in the 
paragraph, and the values are the frequencies of those words.


#### Consider the following requirements:

- The function should treat words in a case-insensitive manner. For example, "apple" and "Apple" should be considered 
the same word.
- The function should strip leading and trailing whitespace from each word.
- The function should exclude any punctuation marks attached to words. For example, "apple." and "apple," should be 
considered the same word "apple".
- The function should exclude empty strings as words.
- The function should aim for an optimal time complexity.

---

### Example:

#### Input:
```
paragraph = [
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away."
]
```

#### Code:
```
frequency = word_frequency(paragraph)
print(frequency)
```

#### Output:
```
{
    "the": 4,
    "quick": 1,
    "brown": 1,
    "fox": 2,
    "jumps": 1,
    "over": 1,
    "lazy": 1,
    "dog": 2,
    "barks": 1,
    "and": 1,
    "runs": 1,
    "away": 1
}
```

---

In the example above, the given paragraph consists of several sentences. The word_frequency function calculates the 
frequency of each unique word, ignoring case, punctuation marks, and leading/trailing whitespace. The resulting 
dictionary contains the word frequencies.

Please write your solution in Python and provide the code for the word_frequency function.

---

## My solution to this task

```python3
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
```

---

### Explanation of the code

1. Decided to use a class to avoid problems with local variables, and to achieve the maximum structure of the code
2. I've separated the word formatting function into separate, to separate blocks of code logically
3. Tried to make the code as simple and logical as possible, without using third-party libraries like Collections
4. Added type hints for code clarity

---

### Also, the results of my code for the arguments from the example

#### Input:
```
[
   "The quick brown fox",
   "jumps over the lazy dog.",
   "The dog barks,",
   "and the fox runs away."
]
```

#### Output:
```
{
   "the": 4,
   "quick": 1,
   "brown": 1,
   "fox": 2,
   "jumps": 1,
   "over": 1,
   "lazy": 1,
   "dog": 2,
   "barks": 1,
   "and": 1,
   "runs": 1,
   "away": 1
}
```

---

### Let's try on some other paragraph

#### Input:
```
[
   "Glorious spirit of Ukraine shines and lives forever.",
   "Blessed by Fortune brotherhood will stand up together.",
   "Like the dew before the sun enemies will fade.",
   "We will further rule and prosper in our promised land."
]
```

#### Output:
```
{
   "glorious": 1,
   "spirit": 1,
   "of": 1,
   "ukraine": 1,
   "shines": 1,
   "and": 2,
   "lives": 1,
   "forever": 1,
   "blessed": 1,
   "by": 1,
   "fortune": 1,
   "brotherhood": 1,
   "will": 3,
   "stand": 1,
   "up": 1,
   "together": 1,
   "like": 1,
   "the": 2,
   "dew": 1,
   "before": 1,
   "sun": 1,
   "enemies": 1,
   "fade": 1,
   "we": 1,
   "further": 1,
   "rule": 1,
   "prosper": 1,
   "in": 1,
   "our": 1,
   "promised": 1,
   "land": 1
}
```

---

### I think I was able to complete the task