from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import (
    LoginRequiredMixin
)
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import generic

from startex import forms
from startex import models
from django.db.models import Q

User = get_user_model()


# Create your views here.

# FBV
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def post_StartEx_Plan(request):
    if is_ajax(request) and request.method == "POST":
        sx_plan_id = request.POST.get('sx_plan_id', None)
        request.session['session_sx_id'] = sx_plan_id
        request.session['session_chain'] = 1
        request.session['session_sx_guide'] = 0
        return JsonResponse({"instance": ""}, status=200)
    # some error occured
    return JsonResponse({"error": ""}, status=400)


def post_Unit_Detail(request):
    if is_ajax(request) and request.method == "POST":
        sx_unit_id = request.POST.get('sx_unit_id', None)
        sx_plan_id = request.POST.get('sx_plan_id', None)
        request.session['session_sx_u_id'] = sx_unit_id
        request.session['session_sx_id'] = sx_plan_id
        request.session['session_chain'] = 1
        request.session['session_sx_guide'] = 0
        return JsonResponse({"instance": ""}, status=200)
    # some error occured
    return JsonResponse({"error": ""}, status=400)


def get_Unit_Detail(request):
    if is_ajax(request) and request.method == "GET":
        if request.GET.get('sx_id'):
            sx_id = request.GET.get('sx_id', None)
        else:
            sx_id = 0
        if sx_id != 0:
            request.session['session_sx_id'] = sx_id
        else:
            request.session['session_sx_id'] = 0

        return JsonResponse({"instance": ""}, status=200)
    # some error occured
    return JsonResponse({"error": ""}, status=400)


def get_Vehicle_Detail(request):
    if is_ajax(request) and request.method == "GET":
        if request.GET.get('sx_unit_id'):
            sx_unit_id = request.GET.get('sx_unit_id', None)
        else:
            sx_unit_id = 0
        if sx_unit_id != 0:
            print(sx_unit_id)
            request.session['session_sx_u_id'] = sx_unit_id
        else:
            request.session['session_sx_u_id'] = 0

        return JsonResponse({"instance": ""}, status=200)
    # some error occured
    return JsonResponse({"error": ""}, status=400)


