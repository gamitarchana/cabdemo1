from .models import UserProfile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.conf import settings

def save_profile(backend, user, response, *args, **kwargs):
    #print("----backend-------")
    #print(isinstance(backend,settings.GOOGLE_BACKEND))
    #social = user.social_auth.get(provider='google-oauth2')
    #print(social)
    #print(backend.name)
    #print(backend.__name__)
    #print(backend.name== settings.GOOGLE_OAUTH2)
    #print("----endh-------")
    user_profile_url=''
    if(backend.name== settings.GOOGLE_OAUTH2):
        user_profile_url = response['picture']

    if(UserProfile.objects.filter(user_id=user.id).exists()):
        userprofile = get_object_or_404(UserProfile, user_id = user.id)
        userprofile.profile_photo_url=user_profile_url
        userprofile.save()
        userprofile.save_image()
    else:
        userprofile = UserProfile.objects.create(
            user=user,
            profile_photo_url = user_profile_url
        )
        userprofile.save_image()
        #print("user profile new")
