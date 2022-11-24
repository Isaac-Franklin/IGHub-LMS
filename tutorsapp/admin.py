from django.contrib import admin
from .models import Scores
from .models import Quiz
from .models import Answer

# Register your models here.
admin.site.register(Scores)
admin.site.register(Quiz)
admin.site.register(Answer)
