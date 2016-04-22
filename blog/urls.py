"""
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

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'), #assigns the landing page to be a view called post_list, the regex matches an empty string
]

