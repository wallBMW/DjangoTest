"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    
    
    EXAMPLE URL: http://www.mysite.com/post/12345/ where 12345 is the post number
    SUMMARIZED WITH: ^post/(\d+)/$
    
    ^ for beginning of text
    $ for end of text
    \d for digit
    + to indicate that the previous item should be repeated at least once
    () to capture part of the pattern
    
    ^post/ tells Django to take anything that has post/ at the beggining of the url
    (\d+) means that there will be a number of one or more digits and that we want the number captured and extracted
    / tells django that another / character should follow in the url
    $ indicated the end of the URL meaning that only strings ending with the / will match this pattern
"""

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]
