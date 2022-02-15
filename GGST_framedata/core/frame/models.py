from uuid import uuid4
import os

from django.db import models
from django.core.validators import MinValueValidator


def upload_to(instance, filename):
    uuid_name = uuid4().hex
    character = instance.move.character.eng_name
    ext = os.path.splitext(filename)[-1].lower()
    return '/'.join([
        character,
        uuid_name + ext,
    ])


class Character(models.Model):
    WEIGHT_CHOICES = (
        ('Light', 'Light'),
        ('Normal', 'Normal'),
        ('Heavy', 'Heavy')
    )
    eng_name = models.CharField(
        verbose_name='영문캐릭터명', max_length=100, unique=True)
    kor_name = models.CharField(
        verbose_name='한글캐릭터명', max_length=200, unique=True)
    description = models.TextField(verbose_name='캐릭터 설명')
    defence = models.FloatField(verbose_name='방어')
    guts = models.IntegerField(verbose_name='근성치', validators=[
                               MinValueValidator(0)])
    prejump = models.IntegerField(
        verbose_name='점프이행', validators=[MinValueValidator(0)])
    backdash = models.IntegerField(
        verbose_name='백대시프레임', validators=[MinValueValidator(0)])
    backdash_invuln = models.IntegerField(
        verbose_name='백대시무적', validators=[MinValueValidator(0)])
    weight = models.CharField(
        verbose_name='무게', choices=WEIGHT_CHOICES, max_length=10)

    class Meta:
        db_table = 'character'
        verbose_name = '캐릭터'
        verbose_name_plural = '캐릭터'


class Guard(models.Model):
    direction = models.CharField(verbose_name='가드방향', max_length=100)

    class Meta:
        db_table = 'guard'
        verbose_name = '가드방향'
        verbose_name_plural = '가드방향'


class Move(models.Model):
    character = models.ForeignKey(
        Character, verbose_name='캐릭터', on_delete=models.CASCADE, related_name='move')
    command = models.CharField(verbose_name='커맨드', max_length=100)
    name = models.CharField(verbose_name='기술명', blank=True, max_length=100)
    damage = models.IntegerField(verbose_name='데미지')
    guard = models.ManyToManyField(
        Guard, verbose_name='가드방향', through='MoveGuard')
    start = models.IntegerField(
        verbose_name='이행프레임', validators=[MinValueValidator(0)])
    active = models.IntegerField(
        verbose_name='지속프레임', validators=[MinValueValidator(0)])
    recovery = models.IntegerField(
        verbose_name='회복프레임', validators=[MinValueValidator(0)])
    on_block = models.IntegerField(verbose_name='가드시프레임')
    description = models.TextField(verbose_name='기술 설명', null=True, blank=True)

    class Meta:
        db_table = 'move'
        verbose_name = '기술'
        verbose_name_plural = '기술'


class MoveFile(models.Model):
    move = models.ForeignKey(
        Move, verbose_name='기술', on_delete=models.CASCADE, related_name='move_image')
    file = models.FileField(verbose_name='이미지', upload_to=upload_to)

    class Meta:
        db_table = 'move_file'
        verbose_name = '기술이미지'
        verbose_name_plural = '기술이미지'


class MoveGuard(models.Model):
    move = models.ForeignKey(
        Move, verbose_name='기술', on_delete=models.CASCADE)
    guard = models.ForeignKey(
        Guard, verbose_name='가드방향', on_delete=models.CASCADE)

    class Meta:
        db_table = 'move_guard'
