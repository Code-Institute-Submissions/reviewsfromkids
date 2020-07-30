from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='books'), # 8.1
    path('<book_id>', views.book_detail, name='book_detail'), # 10.6
    path('', views.all_books, name='book_search'),
    # path('', views.testFilterView, name='test_filter_view'),
]