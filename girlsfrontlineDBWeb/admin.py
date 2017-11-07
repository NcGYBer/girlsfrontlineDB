from django.contrib import admin
from .models import DollRank, WeaponType, VoiceActor, Illustrator, DollSkillType, DollBuffType, DollBuff, TacticalDoll


# Register your models here.
class DollBuffInline(admin.TabularInline):
    model = DollBuff
    extra = 0


class TacticalDollAdmin(admin.ModelAdmin):
    list_display = ("name", "num", "rank", "weapon_type")
    list_filter = ("rank", "weapon_type")
    ordering = ("num",)
    inlines = [DollBuffInline]


class DollRankAdmin(admin.ModelAdmin):
    list_display = ("name", "num_star")
    ordering = ("num_star",)


class DollSkillTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "weapon_type", "skill_description")


admin.site.register(TacticalDoll, TacticalDollAdmin)
admin.site.register(DollRank, DollRankAdmin)
admin.site.register(WeaponType)
admin.site.register(VoiceActor)
admin.site.register(Illustrator)
admin.site.register(DollSkillType, DollSkillTypeAdmin)
admin.site.register(DollBuffType)
# admin.site.register(DollBuff)


