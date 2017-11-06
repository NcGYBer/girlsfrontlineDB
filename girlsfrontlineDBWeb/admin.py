from django.contrib import admin
from .models import DollRank, WeaponType, VoiceActor, Illustrator, DollSkillType, DollBuffType, DollBuff, TacticalDoll


# Register your models here.
class DollBuffInline(admin.TabularInline):
    model = DollBuff
    extra = 0


class TacticalDollAdmin(admin.ModelAdmin):
    inlines = [DollBuffInline]


admin.site.register(TacticalDoll, TacticalDollAdmin)
admin.site.register(DollRank)
admin.site.register(WeaponType)
admin.site.register(VoiceActor)
admin.site.register(Illustrator)
admin.site.register(DollSkillType)
admin.site.register(DollBuffType)
# admin.site.register(DollBuff)


