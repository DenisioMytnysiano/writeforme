from abc import ABC, abstractmethod

import fasttext.util
import gensim.downloader as api
import numpy as np
from utils import cosine_similarity


class RelatedWordsExtractor(ABC):
    def get_related_words(self, sentence, top_n=5):
        sentence_embedding = self._get_sentence_embedding(sentence)
        word_similarities = self._calculate_word_similarities(sentence_embedding)
        related_words = self._get_top_similar_words(word_similarities, top_n)
        return related_words

    def _get_sentence_embedding(self, sentence):
        sentence_tokens = sentence.split()
        word_vectors = []
        for token in sentence_tokens:
            if token in self._get_all_words():
                word_vectors.append(self._get_word_vector(token))
        if len(word_vectors) == 0:
            return None
        return np.mean(word_vectors, axis=0)

    def _calculate_word_similarities(self, sentence_embedding):
        word_similarities = []
        if sentence_embedding is None:
            return word_similarities
        for word in self._get_all_words():
            word_embedding = self._get_word_vector(word)
            similarity = cosine_similarity(sentence_embedding, word_embedding)
            word_similarities.append((word, similarity))
        return word_similarities

    def _get_top_similar_words(self, word_similarities, top_n):
        sorted_similarities = sorted(
            word_similarities, key=lambda x: x[1], reverse=True
        )
        top_similar_words = [word for word, _ in sorted_similarities[:top_n]]
        return top_similar_words

    @abstractmethod
    def _get_all_words(self) -> list:
        pass

    @abstractmethod
    def _get_word_vector(self, word: str) -> list:
        pass


class UkrainianRelatedWordsExtractor(RelatedWordsExtractor):
    def __init__(self):
        self.fast_text = fasttext.load_model("fiction.cased.tokenized.glove.300d.bz2")

    def _get_all_words(self) -> list:
        return self.fast_text.get_words()

    def _get_word_vector(self, word: str) -> list:
        return self.fast_text.get_word_vector(word)


class EnglishRelatedWordsExtractor(RelatedWordsExtractor):
    def __init__(self):
        self.word2vec_model = api.load("glove-twitter-25")

    def _get_all_words(self) -> list:
        return self.word2vec_model.wv.vocab

    def _get_word_vector(self, word: str) -> list:
        return self.word2vec_model.wv[word]