from django.contrib import admin

# ////video embed details
from embed_video.admin import AdminVideoMixin
from .models import Video_upload
from .models import Rooms
from .models import Response
from .models import Assignment
from .models import Assignment_submission
from .models import Report 
from .models import GradeStudent 
from .models import GradeStudent 


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


# admin.site.register(Video_upload, MyModelAdmin)
# ///


# Register your models here.
admin.site.register(Video_upload)
admin.site.register(Rooms)
admin.site.register(Response)
admin.site.register(Assignment)
admin.site.register(Assignment_submission)
admin.site.register(Report)
admin.site.register(GradeStudent)
