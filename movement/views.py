from django.shortcuts import render, get_object_or_404, redirect, reverse
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator
# pip install django-braces
# from braces.views import SelectRelatedMixin
from . import models
from . import forms

from django.contrib.auth import get_user_model
from django.http import JsonResponse

User = get_user_model()

# Create your views here.

#FBV

def post_Movement_Plan(request):
    if request.is_ajax and request.method == "POST":
        movement_plan_id = request.POST.get('movement_plan_id', None)
        request.session['session_m_id'] = movement_plan_id
        request.session['session_chain'] = 1
        return JsonResponse({"instance": ""}, status=200)
    # some error occured
    return JsonResponse({"error": ""}, status=400)

def post_CP_Detail(request):
    if request.is_ajax and request.method == "POST":
        m_cp_id = request.POST.get('m_cp_id', None)
        m_plan_id = request.POST.get('m_plan_id', None)
        request.session['session_cp_id'] = m_cp_id
        request.session['session_m_id'] = m_plan_id
        request.session['session_chain'] = 1
        return JsonResponse({"instance": ""}, status=200)
    # some error occured
    return JsonResponse({"error": ""}, status=400)

def get_CP_Detail(request):
    if request.is_ajax and request.method == "GET":
        if request.GET.get('m_id'):
            m_id = request.GET.get('m_id', None)
        else:
            m_id = 0
        if m_id != 0:
            request.session['session_m_id'] = m_id
        else:
            request.session['session_m_id'] = 0

        return JsonResponse({"instance": ""}, status=200)
    # some error occured
    return JsonResponse({"error": ""}, status=400)

def post_Unit_Detail(request):
    if request.is_ajax and request.method == "POST":
        m_unit_id = request.POST.get('m_unit_id', None)
        m_plan_id = request.POST.get('m_plan_id', None)
        request.session['session_u_id'] = m_unit_id
        request.session['session_m_id'] = m_plan_id
        request.session['session_chain'] = 1
        return JsonResponse({"instance": ""}, status=200)
    # some error occured
    return JsonResponse({"error": ""}, status=400)

def get_Unit_Detail(request):
    if request.is_ajax and request.method == "GET":
        if request.GET.get('m_id'):
            m_id = request.GET.get('m_id', None)
        else:
            m_id = 0
        if m_id != 0:
            request.session['session_m_id'] = m_id
        else:
            request.session['session_m_id'] = 0

        return JsonResponse({"instance": ""}, status=200)
    # some error occured
    return JsonResponse({"error": ""}, status=400)

def get_Packet_Detail(request):
    if request.is_ajax and request.method == "GET":
        if request.GET.get('u_id'):
            u_id = request.GET.get('u_id', None)
        else:
            u_id = 0
        if u_id != 0:
            request.session['session_u_id'] = u_id
        else:
            request.session['session_u_id'] = 0

        return JsonResponse({"instance": ""}, status=200)
    # some error occured
    return JsonResponse({"error": ""}, status=400)

# CBV
# Base
class Movement_PlanBaseView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'movement/movement_base.html'

    def get_context_data(self, **kwargs):
        context = super(Movement_PlanBaseView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Base Page'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context

# List and Detail
class Movement_PlanListView(LoginRequiredMixin, generic.ListView):
    model = models.Movement_Data
    template_name = 'movement/movement_list.html'
    context_object_name = 'movement_detail_list'
    paginate_by = 4

    def get_queryset(self):
        self.request.session['session_chain'] = 0
        return models.Movement_Data.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(Movement_PlanListView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Movement Plan List'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context


class Movement_PlanDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Movement_Data
    template_name = 'movement/movement_detail.html'
    context_object_name = 'movement_detail_detail'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            id__iexact=self.kwargs.get("pk")
        )

    def get_context_data(self, **kwargs):
        context = super(Movement_PlanDetailView, self).get_context_data(**kwargs)
        context["unit_detail"] = models.Unit_Detail.objects.filter(
            m_id__exact=self.kwargs.get("pk")
        ).order_by('packet_no')
        context["cp_detail"] = models.CP_Detail.objects.filter(
            m_id__exact=self.kwargs.get("pk")
        ).order_by('cp_no')
        context['title'] = 'Movement - Movement Plan Detail'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context


class Unit_DetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Unit_Detail
    template_name = 'movement/unit_detail.html'
    context_object_name = 'unit_detail'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            id__iexact=self.kwargs.get("pk")
        )

    def get_context_data(self, **kwargs):
        context = super(Unit_DetailView, self).get_context_data(**kwargs)
        context["packet_detail"] = models.Packet_Detail.objects.filter(u_id__exact=self.kwargs.get("pk")
        ).order_by('packet_no')
        context["cp_detail"] = models.CP_Detail.objects.all().order_by('cp_no')
        context['title'] = 'Movement - Movement Plan Unit Detail'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context

