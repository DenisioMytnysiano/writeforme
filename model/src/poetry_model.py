import numpy as np
import tensorflow as tf
from poetry_masked_template_factory import PoetryMaskedTemplateFactory
from rhyme_pairs_provider import RhymePairsProvider
from rhyming_scheme import RhymingScheme
from transformers import PreTrainedTokenizer, TFBertForPreTraining


class PoetryModel:
    def __init__(
        self,
        model: TFBertForPreTraining,
        tokenizer: PreTrainedTokenizer,
        template_factory: PoetryMaskedTemplateFactory,
        rhyming_pairs_provider: RhymePairsProvider,
    ):
        self.__rhyming_pairs_provider = rhyming_pairs_provider
        self.__model = model
        self.__tokenizer = tokenizer
        self.__template_factory = template_factory

    def generate(self, prompt: str, rhyming_scheme: RhymingScheme) -> str:
        rhyme_pairs = self.__rhyming_pairs_provider.get(prompt)
        template = self.__template_factory.create_template(
            prompt, rhyming_scheme, rhyme_pairs
        )
        padded_template = tf.keras.preprocessing.sequence.pad_sequences(
            template, padding="post", value=self.__tokenizer.pad_token_id
        )
        return self._fill_template(padded_template)

    def _fill_template(self, template):
        predicted_masks = self.__model(tf.constant(template))[0]
        for i, token_ids in enumerate(template):
            idxs = np.where(token_ids == self.__tokenizer.mask_token_id)[0]
            for replace_ix in idxs:
                token_ids[replace_ix] = self._extract_mask_value(
                    predicted_masks[i], replace_ix
                )
                template[i] = token_ids
        return self._decode_template(template)

    def _extract_mask_value(self, predictions, replace_ix):
        probas = tf.nn.softmax(predictions[replace_ix]).numpy()
        probas /= probas.sum()
        return np.random.choice(range(len(probas)), p=probas)

    def _decode_template(self, template):
        result = []
        for i in range(0, len(template)):
            line = self.__tokenizer.convert_tokens_to_string(
                    self.__tokenizer.convert_ids_to_tokens(
                        template[i], skip_special_tokens=True
                    )
            )
            if i != 0:
                line = line.split(",")[1].strip()
            result.append(line)
        return result
