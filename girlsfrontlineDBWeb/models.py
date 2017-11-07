from django.db import models



# Create your models here.
class DollRank(models.Model):
    num_star = models.IntegerField(verbose_name="별 개수", primary_key=True, null=False, blank=False)
    name = models.CharField(verbose_name="등급 이름", max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name


class WeaponType(models.Model):
    name = models.CharField(verbose_name="총기 종류", max_length=3, null=False, blank=False)

    def __str__(self):
        return self.name


class VoiceActor(models.Model):
    name = models.CharField(verbose_name="이름", max_length=30, null=False, blank=False)
    name_ko = models.CharField(verbose_name="한글 이름", max_length=30, null=False, blank=True)
    name_en = models.CharField(verbose_name="영문 이름", max_length=30, null=False, blank=True)

    def __str__(self):
        return self.name


class Illustrator(models.Model):
    name = models.CharField(verbose_name="이름", max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name


class DollSkillType(models.Model):
    name = models.CharField(verbose_name="스킬 이름", max_length=20, null=False, blank=False)
    weapon_type = models.ForeignKey(verbose_name="총기 종류", to=WeaponType)
    skill_description = models.TextField(verbose_name="스킬 설명", null=False, blank=False)

    def __str__(self):
        return self.name


class DollBuffType(models.Model):
    name = models.CharField(verbose_name="버프 종류", max_length=5, null=False, blank=False)

    def __str__(self):
        return self.name


class TacticalDoll(models.Model):
    name = models.CharField(verbose_name="이름", max_length=30, null=False, blank=False)
    img_normal = models.ImageField(verbose_name="기본 이미지", null=True, blank=False)
    img_destroyed = models.ImageField(verbose_name="중상 이미지", null=True, blank=False)
    description = models.TextField(verbose_name="설명", null=False, blank=False)
    num = models.IntegerField(verbose_name="번호", primary_key=True, null=False, blank=False)
    rank = models.ForeignKey(verbose_name="등급", to=DollRank, null=False, blank=False)
    weapon_type = models.ForeignKey(verbose_name="총기 종류", to=WeaponType, related_name="weapon_type")
    weapon_name = models.CharField(verbose_name="실제 총기명", max_length=30, null=False, blank=False)
    voice = models.ForeignKey(verbose_name="성우", to=VoiceActor)
    illustrator = models.ForeignKey(verbose_name="일러스트", to=Illustrator)
    skill_name = models.ForeignKey(verbose_name="스킬명", to=DollSkillType)
    skill_pre_cooldown = models.IntegerField(verbose_name="스킬 사용 대기시간", null=False, blank=False)
    skill_cooldown = models.IntegerField(verbose_name="스킬 재사용 대기시간", null=False, blank=False)
    skill_duration = models.IntegerField(verbose_name="스킬 지속시간", null=False, blank=False)
    skill_value = models.IntegerField(verbose_name="스킬 수치", null=False, blank=False)
    buff_range = models.CharField(verbose_name="버프 범위", max_length=9, null=False, blank=False)
    buff_target = models.ForeignKey(verbose_name="버프 대상", to=WeaponType, related_name="buff_target")
    # buff_type = models.ForeignKey(verbose_name="버프 종류", to=DollBuff)

    def __str__(self):
        return self.name


class DollBuff(models.Model):
    name = models.ForeignKey(verbose_name="버프 종류", to=DollBuffType)
    value = models.IntegerField(verbose_name="버프 수치", null=False, blank=False)
    doll = models.ForeignKey(verbose_name="전술 인형", to=TacticalDoll, null=True)

    def __str__(self):
        return str(self.name)
