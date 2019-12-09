from django.contrib import admin
from .models import Direksi, Mentee, Mentor, MataPelajaran, LiveCode, Challange

# Register your models here.
admin.site.register(Direksi)
admin.site.register(Mentee)
admin.site.register(Mentor)
admin.site.register(MataPelajaran)
admin.site.register(LiveCode)
admin.site.register(Challange)

