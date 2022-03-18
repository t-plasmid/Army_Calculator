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
    path('', views.Movement_PlanBaseView.as_view(), name="movement_plan_base"),
    # View
    path('list_movement_plan/', views.Movement_PlanListView.as_view(), name="list_movement_plan"),
    path("<brigade>/<int:pk>/", views.Movement_PlanDetailView.as_view(), name="detail_movement_plan"),
    path("<brigade>/<unit>/<int:pk>/", views.Unit_DetailView.as_view(), name="detail_movement_plan_by_unit"),
    # Create
    path("create_list_unit/", views.Create_UnitCreateListView.as_view(), name="create_list_unit"),
    path("create_list_brigade/", views.Create_BrigadeCreateListView.as_view(), name="create_list_brigade"),
    path("create_movement_plan/", views.Create_Movement_PlanView.as_view(), name="create_movement_plan"),
    path("create_list_mov_cp_detail/", views.Create_CP_DetailCreateListView.as_view(), name="create_list_mov_cp_detail"),
    path("create_list_mov_unit_detail/", views.Create_Unit_DetailCreateListView.as_view(), name="create_list_mov_unit_detail"),
    path("create_list_mov_packet_detail/", views.Create_Packet_DetailCreateListView.as_view(), name="create_list_mov_packet_detail"),
    # Edit
    path("list_edit_unit/", views.Edit_Unit_ListView.as_view(), name="list_edit_unit"),
    path("list_edit_brigade/", views.Edit_Brigade_ListView.as_view(), name="list_edit_brigade"),
    path("list_edit_movement_plan/", views.Edit_Movement_PlanListView.as_view(),
         name="list_edit_movement_plan"),
    path("list_edit_mov_cp_detail/", views.Edit_CP_DetailListView.as_view(), name="list_edit_mov_cp_detail"),
    path("list_edit_mov_unit_detail/", views.Edit_Unit_DetailListView.as_view(),
         name="list_edit_mov_unit_detail"),
    path("list_edit_mov_packet_detail/", views.Edit_Packet_DetailListView.as_view(),
         name="list_edit_mov_packet_detail"),
    # Update
    path("update_unit_<int:pk>/", views.Update_UnitView.as_view(), name="update_unit"),
    path("update_brigade_<int:pk>/", views.Update_BrigadeView.as_view(), name="update_brigade"),
    path("update_movement_plan_<int:pk>/", views.Update_Movement_PlanView.as_view(), name="update_movement_plan"),
    path("update_mov_cp_detail_<int:pk>/", views.Update_Mov_CP_DetailView.as_view(), name="update_mov_cp_detail"),
    path("update_mov_unit_detail_<int:pk>/", views.Update_Mov_Unit_DetailView.as_view(), name="update_mov_unit_detail"),
    path("update_mov_packet_detail_<int:pk>/", views.Update_Mov_Packet_DetailView.as_view(), name="update_mov_packet_detail"),
    # Delete
    path("delete_unit_<int:pk>/", views.Delete_UnitView.as_view(), name="delete_unit"),
    path("delete_brigade_<int:pk>/", views.Delete_BrigadeView.as_view(), name="delete_brigade"),
    path("delete_movement_plan_<int:pk>/", views.Delete_Movement_PlanView.as_view(), name="delete_movement_plan"),
    path("delete_mov_cp_detail_<int:pk>/", views.Delete_Mov_CP_DetailView.as_view(), name="delete_mov_cp_detail"),
    path("delete_mov_unit_detail_<int:pk>/", views.Delete_Mov_Unit_DetailView.as_view(), name="delete_mov_unit_detail"),
    path("delete_mov_packet_detail_<int:pk>/", views.Delete_Mov_Packet_DetailView.as_view(), name="delete_mov_packet_detail"),
]
