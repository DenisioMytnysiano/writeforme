import nltk
from nltk.corpus import stopwords
from related_words_extractor import RelatedWordsExtractor
from rhyme_service import RhymeService

nltk.download('stopwords')
STOPWORDS = stopwords.words('english')

class RhymePairsProvider:
    def __init__(
        self,
        related_words_extractor: RelatedWordsExtractor,
        rhyme_service: RhymeService,
    ):
        self.__related_words_extractor = related_words_extractor
        self.__rhyme_service = rhyme_service

    def get(self, input_sentence: str) -> list:
        related_words = self.__related_words_extractor.get_related_words(input_sentence, 1000)
        return self.__extract_rhyming_pairs(input_sentence, related_words)

    def __extract_rhyming_pairs(self, prompt, related_words):
        base_rhymes = self.__get_base_rhyme(prompt, related_words)
        complementary_rhymes = self.__get_complementary_rhyme(related_words)
        return (base_rhymes, complementary_rhymes)

    def __get_base_rhyme(self, prompt, related_words):
        last_word = prompt.split(" ")[-1]
        rhyme = self.__get_rhyming_word(last_word, related_words)
        return last_word, rhyme

    def __get_complementary_rhyme(self, related_words):
        for word in related_words:
            rhyme = self.__get_rhyming_word(word, related_words)
            if rhyme:
                return word, rhyme
        return None, None

    def __get_rhyming_word(self, word, rhyming_words):
        if word in STOPWORDS:
            return None
        for rhyme_candidate in rhyming_words:
            if rhyme_candidate != word and self.__rhyme_service.do_rhyme(word, rhyme_candidate):
                return rhyme_candidate
        return None