def validate_Vehicle_Name(request):
    vehicle_name = request.GET.get('vehicle_name', None)
    data = {
        'is_taken': models.SX_Vehicle_Data.objects.filter(name=vehicle_name).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A vehicle with this name already exists.'
    return JsonResponse(data)

def validate_SX_Unit_Name(request):
    sx_unit_name = request.GET.get('sx_unit_name', None)
    sx_id = request.GET.get('sx_id', None)
    data = {
        'is_taken': models.SX_Unit_Detail.objects.filter(u_id__id=sx_unit_name, sx_id__id=sx_id).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A unit with this name already exists.'
    return JsonResponse(data)

def validate_SX_Vehicle_Name(request):
    sx_vehicle_name = request.GET.get('sx_vehicle_name', None)
    sx_u_id = request.GET.get('sx_u_id', None)
    data = {
        'is_taken': models.SX_Vehicle_Detail.objects.filter(sx_v_id__id=sx_vehicle_name, sx_u_id__id=sx_u_id).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A vehicle with this name already exists.'
    return JsonResponse(data)

# CBV
# Base
class StartEx_PlanBaseView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'startex/startex_plan_base.html'

    def get_context_data(self, **kwargs):
        context = super(StartEx_PlanBaseView, self).get_context_data(**kwargs)
        context['title'] = 'StartEx - Base Page'
        context['sidebar'] = 'StartEx'
        context['year'] = datetime.now().year
        self.request.session['session_sx_guide'] = 0
        return context


# List and Detail
class List_StartEx_PlanView(LoginRequiredMixin, generic.ListView):
    model = models.StartEx_Plan
    template_name = 'startex/list_startex_plan.html'
    context_object_name = 'list_startex_plan'
    paginate_by = 4

    def get_queryset(self):
        self.request.session['session_chain'] = 0
        return models.StartEx_Plan.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(List_StartEx_PlanView, self).get_context_data(**kwargs)
        context['title'] = 'StartEx - StartEx Plan List'
        context['sidebar'] = 'StartEx'
        context['year'] = datetime.now().year
        return context


class Detail_StartEx_PlanView(LoginRequiredMixin, generic.DetailView):
    model = models.StartEx_Plan
    template_name = 'startex/detail_startex_plan.html'
    context_object_name = 'detail_startex_plan'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.kwargs.get("pk")
        )

    def get_context_data(self, **kwargs):
        context = super(Detail_StartEx_PlanView, self).get_context_data(**kwargs)
        context["sx_vehicle_data"] = models.SX_Vehicle_Data.objects.all().order_by('name')
        context["sx_vehicle_detail"] = models.SX_Vehicle_Detail.objects.all().order_by('id')
        context["sx_unit_detail"] = models.SX_Unit_Detail.objects.filter(
            sx_id__exact=self.kwargs.get("pk")
        ).order_by('id')
        context['title'] = 'StartEx - StartEx Plan Detail'
        context['sidebar'] = 'StartEx'
        context['year'] = datetime.now().year
        return context


# Edit
class list_edit_vehicle_dataView(LoginRequiredMixin, generic.ListView):
    model = models.SX_Vehicle_Data
    template_name = 'startex/list_edit_vehicle_data.html'
    context_object_name = 'list_edit_vehicle_data'
    paginate_by = 8

    def get_queryset(self):
        self.request.session['session_chain'] = 0
        return models.SX_Vehicle_Data.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super(list_edit_vehicle_dataView, self).get_context_data(**kwargs)
        context['title'] = 'StartEx - Edit Vehicle Data List'
        context['sidebar'] = 'StartEx'
        context['year'] = datetime.now().year
        search_post = self.request.GET.get('search')
        if search_post:
            context['vehicle_data'] = models.SX_Vehicle_Data.objects.filter(
                Q(id__icontains=search_post) | Q(name__icontains=search_post) | Q(
                    model__icontains=search_post) | Q(category__icontains=search_post))
            context['searchbool'] = 1
        else:
            context['searchbool'] = 0
        return context


class List_Edit_StartEx_PlanView(LoginRequiredMixin, generic.ListView):
    model = models.StartEx_Plan
    template_name = 'startex/list_edit_startex_plan.html'
    context_object_name = 'list_edit_startex_plan'
    paginate_by = 8

    def get_queryset(self):
        self.request.session['session_chain'] = 0
        return models.StartEx_Plan.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(List_Edit_StartEx_PlanView, self).get_context_data(**kwargs)
        context['title'] = 'StartEx - Edit StartEx Plan List'
        context['sidebar'] = 'StartEx'
        context['year'] = datetime.now().year
        search_post = self.request.GET.get('search')
        if search_post:
            context['startex_plans'] = models.StartEx_Plan.objects.filter(
                Q(description__icontains=search_post) | Q(brigade__brigade__icontains=search_post) | Q(
                    brigade__acronym__icontains=search_post) | Q(id__icontains=search_post) | Q(
                    name__icontains=search_post))
            context['searchbool'] = 1
        else:
            context['searchbool'] = 0
        return context


class List_Edit_SX_Unit_DetailView(LoginRequiredMixin, generic.ListView):
    model = models.SX_Unit_Detail
    template_name = 'startex/list_edit_sx_unit_detail.html'
    context_object_name = 'list_edit_sx_unit_detail'
    paginate_by = 8

    def get_queryset(self):
        self.request.session['session_chain'] = 0
        return models.SX_Unit_Detail.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(List_Edit_SX_Unit_DetailView, self).get_context_data(**kwargs)
        context["sx_unit_detail"] = models.SX_Unit_Detail.objects.filter(
            sx_id__exact=self.kwargs.get("pk")
        ).order_by('id')
        context["sx_vehicle_detail"] = models.SX_Vehicle_Detail.objects.all().order_by('id')
        context['title'] = 'StartEx - Edit Unit Detail List'
        context['sidebar'] = 'StartEx'
        context['year'] = datetime.now().year
        search_post = self.request.GET.get('search')
        if search_post:
            context['unit_details'] = models.SX_Unit_Detail.objects.filter(
                Q(id__icontains=search_post) | Q(sx_id__id__icontains=search_post) | Q(sx_id__name__icontains=search_post) | Q(
                    u_id__unit__icontains=search_post) | Q(u_id__acronym__icontains=search_post))
            context['searchbool'] = 1
        else:
            context['searchbool'] = 0
        return context


class List_Edit_SX_Vehicle_DetailView(LoginRequiredMixin, generic.ListView):
    model = models.SX_Vehicle_Detail
    template_name = 'startex/list_edit_sx_vehicle_detail.html'
    context_object_name = 'list_edit_sx_vehicle_detail'
    paginate_by = 8

    def get_queryset(self):
        self.request.session['session_chain'] = 0
        return models.SX_Vehicle_Detail.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(List_Edit_SX_Vehicle_DetailView, self).get_context_data(**kwargs)
        context["sx_vehicle_detail"] = models.SX_Vehicle_Detail.objects.filter(
            sx_u_id__exact=self.kwargs.get("pk")
        ).order_by('id')
        context['title'] = 'StartEx - Edit Vehicle Detail List'
        context['sidebar'] = 'StartEx'
        context['year'] = datetime.now().year
        search_post = self.request.GET.get('search')
        if search_post:
            context['vehicle_details'] = models.SX_Vehicle_Detail.objects.filter(
                Q(sx_u_id__u_id__acronym__icontains=search_post) | Q(sx_u_id__u_id__unit__icontains=search_post) | Q(sx_u_id__sx_id__name__icontains=search_post) | Q(id__icontains=search_post) | Q(
                    sx_v_id__name__icontains=search_post) | Q(qty__icontains=search_post))
            context['searchbool'] = 1
        else:
            context['searchbool'] = 0
        return context


# Create
class Create_List_SX_Vehicle_DataView(LoginRequiredMixin, generic.CreateView, generic.ListView):
    template_name = 'startex/create_list_sx_vehicle_data.html'
    model = models.SX_Vehicle_Data
    form_class = forms.SX_Vehicle_DataForm
    context_object_name = 'create_list_sx_vehicle_data'
    success_url = '/startex/create_list_sx_vehicle_data'
    paginate_by = 5

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        self.request.session['session_chain'] = 1
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(Create_List_SX_Vehicle_DataView, self).get_context_data(**kwargs)
        context['title'] = 'StartEx - Create New Vehicle Data'
        context['sidebar'] = 'StartEx'
        context['year'] = datetime.now().year
        search_post = self.request.GET.get('search')
        if search_post:
            context['vehicle_data'] = models.SX_Vehicle_Data.objects.filter(
                Q(id__icontains=search_post) | Q(name__icontains=search_post) | Q(
                    model__icontains=search_post) | Q(category__icontains=search_post))
            context['searchbool'] = 1
        else:
            context['searchbool'] = 0
        return context

    def get_queryset(self):
        return models.SX_Vehicle_Data.objects.all().order_by('id')


class Create_StartEx_PlanView(LoginRequiredMixin, generic.CreateView, generic.ListView):
    template_name = 'startex/create_startex_plan.html'
    model = models.StartEx_Plan
    form_class = forms.StartEx_PlanForm
    context_object_name = 'create_list_startex_plan'
    paginate_by = 20
    success_url = '/startex/create_startex_plan'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        self.request.session['session_sx_id'] = self.object.pk
        self.request.session['session_chain'] = 1
        self.request.session['session_sx_guide'] = 1
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(Create_StartEx_PlanView, self).get_context_data(**kwargs)
        context['title'] = 'StartEx - Create New StartEx Plan'
        context['sidebar'] = 'StartEx'
        context['year'] = datetime.now().year
        context['open_url'] = 'startex:create_list_sx_unit_detail'
        context['open_text'] = 'Open'
        context['sx_guide'] = self.request.session.get('session_sx_guide', 0)
        search_post = self.request.GET.get('search')
        if search_post:
            context['startex_plans'] = models.StartEx_Plan.objects.filter(
                Q(description__icontains=search_post) | Q(brigade__brigade__icontains=search_post) | Q(
                    brigade__acronym__icontains=search_post) | Q(id__icontains=search_post) | Q(
                    name__icontains=search_post))
            context['searchbool'] = 1
        else:
            context['searchbool'] = 0
        return context

    def get_queryset(self):
        self.request.session['session_chain'] = 1
        return models.StartEx_Plan.objects.all().order_by('-created_at')


class Create_List_SX_Unit_DetailView(LoginRequiredMixin, generic.CreateView, generic.ListView):
    template_name = 'startex/create_list_sx_unit_detail.html'
    model = models.SX_Unit_Detail
    form_class = forms.SX_Unit_DetailForm
    context_object_name = 'create_list_sx_unit_detail'
    paginate_by = 20
    success_url = '/startex/create_list_sx_unit_detail'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        self.request.session['session_sx_u_id'] = self.object.pk
        self.request.session['session_sx_id'] = self.object.sx_id.pk
        self.request.session['session_sx_guide'] = 1
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(Create_List_SX_Unit_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'StartEx - Allocate New Unit'
        context['sidebar'] = 'StartEx'
        context['year'] = datetime.now().year
        context['sx_id'] = self.request.session.get('session_sx_id', 0)
        context['sx_guide'] = self.request.session.get('session_sx_guide', 0)
        search_post = self.request.GET.get('search')
        if search_post:
            context['unit_details'] = models.SX_Unit_Detail.objects.filter(
                Q(id__icontains=search_post) | Q(sx_id__id__icontains=search_post) | Q(sx_id__name__icontains=search_post) | Q(
                    u_id__unit__icontains=search_post) | Q(u_id__acronym__icontains=search_post))
            context['searchbool'] = 1
        else:
            context['searchbool'] = 0
        if self.request.session.get('session_chain', 0) == 0:
            context['done_url'] = 'startex:startex_plan_base'
            context['done_text'] = 'Close'
        else:
            context['done_url'] = 'startex:create_startex_plan'
            context['done_text'] = 'Back'
        return context

    def get_queryset(self):
        self.request.session['session_chain'] = 1
        if self.request.session.get('session_sx_id', 0) == 0:
            return models.SX_Unit_Detail.objects.all().order_by('id')
        else:
            return models.SX_Unit_Detail.objects.filter(sx_id_id=self.request.session.get('session_sx_id', 0)).order_by(
                'id')


class Create_List_SX_Vehicle_DetailView(LoginRequiredMixin, generic.CreateView, generic.ListView):
    template_name = 'startex/create_list_sx_vehicle_detail.html'
    model = models.SX_Vehicle_Detail
    form_class = forms.SX_Vehicle_DetailForm
    context_object_name = 'create_list_sx_vehicle_detail'
    paginate_by = 5
    success_url = '/startex/create_list_sx_vehicle_detail'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        self.request.session['session_sx_u_id'] = self.object.sx_u_id.id
        self.request.session['session_sx_id'] = self.object.sx_u_id.sx_id.id
        self.request.session['session_sx_guide'] = 1
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(Create_List_SX_Vehicle_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'StartEx - Allocate New Vehicle'
        context['sidebar'] = 'StartEx'
        context['year'] = datetime.now().year
        context['sx_u_id'] = self.request.session.get('session_sx_u_id', 0)
        context['sx_guide'] = self.request.session.get('session_sx_guide', 0)
        search_post = self.request.GET.get('search')
        if search_post:
            context['vehicle_details'] = models.SX_Vehicle_Detail.objects.filter(
                Q(sx_u_id__u_id__acronym__icontains=search_post) | Q(sx_u_id__u_id__unit__icontains=search_post) | Q(sx_u_id__sx_id__name__icontains=search_post) | Q(id__icontains=search_post) | Q(
                    sx_v_id__name__icontains=search_post) | Q(qty__icontains=search_post))
            context['searchbool'] = 1
        else:
            context['searchbool'] = 0
        if self.request.session.get('session_chain', 0) == 0:
            context['done_url'] = 'startex:startex_plan_base'
            context['done_text'] = 'Close'
        else:
            context['done_url'] = 'startex:create_list_sx_unit_detail'
            context['done_text'] = 'Back'
        return context

    def get_queryset(self):
        self.request.session['session_chain'] = 1
        if self.request.session.get('session_sx_u_id', 0) == 0:
            return models.SX_Vehicle_Detail.objects.all().order_by('id')
        else:
            return models.SX_Vehicle_Detail.objects.filter(
                sx_u_id_id=self.request.session.get('session_sx_u_id', 0)).order_by('id')


# Update
class Update_SX_Vehicle_DataView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'startex/update_sx_vehicle_data.html'
    form_class = forms.SX_Vehicle_DataForm
    model = models.SX_Vehicle_Data

    def get_success_url(self):
        if self.request.session.get('session_chain', 0) == 0:
            return reverse_lazy('startex:list_edit_vehicle_data')
        else:
            return reverse_lazy('startex:create_list_sx_vehicle_data')

    def get_context_data(self, **kwargs):
        context = super(Update_SX_Vehicle_DataView, self).get_context_data(**kwargs)
        context['title'] = 'StartEx - Update Vehicle Data'
        context['sidebar'] = 'StartEx'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'startex:list_edit_vehicle_data'
        else:
            context['cancel_url'] = 'startex:create_list_sx_vehicle_data'
        return context


class Update_StartEx_PlanView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'startex/update_startex_plan.html'
    form_class = forms.StartEx_PlanForm
    model = models.StartEx_Plan

    def get_success_url(self):
        if self.request.session.get('session_chain', 0) == 0:
            return reverse_lazy('startex:edit_list_startex_plan')
        else:
            return reverse_lazy('startex:create_startex_plan')

    def get_context_data(self, **kwargs):
        context = super(Update_StartEx_PlanView, self).get_context_data(**kwargs)
        context['title'] = 'StartEx - Update StartEx Plan'
        context['sidebar'] = 'StartEx'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'startex:edit_list_startex_plan'
        else:
            context['cancel_url'] = 'startex:create_startex_plan'
        return context


class Update_SX_Unit_DetailView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'startex/update_sx_unit_detail.html'
    form_class = forms.SX_Unit_DetailForm
    model = models.SX_Unit_Detail

    def get_success_url(self):
        if self.request.session.get('session_chain', 0) == 0:
            return reverse_lazy('startex:edit_list_sx_unit_detail')
        else:
            return reverse_lazy('startex:create_list_sx_unit_detail')

    def get_context_data(self, **kwargs):
        context = super(Update_SX_Unit_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'StartEx - Update Allocated Unit Detail'
        context['sidebar'] = 'StartEx'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'startex:edit_list_sx_unit_detail'
        else:
            context['cancel_url'] = 'startex:create_list_sx_unit_detail'
        return context


class Update_SX_Vehicle_DetailView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'startex/update_sx_vehicle_detail.html'
    form_class = forms.SX_Vehicle_DetailForm
    model = models.SX_Vehicle_Detail

    def get_success_url(self):
        if self.request.session.get('session_chain', 0) == 0:
            return reverse_lazy('startex:edit_list_sx_vehicle_detail')
        else:
            return reverse_lazy('startex:create_list_sx_vehicle_detail')

    def get_context_data(self, **kwargs):
        context = super(Update_SX_Vehicle_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'StartEx - Update Allocated Vehicle Detail'
        context['sidebar'] = 'StartEx'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'startex:edit_list_sx_vehicle_detail'
        else:
            context['cancel_url'] = 'startex:create_list_sx_vehicle_detail'
        return context


# Delete
class Delete_SX_Vehicle_DataView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'startex/delete_sx_vehicle_data.html'
    model = models.SX_Vehicle_Data

    def get_success_url(self):
        if self.request.session.get('session_chain', 0) == 0:
            return reverse_lazy('startex:list_edit_vehicle_data')
        else:
            return reverse_lazy('startex:create_list_sx_vehicle_data')

    def get_context_data(self, **kwargs):
        context = super(Delete_SX_Vehicle_DataView, self).get_context_data(**kwargs)
        context['title'] = 'StartEx - Delete Vehicle Data'
        context['sidebar'] = 'StartEx'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'startex:list_edit_vehicle_data'
        else:
            context['cancel_url'] = 'startex:create_list_sx_vehicle_data'
        return context


class Delete_StartEx_PlanView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'startex/delete_startex_plan.html'
    model = models.StartEx_Plan

    def get_success_url(self):
        if self.request.session.get('session_chain', 0) == 0:
            return reverse_lazy('startex:edit_list_startex_plan')
        else:
            return reverse_lazy('startex:create_startex_plan')

    def get_context_data(self, **kwargs):
        context = super(Delete_StartEx_PlanView, self).get_context_data(**kwargs)
        context['title'] = 'StartEx - Delete StartEx Plan'
        context['sidebar'] = 'StartEx'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'startex:edit_list_startex_plan'
        else:
            context['cancel_url'] = 'startex:create_startex_plan'
        return context


class Delete_SX_Unit_DetailView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'startex/delete_sx_unit_detail.html'
    model = models.SX_Unit_Detail

    def get_success_url(self):
        if self.request.session.get('session_chain', 0) == 0:
            return reverse_lazy('startex:edit_list_sx_unit_detail')
        else:
            return reverse_lazy('startex:create_list_sx_unit_detail')

    def get_context_data(self, **kwargs):
        context = super(Delete_SX_Unit_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'StartEx - Remove Unit Detail'
        context['sidebar'] = 'StartEx'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'startex:edit_list_sx_unit_detail'
        else:
            context['cancel_url'] = 'startex:create_list_sx_unit_detail'
        return context


class Delete_SX_Vehicle_DetailView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'startex/delete_sx_vehicle_detail.html'
    model = models.SX_Vehicle_Detail

    def get_success_url(self):
        if self.request.session.get('session_chain', 0) == 0:
            return reverse_lazy('startex:edit_list_sx_vehicle_detail')
        else:
            return reverse_lazy('startex:create_list_sx_vehicle_detail')

    def get_context_data(self, **kwargs):
        context = super(Delete_SX_Vehicle_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'StartEx - Remove Vehicle Detail'
        context['sidebar'] = 'StartEx'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'startex:edit_list_sx_vehicle_detail'
        else:
            context['cancel_url'] = 'startex:create_list_sx_vehicle_detail'
        return context
