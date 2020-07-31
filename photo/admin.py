from django.contrib import admin
from .models import *

# Register your models here.

from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    #어떤것을 보여줄것인지
    list_display = ['id','author','created','updated']
    #raw_id_fields = ['author'] # optionbox가 아니라 실제로 text를 입력해서 찾아야함
    list_filter = ['created','updated'] #filter 목록이 나옴. 보통 기간에 많이 검
    # text나 created를 검색할 수 있음. foreignkey일때는 옵션을 더 줘야한다. foreignkey모델__하위필드
    search_fields = ['text','created','author__username']
    ordering = ['-updated','-created'] #수정일이 만약 같다면 생성일기준으로 순서

admin.site.register(Photo, PhotoAdmin)