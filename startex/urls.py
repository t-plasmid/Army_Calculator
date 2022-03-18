from django.urls import path
from startex import views

app_name = 'startex'

urlpatterns = [
    # FBV
    path('post/ajax/startex_plan', views.post_StartEx_Plan, name="post_startex_plan"),
    path('post/ajax/sx_unit_detail', views.post_Unit_Detail, name="post_unit_detail"),
    path('get/ajax/sx_unit_detail', views.get_Unit_Detail, name="get_unit_detail"),
    path('get/ajax/sx_vehicle_detail', views.get_Vehicle_Detail, name="get_vehicle_detail"),
    path('get/ajax/validate_vehicle_name', views.validate_Vehicle_Name, name="validate_vehicle_name"),
    path('get/ajax/validate_sx_unit_name', views.validate_SX_Unit_Name, name="validate_sx_unit_name"),
    path('get/ajax/validate_sx_vehicle_name', views.validate_SX_Vehicle_Name, name="validate_sx_vehicle_name"),
    # Base
    path('', views.StartEx_PlanBaseView.as_view(), name="startex_plan_base"),
    # View
    path('list_startex_plan/', views.List_StartEx_PlanView.as_view(), name="list_startex_plan"),
    path("detail_startex_plan/<int:pk>/", views.Detail_StartEx_PlanView.as_view(), name="detail_startex_plan"),
    # Create
    path("create_list_sx_vehicle_data/", views.Create_List_SX_Vehicle_DataView.as_view(),
         name="create_list_sx_vehicle_data"),
    path("create_startex_plan/", views.Create_StartEx_PlanView.as_view(), name="create_startex_plan"),
    path("create_list_sx_unit_detail/", views.Create_List_SX_Unit_DetailView.as_view(),
         name="create_list_sx_unit_detail"),
    path("create_list_sx_vehicle_detail/", views.Create_List_SX_Vehicle_DetailView.as_view(),
         name="create_list_sx_vehicle_detail"),
    # Edit
    path("list_edit_vehicle_data/", views.list_edit_vehicle_dataView.as_view(), name="list_edit_vehicle_data"),
    path("list_edit_startex_plan/", views.List_Edit_StartEx_PlanView.as_view(), name="list_edit_startex_plan"),
    path("list_edit_sx_unit_detail/", views.List_Edit_SX_Unit_DetailView.as_view(), name="list_edit_sx_unit_detail"),
    path("list_edit_sx_vehicle_detail/", views.List_Edit_SX_Vehicle_DetailView.as_view(),
         name="list_edit_sx_vehicle_detail"),
    # Update
    path("update_sx_vehicle_data/<int:pk>/", views.Update_SX_Vehicle_DataView.as_view(), name="update_sx_vehicle_data"),
    path("update_startex_plan/<int:pk>/", views.Update_StartEx_PlanView.as_view(), name="update_startex_plan"),
    path("update_sx_unit_detail/<int:pk>/", views.Update_SX_Unit_DetailView.as_view(), name="update_sx_unit_detail"),
    path("update_sx_vehicle_detail/<int:pk>/", views.Update_SX_Vehicle_DetailView.as_view(),
         name="update_sx_vehicle_detail"),
    # Delete
    path("delete_sx_vehicle_data/<int:pk>/", views.Delete_SX_Vehicle_DataView.as_view(), name="delete_sx_vehicle_data"),
    path("delete_startex_plan/<int:pk>/", views.Delete_StartEx_PlanView.as_view(), name="delete_startex_plan"),
    path("delete_sx_unit_detail/<int:pk>/", views.Delete_SX_Unit_DetailView.as_view(), name="delete_sx_unit_detail"),
    path("delete_sx_vehicle_detail/<int:pk>/", views.Delete_SX_Vehicle_DetailView.as_view(), name="delete_sx_vehicle_detail"),
]
