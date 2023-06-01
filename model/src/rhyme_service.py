from abc import ABC, abstractmethod

import nltk

nltk.download("cmudict")


class RhymeService(ABC):
    @abstractmethod
    def do_rhyme(self, first: str, second: str) -> bool:
        pass


class UrainianRhymeService(RhymeService):
    def do_whyme(self, first: str, second: str) -> bool:
        return first[:-2] == second[:-2]


class EnglishRhymeService(RhymeService):
    lookup = nltk.corpus.cmudict.dict()

    def do_rhyme(self, first: str, second: str) -> bool:
        first_pronunciation = self.__to_sounds(first)
        second_pronunciation = self.__to_sounds(second)
        return self.__rhyming_pronunciations(first_pronunciation, second_pronunciation)

    def __to_sounds(self, word: str) -> list:
        if word in EnglishRhymeService.lookup:
            return "".join(EnglishRhymeService.lookup[word][0])
        return None

    def __rhyming_pronunciations(
        self, first_pronunciation: list, second_pronunciation: list
    ) -> bool:
        if not first_pronunciation or not second_pronunciation:
            return False
        return first_pronunciation[-3:] == second_pronunciation[-3:]
