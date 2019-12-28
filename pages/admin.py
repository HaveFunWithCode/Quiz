from django.contrib import admin
from .models import Questions
from .models import User
from .models import Exam


# Register your models here.
admin.site.register(Questions)
admin.site.register(User)
admin.site.register(Exam)