from django.urls import path
from . import views

app_name = 'movement'

urlpatterns = [
    # FBV
    path('post/ajax/movement_plan', views.post_Movement_Plan, name="post_movement_plan"),
    path('post/ajax/m_cp_detail', views.post_CP_Detail, name="post_cp_detail"),
    path('get/ajax/m_cp_detail', views.get_CP_Detail, name="get_cp_detail"),
    path('post/ajax/m_unit_detail', views.post_Unit_Detail, name="post_unit_detail"),
    path('get/ajax/m_unit_detail', views.get_Unit_Detail, name="get_unit_detail"),
    path('get/ajax/m_packet_detail', views.get_Packet_Detail, name="get_packet_detail"),
    # Base
    path('', views.Movement_PlanBaseView.as_view(), name="movement_base"),
    # List
    path('list/', views.Movement_PlanListView.as_view(), name="all"),
    # Detail
    path("<brigade>/<int:pk>/", views.Movement_PlanDetailView.as_view(), name="movement_single"),
    path("<brigade>/<unit>/<int:pk>/", views.Unit_DetailView.as_view(), name="unit_single"),
    # Create
    path("create_unit/", views.Create_UnitCreateListView.as_view(), name="create_unit"),
    path("create_brigade/", views.Create_BrigadeCreateListView.as_view(), name="create_brigade"),
    path("create_movement_plan/", views.Create_Movement_PlanView.as_view(), name="create_movement_plan"),
    path("allocate_new_cp/", views.Create_CP_DetailCreateListView.as_view(), name="allocate_new_cp"),
    path("allocate_new_unit/", views.Create_Unit_DetailCreateListView.as_view(), name="allocate_new_unit"),
    path("allocate_new_packet/", views.Create_Packet_DetailCreateListView.as_view(), name="allocate_new_packet"),
    # Edit
    path("update_delete_unit_list/", views.Edit_Unit_ListView.as_view(), name="update_delete_unit_list"),
    path("update_delete_brigade_list/", views.Edit_Brigade_ListView.as_view(), name="update_delete_brigade_list"),
    path("update_delete_movement_plan_list/", views.Edit_Movement_PlanListView.as_view(),
         name="update_delete_movement_plan_list"),
    path("update_delete_cp_detail_list/", views.Edit_CP_DetailListView.as_view(), name="update_delete_cp_detail_list"),
    path("update_delete_unit_detail_list/", views.Edit_Unit_DetailListView.as_view(),
         name="update_delete_unit_detail_list"),
    path("update_delete_packet_detail_list/", views.Edit_Packet_DetailListView.as_view(),
         name="update_delete_packet_detail_list"),
    # Update
    path("update_unit_<int:pk>/", views.Update_UnitView.as_view(), name="update_unit"),
    path("update_brigade_<int:pk>/", views.Update_BrigadeView.as_view(), name="update_brigade"),
    path("update_movement_plan_<int:pk>/", views.Update_Movement_PlanView.as_view(), name="update_movement_plan"),
    path("update_cp_detail_<int:pk>/", views.Update_CP_DetailView.as_view(), name="update_cp_detail"),
    path("Update_unit_detail_<int:pk>/", views.Update_Unit_DetailView.as_view(), name="update_unit_detail"),
    path("update_packet_detail_<int:pk>/", views.Update_Packet_DetailView.as_view(), name="update_packet_detail"),
    # Delete
    path("delete_unit_<int:pk>/", views.Delete_UnitView.as_view(), name="delete_unit"),
    path("delete_brigade_<int:pk>/", views.Delete_BrigadeView.as_view(), name="delete_brigade"),
    path("delete_movement_plan_<int:pk>/", views.Delete_Movement_PlanView.as_view(), name="delete_movement_plan"),
    path("delete_cp_detail_<int:pk>/", views.Delete_CP_DetailView.as_view(), name="delete_cp_detail"),
    path("delete_unit_detail_<int:pk>/", views.Delete_Unit_DetailView.as_view(), name="delete_unit_detail"),
    path("delete_packet_detail_<int:pk>/", views.Delete_Packet_DetailView.as_view(), name="delete_packet_detail"),
]
