from django.contrib import admin
from app01.models import BBS ,BBS_user,Category
# Register your models here.
class BBS_admin(admin.ModelAdmin):
    list_display=('title','author','summary','showsignate')
    search_fields=('title','author')
    list_filter=('create_date',)
    def showsignate(self,obj):
        return obj.author.signature
    showsignate.short_description='Signature'
"""class Useradmn(admin.StackedInline):
    model=BBS_user
    extra=1
class UseradminAdd(admin.ModelAdmin):
    inlines=[Useradmn]
 """       
admin.site.register(BBS,BBS_admin)
admin.site.register(BBS_user)
admin.site.register(Category)
