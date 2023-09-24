from django.contrib import admin

# Register your models here.
# adminのページでモデルを見れるようにするためにはここにモデルを登録する
from .models import Task

admin.site.register(Task)