from rhyming_scheme import RhymingScheme
from tokenizer_helper import TokenizerHelper
from transformers import PreTrainedTokenizer


class PoetryMaskedTemplateFactory:
    def __init__(
        self, tokenizer_helper: TokenizerHelper, tokenizer: PreTrainedTokenizer
    ):
        self.__tokenizer_helper = tokenizer_helper
        self.__tokenizer = tokenizer

    def create_template(
        self, prompt: str, rhyming_scheme: RhymingScheme, rhyme_pairs
    ) -> list:
        if rhyming_scheme == RhymingScheme.ABAB:
            return self.__create_abab_templae(prompt, rhyme_pairs)
        elif rhyming_scheme == RhymingScheme.AABB:
            return self.__create_aabb_templae(prompt, rhyme_pairs)
        elif rhyming_scheme == RhymingScheme.ABBA:
            return self.__create_abba_templae(prompt, rhyme_pairs)
        raise Exception(f"Unknown value for rhyming scheme '{rhyming_scheme}'")

    def __create_abab_templae(self, prompt, rhyme_pairs):
        base, complementary = rhyme_pairs
        return [
            self.__tokenizer.encode(prompt, add_special_tokens=False),
            self.__create_masked_line(prompt, complementary[0]),
            self.__create_masked_line(prompt, base[1]),
            self.__create_masked_line(prompt, complementary[1]),
        ]

    def __create_aabb_templae(self, prompt, rhyme_pairs):
        base, complementary = rhyme_pairs
        return [
            self.__tokenizer.encode(prompt, add_special_tokens=False),
            self.__create_masked_line(prompt, base[1]),
            self.__create_masked_line(prompt, complementary[0]),
            self.__create_masked_line(prompt, complementary[1]),
        ]

    def __create_abba_templae(self, prompt, rhyme_pairs):
        base, complementary = rhyme_pairs
        return [
            self.__tokenizer.encode(prompt, add_special_tokens=False),
            self.__create_masked_line(prompt, complementary[0]),
            self.__create_masked_line(prompt, complementary[1]),
            self.__create_masked_line(prompt, base[1]),
        ]

    def __create_masked_line(self, prompt, rhyme):
        tokenized_prompt = self.__tokenizer.encode(prompt, add_special_tokens=False)
        tokenized_rhyme = self.__tokenizer.encode(rhyme, add_special_tokens=False)

        if tokenized_prompt[-1] != self.__tokenizer_helper.get_comma_token():
            tokenized_prompt.append(self.__tokenizer_helper.get_comma_token())

        magic_correction = len(tokenized_rhyme) + 1
        return (
            tokenized_prompt
            + [self.__tokenizer_helper.get_mask_token()]
            * (len(tokenized_prompt) - magic_correction)
            + tokenized_rhyme
            + [self.__tokenizer_helper.get_period_token()]
        )
