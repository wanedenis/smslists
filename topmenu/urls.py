from django.conf.urls import url
import views

app_name = "topmenu"

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^menu_2/$', views.menu_2, name='menu_2'),
	url(r'^listings/(?P<category>\w+)/', views.listings, name='listings'),
	url(r'^session_flush/$', views.session_flush, name='session_flush'),
	url(r'^invalid_response/$', views.invalid_response, name='invalid_response'),
	url(r'^listing/(?P<category>\w+)/(?P<listing_id>\d+)/', views.listing_detail, name='listing_detail'),
	url(r'^post_subject_request/(?P<category>\w+)/', views.post_subject_request, name='post_subject_request'),
	url(r'^post_description_request/(?P<category>\w+)/', views.post_description_request, name='post_description_request'),
	url(r'^post_review/(?P<category>\w+)/', views.post_review, name='post_review'),
	url(r'^post_commit/(?P<category>\w+)/', views.post_commit, name='post_commit'),
	]
