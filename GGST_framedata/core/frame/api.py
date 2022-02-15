from enum import Enum
from typing import List
from django.shortcuts import get_object_or_404
from ninja import Field, ModelSchema, Router, Schema
from pydantic import PositiveInt

from .models import Character, Move

router = Router()


class CharacterIn(ModelSchema):
    class Config:
        model = Character
        model_fields = ["id", "eng_name", "kor_name", "description", "defence",
                        "guts", "prejump", "backdash", "backdash_invuln", "weight"]


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


@router.post('/character', response={201: CharacterOut})
def create_character(request, item: CharacterIn):
    character = Character.objects.create(**item.dict())
    character.save()
    return 201, character


@router.get('/character/{character_id}', response=CharacterOut)
def get_character(request, character_id: int):
    character = get_object_or_404(Character, id=character_id)
    return character


@router.get('/character', response=List[CharacterOut])
def list_character(request):
    character = Character.objects.prefetch_related("move").all()
    return character
