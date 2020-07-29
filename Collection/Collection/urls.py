
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ToDo.urls')),
    path('image-upload/',include('imageupload.urls')),
    path('home',include('Frontend.urls')),
    path('account/',include('account.urls')),
    path('choice/',include('Choice.urls')),
    path('quiz/',include('Quiz.urls')),
    path('grammar/',include('grammar.urls')),
    path('wordgame',include('wordgame.urls')),
    path('query',include('Queries.urls')),
    path('subs/',include('subscription.urls')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)