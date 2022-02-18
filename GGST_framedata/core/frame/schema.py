from wsgiref.validate import validator
from ninja import ModelSchema, Schema

from GGST_framedata.core.modules import optional
from .models import Character, Move


class CharacterIn(ModelSchema):
    @validator("eng_name", check_fields=False, allow_reuse=True)
    def eng_name_check(cls, v: str):
        if not v.encode().isalnum():
            raise ValueError(f'{v} is not English or Number')
        return v

    class Config:
        model = Character
        model_fields = ["id", "eng_name", "kor_name", "description", "defence",
                        "guts", "prejump", "backdash", "backdash_invuln", "weight"]


@optional
class CharacterPatch(CharacterIn):
    pass


class MoveSchema(ModelSchema):
    class Config:
        model = Move
        model_fields = ["id", "command", "name", "damage",
                        "start", "active", "recovery", "on_block", "description"]


class CharacterOut(Schema):
    id: int
    eng_name: str
    kor_name: str
    description: str
    defence: float
    guts: int
    prejump: int
    backdash: int
    backdash_invuln: int
    weight: str
