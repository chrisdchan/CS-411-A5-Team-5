from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'patients', views.PatientViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'trainings', views.TrainingViewSet)
router.register(r'resources', views.ResourcesViewSet)
router.register(r'nested', views.NestedViewSet)


urlpatterns = [

    path('api/', include(router.urls)),
    path('', views.index, name="index"),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('patientcreate/', views.PatientCreate.as_view(), name='patientcreate'),
    path('exercisecreate/', views.ExerciseCreate.as_view(), name='exercisecreate'),
    path('resourcecreate/', views.ResourceCreate.as_view(), name='resourcecreate'),
    path('audiocreate/', views.AudioCreate.as_view(), name='audiocreate'),
    path('coursecreate/', views.CourseCreate.as_view(), name='coursecreate'),
    path('course/<pk>/', views.CourseDetail.as_view(), name='coursedetail'),
    path('audio/<pk>/', views.AudioDetail.as_view(), name='audiodetail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)