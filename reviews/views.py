from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Review, ReviewImage, ReviewVideo
from outstation.models import OutstationRoutePage
from login.models import UserProfile
from django.http import HttpResponse, JsonResponse

def review_list(request, route_id):
    if (route_id and route_id.strip and Review.objects.all().filter(route_id=route_id).exists()):
        reviews = Review.objects.all().filter(route_id=route_id)
        return render(request, 'reviews/review_list.html', {'reviews': reviews})
    return render(request, 'reviews/review_list.html',{'reviews':''})

"""def review_image_list(request, review_id):
    #print("---image list---")
    print(review_id)
    if (review_id and review_id.strip and ReviewImage.objects.all().filter(review_id=review_id).exists()):
        imagesList = ReviewImage.objects.all().filter(review_id=review_id)
        print(imagesList)
        return render(request, 'reviews/review_image_list.html', {'imagesList': imagesList})
    return render(request, 'reviews/review_image_list.html',{'imagesList':''})"""

def review(request):
    if request.method == 'POST':
        route = get_object_or_404(OutstationRoutePage, id=request.POST.get('route_id'))
        user_profile = get_object_or_404(UserProfile, user_id=request.user.id)
        user_review = Review.objects.create(
            title = request.POST.get('reviewTitle'),
            review_comments = request.POST.get('reviewComments'),
            rating = request.POST.get('reviewRating'),
            user_profile = user_profile,
            route = route
        )
        for key in request.FILES:
            if 'images' in key:
                image_file = request.FILES[key]
                ReviewImage.objects.create(image=image_file, review=user_review)
            if 'videos' in key:
                video_file = request.FILES[key]
                ReviewVideo.objects.create(video=video_file, review=user_review)
        count=route.page_review.count()
        return JsonResponse({'total_reviews':count})
        print("------------- reviews photos-----")
        for key in request.POST:
            print(key)
            value = request.POST[key]
            print(value)
        for key in request.FILES:
            print(key)
            value = request.FILES[key]
            print(value)
    return render(request, 'reviews/review.html')

"""
def photoupload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'comments/uploadphoto.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'comments/uploadphoto.html')

"""
