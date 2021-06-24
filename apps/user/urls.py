from django.urls import path
from apps.user.views import (
    Home,
    ListSlider,
    AddSlider,
    VisualizeSlider,
    UpdateSlider,
    DeleteSlider
)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('list_sliders/', ListSlider.as_view(), name='list_sliders'),
    path('add_slider/', AddSlider.as_view(), name='add_slider'),
    path('visualize_slider/<int:id>/', VisualizeSlider.as_view(), name='visualize_slider'),
    path('update_slider/<int:id>/', UpdateSlider.as_view(), name='update_slider'),
    path('delete_slider/<int:id>/', DeleteSlider.as_view(), name='delete_slider')
]