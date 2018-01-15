# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# from django.conf import settings
# from django.conf.urls import include, url
# from django.contrib import admin
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# urlpatterns = [url(r'^', include('polls.urls')),
#                url(r'^admin/', admin.site.urls)]

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^', include('projects.urls')),
    
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),    
    # url(r'^', include('pages.urls', namespace="pages")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# This enables static files to be served from the Gunicorn server
# In Production, serve static files from Google Cloud Storage or an alternative
# CDN
# if settings.DEBUG:
#     urlpatterns += staticfiles_urlpatterns()
