from django.shortcuts import render
from django.shortcuts import HttpResponse
from ..models import About, Education, Experience, Project, SocialLink, Skills, Interest, prifileImage

def home(request):
    about = About.objects.first()
    project = Project.objects.filter(active=True)
    sociale = SocialLink.objects.first()
    experience = Experience.objects.filter(active=True)
    education = Education.objects.filter(active=True)
    skill = Skills.objects.first()
    interest = Interest.objects.first()
    profile_image = prifileImage.objects.first()
    context = {
        'about': about,
        'project': project,
        'sociale': sociale,
        'experience': experience,
        'education': education,
        'skill': skill,
        'interest': interest,
        'profile_image': profile_image
    }
    return render(request,'profile/profile_content.html', context)