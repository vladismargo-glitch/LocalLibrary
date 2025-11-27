from django.urls import path, include # Возможно, include вам пока не нужен, но path нужен
from . import views
from django.conf.urls import url # Эта строка может быть удалена, если вы больше не используете 'url()'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    # url(r'^/url/$', views.my_reused_view, {'my_template_name': 'some_path'}, name='aurl'),
    # url(r'^/anotherurl/$', views.my_reused_view, {'my_template_name': 'another_path'}, name='anotherurl'),
]

# Примечание: В современных версиях Django (3.0+) рекомендуется использовать path() вместо url()
# Например, первую строку лучше переписать как: path('', views.index, name='index'),
