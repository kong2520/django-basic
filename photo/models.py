from django.db import models

# Create your models here.

# 1. 모델 : 데이터베이스 저장될 데이터가 있다면 해당 데이터를 묘사한다.
# 2. 뷰 : 계산 , 처리 - 실제 기능, 화면
# 3. URL 맵핑 : 라우팅 테이블에 기록한다. urls.py에 기록 - 주소를 지정
# 4. 화면에 보여줄 것이있다. : 템플릿작성(html)

# 장고 기본 유저 모델
# 커스터마이징을 하고 싶으면 abstract base usermodel 을 사용하게 되있다. 메뉴얼보면 쉽게 할수 있다.
from django.contrib.auth.models import User
from django.urls import reverse

class Photo(models.Model):
    # related_name : User입장에서 Photo를 가져오기 위해 이름
    # 만약에 related_name 이 없다면 User입장에서 Photo를 가져올때 photo_set 을 통해 가져온다.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()
    # auto_now_add : db 한번 등록 될때 시간을 자동으로 등록해줌
    # auto_now : 업데이트 될때 시간을 자동으로 등록
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #옵션에 대해 작성 : default = id 순서대로
    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[self.id])