from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # blank= 유효성과 관련되어 있다. (validation-related) form.is_valid()가 호출될 때 폼 유효성 검사에 사용된다.
    # null= DB와 관련되어 있다. (database-related) 주어진 데이터베이스 컬럼이 null 값을 가질 것인지 아닌지를 정의한다.
    img = models.ImageField(upload_to='media',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # 관리자 페이지에서 보고싶은 것
    def __str__(self):
        return self.title +" " + self.content