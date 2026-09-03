from django.db import models

# Create your models here.
from django.db import models

from django.db import models

# വാർത്തകൾ/പോസ്റ്റുകൾ സേവ് ചെയ്യാനുള്ള ടേബിൾ ഉണ്ടാക്കുന്നു
class Post(models.Model):
    title = models.CharField(max_length=200)      # തലക്കെട്ട് എഴുതാനുള്ള കോളം
    content = models.TextField()                  # വാർത്തയുടെ മുഴുവൻ വിവരണം എഴുതാനുള്ള വലിയ കോളം
    author = models.CharField(max_length=100)     # എഴുതിയ ആളുടെ പേര്
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blog_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # പോസ്റ്റ് ഇട്ട സമയം തനിയെ സേവ് ആകും

    # അഡ്മിൻ പാനലിൽ വാർത്തയുടെ പേര് കാണിക്കാൻ
    def __str__(self):
        return self.title