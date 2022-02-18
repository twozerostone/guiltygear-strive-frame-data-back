from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router

from GGST_framedata.core.frame.schema import CharacterIn, CharacterOut, CharacterPatch

from .models import Character

router = Router()


@router.post('/character', response={201: CharacterOut})
def create_character(request, item: CharacterIn):
    character = Character.objects.create(**item.dict())
    character.save()
    return character


@router.get('/character/{character_id}', response=CharacterOut)
def get_character(request, character_id: int):
    character = get_object_or_404(Character, id=character_id)
    return character


@router.patch('/character/{character_id}', response=CharacterOut, exclude_none=True, exclude_unset=True)
def get_character(request, character_id: int, item: CharacterPatch):
    character = get_object_or_404(Character, id=character_id)
    for attr, val in item.dict(exclude_none=True).items():
        setattr(character, attr, val)
    character.save()
    return character


@router.get('/character', response=List[CharacterOut])
def list_character(request):
    character = Character.objects.prefetch_related("move").all()
    return character
