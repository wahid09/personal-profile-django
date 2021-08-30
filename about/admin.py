from django.contrib import admin
from about.models import About
from about.models import SocialLink
from about.models import Experience
from about.models import Project
from about.models import Education
from about.models import Skills
from about.models import Interest
from about.models import prifileImage

# Register your models here.
class aboutModel(admin.ModelAdmin):
    list_display = ["__str__", "designation", "address", "objective", "phone_number", "email", "active"]
    search_fields = ["__str__", "designation"]
    list_filter = ["name", "designation"]
    class Meta:
        Model = About
admin.site.register(About, aboutModel)

class socialLinkModel(admin.ModelAdmin):
    list_display = ["linked_id", "github_link", "tweeter_link", "facebook_link"]
    class Meta:
        Model = SocialLink
admin.site.register(SocialLink, socialLinkModel)

class experienceModel(admin.ModelAdmin):
    list_display = ["position", "company_name", "from_date", "to_date", "till_now", "active"]
    list_filter = ["position", "from_date", "till_now"]
    search_fields = ["position", "from_date"]
    class Meta:
        Model=Experience

admin.site.register(Experience, experienceModel)

class projectModel(admin.ModelAdmin):
    list_display = ["project_name", "technologies", "short_note", "live_url", "active"]
    list_filter = ["project_name", "technologies"]
    search_fields = ["project_name", "technologies"]
    class Meta:
        Model = Project

admin.site.register(Project, projectModel)

class educationModel(admin.ModelAdmin):
    list_display = ["degree_name", "subject_name", "institute", "from_date", "to_date", "till_now", "active"]
    list_filter = ["degree_name", "from_date"]
    search_fields = ["degree_name", "institute"]
    class Meta:
        Model = Education

admin.site.register(Education, educationModel)


class skillModel(admin.ModelAdmin):
    list_filter = ["backend_framwork", "frontend_framwork"]
    list_display = ["backend_language","backend_framwork", "frontend_language","frontend_framwork", "database", "active"]
    search_fields = ["backend_language","backend_framwork"]
    class Meta:
        Model: Skills
admin.site.register(Skills, skillModel)


class interestModel(admin.ModelAdmin):
    list_display = ["interest", "active"]
    class Meta:
        Model: Interest
admin.site.register(Interest, interestModel)

admin.site.register(prifileImage)