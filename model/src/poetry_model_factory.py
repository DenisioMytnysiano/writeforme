from functools import lru_cache

from languages import Languages
from poetry_masked_template_factory import PoetryMaskedTemplateFactory
from poetry_model import PoetryModel
from related_words_extractor import EnglishRelatedWordsExtractor, UkrainianRelatedWordsExtractor
from rhyme_pairs_provider import RhymePairsProvider
from rhyme_service import EnglishRhymeService, UrainianRhymeService
from tokenizer_helper import TokenizerHelper
from transformers import BertTokenizer, TFBertForMaskedLM

ENGLISH_MODEL = "bert-large-cased-whole-word-masking-finetuned-squad"
UKRAINIAN_MODEL = "youscan/ukr-roberta-base"


class PoetryModelFactory:

    def for_language(self, language: Languages) -> PoetryModel:
        model, tokenizer = self.load_model(language)
        if language == Languages.English:
            return PoetryModel(
                rhyming_pairs_provider=RhymePairsProvider(
                    related_words_extractor=EnglishRelatedWordsExtractor(),
                    rhyme_service=EnglishRhymeService(),
                ),
                model=model,
                tokenizer=tokenizer,
                template_factory=PoetryMaskedTemplateFactory(
                    tokenizer_helper=TokenizerHelper(tokenizer=tokenizer),
                    tokenizer=tokenizer
                )
            )
        elif language == Languages.Ukrainian:
            return PoetryModel(
                rhyming_pairs_provider=RhymePairsProvider(
                    related_words_extractor=UkrainianRelatedWordsExtractor(),
                    rhyme_service=UrainianRhymeService(),
                ),
                model=model,
                tokenizer=tokenizer,
                template_factory=PoetryMaskedTemplateFactory(
                    tokenizer_helper=TokenizerHelper(tokenizer=tokenizer),
                    tokenizer=tokenizer
                )
            )

    @lru_cache()
    def load_model(self, language: Languages):
        if language == Languages.English:
            return (
                TFBertForMaskedLM.from_pretrained(ENGLISH_MODEL),
                BertTokenizer.from_pretrained(ENGLISH_MODEL),
            )
        elif language == Languages.Ukrainian:
            return (
                TFBertForMaskedLM.from_pretrained(UKRAINIAN_MODEL),
                BertTokenizer.from_pretrained(UKRAINIAN_MODEL),
            )
