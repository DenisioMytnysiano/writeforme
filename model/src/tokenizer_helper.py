from functools import lru_cache


class TokenizerHelper:
    def __init__(self, tokenizer):
        self.__tokenizer = tokenizer

    @lru_cache
    def get_period_token(self):
        return self.__tokenizer.encode(".", add_special_tokens=False)[0]

    @lru_cache
    def get_comma_token(self):
        return self.__tokenizer.encode(",", add_special_tokens=False)[0]

    @lru_cache
    def get_mask_token(self):
        return self.__tokenizer.mask_token_id
