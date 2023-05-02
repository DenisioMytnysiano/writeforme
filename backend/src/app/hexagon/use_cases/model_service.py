from hexagon.domain.rhyming_scheme import RhymingScheme


class ModelService:
    def generate(self, rhyming: RhymingScheme, poem_prompt: str) -> str:
        return '''
        Встала весна, чорну землю
        Сонну розбудила,
        Уквітчала її рястом,
        Барвінком укрила;
        '''
