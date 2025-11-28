from django.urls import path, include # Возможно, include вам пока не нужен, но path нужен
from . import views
from django.conf.urls import url # Эта строка может быть удалена, если вы больше не используете 'url()'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),url(r'^borrowed/$', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
    # url(r'^/url/$', views.my_reused_view, {'my_template_name': 'some_path'}, name='aurl'),
    # url(r'^/anotherurl/$', views.my_reused_view, {'my_template_name': 'another_path'}, name='anotherurl'),
]

urlpatterns += [
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]


