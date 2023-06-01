from languages import Languages
from poetry_model_factory import PoetryModelFactory
from rhyming_scheme import RhymingScheme

LANGUAGE = Languages.English
PROMPT = "The birds are flying in the sky"
RHYMING_SCHEME = RhymingScheme.ABAB

if __name__ == "__main__":
    model = PoetryModelFactory().for_language(LANGUAGE)
    poem = model.generate(PROMPT, RHYMING_SCHEME)
    print(poem)
