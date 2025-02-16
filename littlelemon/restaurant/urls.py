from django.urls import path


from .views import index, MenuItemView, SingleMenuItemView, BookingViewSet

urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('booking/', BookingViewSet.as_view()),
    path('booking/<int:pk>', BookingViewSet.as_view()),
    
]
