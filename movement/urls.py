from django.urls import path
from . import views

app_name='movement'

urlpatterns = [
    path('', views.Movement_PlanBaseView.as_view(), name="movement_base"),
    path('list/', views.Movement_PlanListView.as_view(), name="all"),
    path("create_movement_plan/", views.Create_Movement_PlanView.as_view(), name="create_movement_plan"),
    path("allocate_new_cp/", views.Create_CP_DetailCreateListView.as_view(), name="allocate_new_cp"),
    path("allocate_new_unit/", views.Create_Unit_DetailCreateListView.as_view(), name="allocate_new_unit"),
    path("allocate_new_packet/", views.Create_Packet_DetailCreateListView.as_view(), name="allocate_new_packet"),
    path("create_brigade/", views.Create_BrigadeCreateListView.as_view(), name="create_brigade"),
    path("create_unit/", views.Create_UnitCreateListView.as_view(), name="create_unit"),
    path("_update_unit/<int:pk>/", views._Update_UnitView.as_view(), name="_update_unit"),
    path("update_unit/<int:pk>/", views.Update_UnitView.as_view(), name="update_unit"),
    path("update_delete_unit_list/", views.Edit_Unit_ListView.as_view(), name="update_delete_unit_list"),
    path("_update_brigade/<int:pk>/", views._Update_BrigadeView.as_view(), name="_update_brigade"),
    path("update_brigade/<int:pk>/", views.Update_BrigadeView.as_view(), name="update_brigade"),
    path("update_delete_brigade_list/", views.Edit_Brigade_ListView.as_view(), name="update_delete_brigade_list"),
    path("update_movement_plan/<int:pk>/", views.Update_Movement_PlanView.as_view(), name="update_movement_plan"),
    path("update_delete_movement_plan_list/", views.Edit_Movement_PlanListView.as_view(), name="update_delete_movement_plan_list"),
    path("_update_cp_detail/<int:pk>/", views._Update_CP_DetailView.as_view(), name="_update_cp_detail"),
    path("update_cp_detail/<int:pk>/", views.Update_CP_DetailView.as_view(), name="update_cp_detail"),
    path("update_delete_cp_detail_list/", views.Edit_CP_DetailListView.as_view(), name="update_delete_cp_detail_list"),
    path("_update_unit_detail/<int:pk>/", views._Update_Unit_DetailView.as_view(), name="_update_unit_detail"),
    path("update_unit_detail/<int:pk>/", views.Update_Unit_DetailView.as_view(), name="update_unit_detail"),
    path("update_delete_unit_detail_list/", views.Edit_Unit_DetailListView.as_view(), name="update_delete_unit_detail_list"),
    path("update_packet_detail/<int:pk>/", views.Update_Packet_DetailView.as_view(), name="update_packet_detail"),
    path("_update_packet_detail/<int:pk>/", views._Update_Packet_DetailView.as_view(), name="_update_packet_detail"),
    path("update_delete_packet_detail_list/", views.Edit_Packet_DetailListView.as_view(), name="update_delete_packet_detail_list"),
    # path("by/<username>/",views.UserPosts.as_view(),name="for_user"),
    path("<brigade>/<int:pk>/",views.Movement_PlanDetailView.as_view(),name="movement_single"),
    path("<brigade>/<unit>/<int:pk>/",views.Unit_DetailView.as_view(),name="unit_single"),

    path("delete_unit_<int:pk>/",views.Delete_UnitView.as_view(),name="delete_unit"),
    path("delete_unit_detail_<int:pk>/",views.Delete_Unit_DetailView.as_view(),name="delete_unit_detail"),
    path("delete_packet_detail_<int:pk>/",views.Delete_Packet_DetailView.as_view(),name="delete_packet_detail"),
    path("delete_movement_plan_<int:pk>/",views.Delete_Movement_PlanView.as_view(),name="delete_movement_plan"),
    path("delete_cp_detail_<int:pk>/",views.Delete_CP_DetailView.as_view(),name="delete_cp_detail"),
    path("delete_brigade_<int:pk>/",views.Delete_BrigadeView.as_view(),name="delete_brigade"),

    path("_delete_unit_<int:pk>/",views._Delete_UnitView.as_view(),name="_delete_unit"),
    path("_delete_brigade_<int:pk>/",views._Delete_BrigadeView.as_view(),name="_delete_brigade"),
    path("_delete_unit_detail_<int:pk>/",views._Delete_Unit_DetailView.as_view(),name="_delete_unit_detail"),
    path("_delete_packet_detail_<int:pk>/",views._Delete_Packet_DetailView.as_view(),name="_delete_packet_detail"),
    path("_delete_cp_detail_<int:pk>/",views._Delete_CP_DetailView.as_view(),name="_delete_cp_detail"),
    # path("delete/<int:pk>/",views.DeletePost.as_view(),name="delete"),
]
