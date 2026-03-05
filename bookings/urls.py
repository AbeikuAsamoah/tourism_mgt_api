from django.urls import path
from .views import BookingListView, BookingCreateView, BookingCancelView

urlpatterns = [
        path('', BookingListView.as_view(), name='booking_list'),
        path('create/', BookingCreateView.as_view(), name='booking_create'),
        path('cancel/<int:pk>/', BookingCancelView.as_view(), name='booking_cancel'),
]
