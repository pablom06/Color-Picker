
from django.urls import path

from color_picker.views import ColorPickerView

urlpatterns = [
    path('', ColorPickerView.as_view(), name='paint'),
]
