from django.contrib import admin
from about.models import About
from about.models import SocialLink
from about.models import Experience
from about.models import Project
from about.models import Education

# Register your models here.
admin.site.register(About)
admin.site.register(SocialLink)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Education)