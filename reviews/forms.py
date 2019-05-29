from django import forms


"""class ReviewForm(forms.Form):
    title = forms.CharField(max_length=100)
    review_comments = forms.CharField(widget=forms.Textarea)
    rating = forms.IntegerField()
    publish_date = forms.DateField()
    image_field = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    video_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'review_comments', 'rating')"""