# Edit
class Edit_Unit_ListView(LoginRequiredMixin, generic.ListView):
    model = models.Unit
    template_name = 'movement/edit_unit_list.html'
    context_object_name = 'unit_list'
    paginate_by = 8

    def get_queryset(self):
        self.request.session['session_chain'] = 0
        return models.Unit.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super(Edit_Unit_ListView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Edit Unit'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context


class Edit_Brigade_ListView(LoginRequiredMixin, generic.ListView):
    model = models.Brigade
    template_name = 'movement/edit_brigade_list.html'
    context_object_name = 'brigade_list'
    paginate_by = 8

    def get_queryset(self):
        self.request.session['session_chain'] = 0
        return models.Brigade.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super(Edit_Brigade_ListView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Edit Brigade'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context


class Edit_Movement_PlanListView(LoginRequiredMixin, generic.ListView):
    model = models.Movement_Data
    template_name = 'movement/edit_movement_plan_list.html'
    context_object_name = 'movement_plan_list'
    paginate_by = 8

    def get_queryset(self):
        self.request.session['session_chain'] = 0
        return models.Movement_Data.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(Edit_Movement_PlanListView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Edit Movement Plan'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context


class Edit_CP_DetailListView(LoginRequiredMixin, generic.ListView):
    model = models.CP_Detail
    template_name = 'movement/edit_cp_detail_list.html'
    context_object_name = 'cp_detail_list'
    paginate_by = 8

    def get_queryset(self):
        self.request.session['session_chain'] = 0
        return models.CP_Detail.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super(Edit_CP_DetailListView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Edit Allocated CP'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context


class Edit_Unit_DetailListView(LoginRequiredMixin, generic.ListView):
    model = models.Unit_Detail
    template_name = 'movement/edit_unit_detail_list.html'
    context_object_name = 'unit_detail_list'
    paginate_by = 20

    def get_queryset(self):
        self.request.session['session_chain'] = 0
        return models.Unit_Detail.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super(Edit_Unit_DetailListView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Edit Allocated Unit'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context


class Edit_Packet_DetailListView(LoginRequiredMixin, generic.ListView):
    model = models.Packet_Detail
    template_name = 'movement/edit_packet_detail_list.html'
    context_object_name = 'packet_detail_list'
    paginate_by = 20

    def get_queryset(self):
        self.request.session['session_chain'] = 0
        return models.Packet_Detail.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super(Edit_Packet_DetailListView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Edit Allocated Packet'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context

# Create
class Create_Movement_PlanView(LoginRequiredMixin, generic.CreateView, generic.ListView):
    template_name = 'movement/create_movement_plan.html'
    model = models.Movement_Data
    form_class = forms.Movement_PlanForm
    context_object_name = 'create_list_movement_plan'
    paginate_by = 20
    success_url = '/movement/create_movement_plan'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        self.request.session['session_m_id'] = self.object.pk
        self.request.session['session_chain'] = 1
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(Create_Movement_PlanView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - New Movement Plan'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        context['open_url'] = 'movement:allocate_new_cp'
        context['open_text'] = 'Open'
        return context

    def get_queryset(self):
        self.request.session['session_chain'] = 1
        return models.Movement_Data.objects.all().order_by('-created_at')


class Create_CP_DetailCreateListView(LoginRequiredMixin, generic.CreateView, generic.ListView):
    template_name = 'movement/create_cp_detail.html'
    model = models.CP_Detail
    form_class = forms.CP_DetailForm
    context_object_name = 'cp_detail_create_list'
    paginate_by = 20
    success_url = '/movement/allocate_new_cp'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        self.request.session['session_cp_id'] = self.object.pk
        self.request.session['session_m_id'] = self.object.m_id.pk
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(Create_CP_DetailCreateListView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - CP Allocation'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        context['m_id'] = self.request.session.get('session_m_id', 0)
        if self.request.session.get('session_chain', 0) == 0:
            context['done_url'] = 'movement:movement_base'
            context['done_text'] = 'Close'
        else:
            context['done_url'] = 'movement:create_movement_plan'
            context['done_text'] = 'Back'
        return context

    def get_queryset(self):
        self.request.session['session_chain'] = 1
        if self.request.session.get('session_m_id', 0) == 0:
            return models.CP_Detail.objects.all().order_by('id')
        else:
            return models.CP_Detail.objects.filter(m_id_id=self.request.session.get('session_m_id', 0)).order_by('id')


class Create_Unit_DetailCreateListView(LoginRequiredMixin, generic.CreateView, generic.ListView):
    template_name = 'movement/create_unit_detail.html'
    model = models.Unit_Detail
    form_class = forms.Unit_DetailForm
    context_object_name = 'unit_detail_create_list'
    paginate_by = 5
    success_url = '/movement/allocate_new_packet'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        self.request.session['session_u_id'] = self.object.pk
        self.request.session['session_m_id'] = self.object.m_id.pk
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(Create_Unit_DetailCreateListView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Unit Allocation'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        context['m_id'] = self.request.session.get('session_m_id', 0)
        if self.request.session.get('session_chain', 0) == 0:
            context['done_url'] = 'movement:movement_base'
            context['done_text'] = 'Close'
        else:
            context['done_url'] = 'movement:allocate_new_cp'
            context['done_text'] = 'Back'
        return context

    def get_queryset(self):
        self.request.session['session_chain'] = 1
        if self.request.session.get('session_m_id', 0) == 0:
            return models.Unit_Detail.objects.all().order_by('id')
        else:
            return models.Unit_Detail.objects.filter(m_id_id=self.request.session.get('session_m_id', 0)).order_by('id')


class Create_Packet_DetailCreateListView(LoginRequiredMixin, generic.CreateView, generic.ListView):
    template_name = 'movement/create_packet_detail.html'
    model = models.Packet_Detail
    form_class = forms.Packet_DetailForm
    context_object_name = 'packet_detail_create_list'
    paginate_by = 5
    success_url = '/movement/allocate_new_packet'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        self.request.session['session_u_id'] = self.object.u_id.id
        self.request.session['session_m_id'] = self.object.u_id.m_id.id
        if models.Packet_Detail.objects.filter(u_id_id=self.object.u_id.id).count() > 0:
            models.Unit_Detail.objects.filter(id=self.object.u_id.id).update(packet_allocated=True)
        else:
            models.Unit_Detail.objects.filter(id=self.object.u_id.id).update(packet_allocated=False)
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(Create_Packet_DetailCreateListView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Packet Allocation'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        context['u_id'] = self.request.session.get('session_u_id', 0)
        if self.request.session.get('session_chain', 0) == 0:
            context['done_url'] = 'movement:movement_base'
            context['done_text'] = 'Close'
        else:
            context['done_url'] = 'movement:allocate_new_unit'
            context['done_text'] = 'Back'
        return context

    def get_queryset(self):
        self.request.session['session_chain'] = 1
        if self.request.session.get('session_u_id', 0) == 0:
            return models.Packet_Detail.objects.all().order_by('id')
        else:
            return models.Packet_Detail.objects.filter(u_id_id=self.request.session.get('session_u_id', 0)).order_by(
                'id')


class Create_BrigadeCreateListView(LoginRequiredMixin, generic.CreateView, generic.ListView):
    template_name = 'movement/create_brigade.html'
    model = models.Brigade
    form_class = forms.BrigadeForm
    context_object_name = 'brigade_create_list'
    success_url = '/movement/create_brigade'
    paginate_by = 5

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        self.request.session['session_chain'] = 1
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(Create_BrigadeCreateListView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Add New Brigade'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context

    def get_queryset(self):
        return models.Brigade.objects.all().order_by('id')


class Create_UnitCreateListView(LoginRequiredMixin, generic.CreateView, generic.ListView):
    template_name = 'movement/create_unit.html'
    model = models.Unit
    form_class = forms.UnitForm
    context_object_name = 'unit_create_list'
    success_url = '/movement/create_unit'
    paginate_by = 5

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        self.request.session['session_chain'] = 1
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(Create_UnitCreateListView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Add New Unit'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context

    def get_queryset(self):
        return models.Unit.objects.all().order_by('id')

# Update
class Update_UnitView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'movement/update_unit.html'
    form_class = forms.UnitForm
    model = models.Unit

    def get_success_url(self):
        if self.request.session.get('session_chain', 0) == 0:
            return reverse_lazy('movement:update_delete_unit_list')
        else:
            return reverse_lazy('movement:create_unit')

    def get_context_data(self, **kwargs):
        context = super(Update_UnitView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Update Unit'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_unit_list'
        else:
            context['cancel_url'] = 'movement:create_unit'
        return context


class Update_BrigadeView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'movement/update_brigade.html'
    form_class = forms.BrigadeForm
    model = models.Brigade

    def get_success_url(self):
        if self.request.session.get('session_chain', 0) == 0:
            return reverse_lazy('movement:update_delete_brigade_list')
        else:
            return reverse_lazy('movement:create_brigade')

    def get_context_data(self, **kwargs):
        context = super(Update_BrigadeView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Update Brigade'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_brigade_list'
        else:
            context['cancel_url'] = 'movement:create_brigade'
        return context


class Update_Movement_PlanView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'movement/update_movement_plan.html'
    form_class = forms.Movement_PlanForm
    model = models.Movement_Data

    def get_success_url(self):
        if self.request.session.get('session_chain', 0) == 0:
            return reverse_lazy('movement:update_delete_movement_plan_list')
        else:
            return reverse_lazy('movement:create_movement_plan')

    def get_context_data(self, **kwargs):
        context = super(Update_Movement_PlanView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Update Movement Plan'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_movement_plan_list'
        else:
            context['cancel_url'] = 'movement:create_movement_plan'
        return context


class Update_CP_DetailView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'movement/update_cp_detail.html'
    form_class = forms.CP_DetailForm
    model = models.CP_Detail

    def get_success_url(self):
        if self.request.session.get('session_chain', 0) == 0:
            return reverse_lazy('movement:update_delete_cp_detail_list')
        else:
            return reverse_lazy('movement:allocate_new_cp')

    def get_context_data(self, **kwargs):
        context = super(Update_CP_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Update Allocated CP'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_cp_detail_list'
        else:
            context['cancel_url'] = 'movement:allocate_new_cp'
        return context


class Update_Unit_DetailView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'movement/update_unit_detail.html'
    form_class = forms.Unit_DetailForm
    model = models.Unit_Detail

    def get_success_url(self):
        if self.request.session.get('session_chain', 0) == 0:
            return reverse_lazy('movement:update_delete_unit_detail_list')
        else:
            return reverse_lazy('movement:allocate_new_unit')

    def get_context_data(self, **kwargs):
        context = super(Update_Unit_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Update Allocated Unit'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_unit_detail_list'
        else:
            context['cancel_url'] = 'movement:allocate_new_unit'
        return context


class Update_Packet_DetailView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'movement/update_packet_detail.html'
    form_class = forms.Packet_DetailForm
    model = models.Packet_Detail

    def get_success_url(self):
        if self.request.session.get('session_chain', 0) == 0:
            return reverse_lazy('movement:update_delete_packet_detail_list')
        else:
            return reverse_lazy('movement:allocate_new_packet')

    def get_context_data(self, **kwargs):
        context = super(Update_Packet_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Update Allocated Packet'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_packet_detail_list'
        else:
            context['cancel_url'] = 'movement:allocate_new_packet'
        return context


# Delete
class Delete_Unit_DetailView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'movement/confirm_delete_unit_detail.html'
    model = models.Unit_Detail

    def get_success_url(self):
        if self.request.session.get('session_chain', 0) == 0:
            return reverse_lazy('movement:update_delete_unit_detail_list')
        else:
            return reverse_lazy('movement:allocate_new_unit')

    def get_context_data(self, **kwargs):
        context = super(Delete_Unit_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Remove Unit'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_unit_detail_list'
        else:
            context['cancel_url'] = 'movement:allocate_new_unit'
        return context


class Delete_UnitView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'movement/confirm_delete_unit.html'
    model = models.Unit

    def get_success_url(self):
        if self.request.session.get('session_chain', 0) == 0:
            return reverse_lazy('movement:update_delete_unit_list')
        else:
            return reverse_lazy('movement:create_unit')

    def get_context_data(self, **kwargs):
        context = super(Delete_UnitView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Delete Unit'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_unit_list'
        else:
            context['cancel_url'] = 'movement:create_unit'
        return context


class Delete_Packet_DetailView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'movement/confirm_delete_packet_detail.html'
    model = models.Packet_Detail

    def get_success_url(self):
        if self.request.session.get('session_chain', 0) == 0:
            return reverse_lazy('movement:update_delete_packet_detail_list')
        else:
            return reverse_lazy('movement:allocate_new_packet')

    def get_context_data(self, **kwargs):
        context = super(Delete_Packet_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Remove Packet'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_packet_detail_list'
        else:
            context['cancel_url'] = 'movement:allocate_new_packet'
        return context


class Delete_Movement_PlanView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'movement/confirm_delete_movement_plan.html'
    model = models.Movement_Data

    def get_success_url(self):
        if self.request.session.get('session_chain', 0) == 0:
            return reverse_lazy('movement:update_delete_movement_plan_list')
        else:
            return reverse_lazy('movement:create_movement_plan')

    def get_context_data(self, **kwargs):
        context = super(Delete_Movement_PlanView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Delete Movement Plan'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_movement_plan_list'
        else:
            context['cancel_url'] = 'movement:create_movement_plan'
        return context


class Delete_CP_DetailView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'movement/confirm_delete_cp_detail.html'
    model = models.CP_Detail

    def get_success_url(self):
        if self.request.session.get('session_chain', 0) == 0:
            return reverse_lazy('movement:update_delete_cp_detail_list')
        else:
            return reverse_lazy('movement:allocate_new_cp')

    def get_context_data(self, **kwargs):
        context = super(Delete_CP_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Remove CP'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_cp_detail_list'
        else:
            context['cancel_url'] = 'movement:allocate_new_cp'
        return context

class Delete_BrigadeView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'movement/confirm_delete_brigade.html'
    model = models.Brigade

    def get_success_url(self):
        if self.request.session.get('session_chain', 0) == 0:
            return reverse_lazy('movement:update_delete_brigade_list')
        else:
            return reverse_lazy('movement:create_brigade')

    def get_context_data(self, **kwargs):
        context = super(Delete_BrigadeView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Delete Brigade'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_brigade_list'
        else:
            context['cancel_url'] = 'movement:create_brigade'
        return context
