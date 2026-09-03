from django import forms
# Django ഇൻബിൽറ്റ് യൂസർ ഫോം ഇമ്പോർട്ട് ചെയ്യുന്നു
from django.contrib.auth.forms import UserCreationForm
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title", "content", "author", "image"]


# പുതിയ യൂസർ രജിസ്ട്രേഷൻ ഫോം
class SignUpForm(UserCreationForm):
    pass