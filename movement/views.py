from django.shortcuts import render, get_object_or_404, redirect, reverse
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.mixins import(
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
#from braces.views import SelectRelatedMixin
from . import models
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

class Movement_PlanBaseView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'movement/movement_base.html'

    def get_context_data(self, **kwargs):
        context = super(Movement_PlanBaseView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Base Page'
        context['sidebar']=  'Movement'
        context['year'] = datetime.now().year
        return context

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
        context['title'] = 'Movement - List View'
        context['sidebar']=  'Movement'
        context['year'] = datetime.now().year
        return context


class Movement_PlanDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Movement_Data
    template_name = 'movement/movement_detail.html'
    context_object_name ='movement_detail_detail'

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
        context['title'] = 'Movement - Detail View'
        context['sidebar']=  'Movement'
        context['year'] = datetime.now().year
        return context

class Unit_DetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Unit_Detail
    template_name = 'movement/unit_detail.html'
    context_object_name ='unit_detail'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            id__iexact=self.kwargs.get("pk")
        )

    def get_context_data(self, **kwargs):
        context = super(Unit_DetailView, self).get_context_data(**kwargs)
        context["packet_detail"] = models.Packet_Detail.objects.filter(
            u_id__exact=self.kwargs.get("pk")
        ).order_by('packet_no')
        context["cp_detail"] = models.CP_Detail.objects.all().order_by('cp_no')
        context['title'] = 'Movement - Unit Detail View'
        context['sidebar']=  'Movement'
        context['year'] = datetime.now().year
        return context

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
        context['title'] = 'Movement - Update/Delete Unit List'
        context['sidebar']=  'Movement'
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
        context['title'] = 'Movement - Update/Delete Unit List'
        context['sidebar']=  'Movement'
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
        context['title'] = 'Movement - Update/Delete Movement Plan List'
        context['sidebar']=  'Movement'
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
        context['title'] = 'Movement - Update/Delete CP Detail List'
        context['sidebar']=  'Movement'
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
        context['title'] = 'Movement - Update/Delete Unit Detail List'
        context['sidebar']=  'Movement'
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
        context['title'] = 'Movement - Update/Delete Packet Detail List'
        context['sidebar']=  'Movement'
        context['year'] = datetime.now().year
        return context

class Create_Movement_PlanView(LoginRequiredMixin,generic.CreateView):
    template_name = 'movement/create_movement_plan.html'
    form_class = forms.Movement_PlanForm
    success_url = '/movement/allocate_new_cp'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        self.request.session['session_m_id'] = self.object.pk
        self.request.session['session_chain'] = 1
        return HttpResponseRedirect(self.get_success_url())
        # return redirect(reverse('movement:allocate_new_cp')+ '?m_id=' + str(self.object.pk))

    def get_context_data(self, **kwargs):
        context = super(Create_Movement_PlanView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Create New Movement Plan'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context

    def get_queryset(self):
        self.request.session['session_chain'] = 1
    # def get_initial(self, *args, **kwargs):
    #     initial = super(Create_Movement_DetailView, self).get_initial(**kwargs)
    #     initial['title'] = 'Movement - Create New Movement Detail'
    #     initial['sidebar'] = 'Movement'
    #     initial['year'] = datetime.now().year
    #     return initial

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
        # return redirect(reverse('movement:allocate_new_cp')+ '?m_id=' + str(self.object.m_id.pk) + '&cp_id=' + str(self.object.pk))
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(Create_CP_DetailCreateListView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Create New CP Detail'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        context['m_id'] = self.request.session.get('session_m_id', 0)
        if self.request.session.get('session_chain', 0) == 0:
            context['done_url'] = 'movement:movement_base'
            context['done_text'] = 'Close'
        else:
            context['done_url'] = 'movement:allocate_new_unit'
            context['done_text'] = 'Next'
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
        # return redirect(reverse('movement:allocate_new_packet')+ '?m_id=' + str(self.object.m_id.pk) + '&u_id=' + str(self.object.pk))
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(Create_Unit_DetailCreateListView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Create New Unit Detail'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        context['m_id'] = self.request.session.get('session_m_id', 0)
        context['done_url'] = 'movement:movement_base'
        context['done_text'] = 'Close'        
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
            models.Unit_Detail.objects.filter(id = self.object.u_id.id).update(packet_allocated = True)
        else:
            models.Unit_Detail.objects.filter(id = self.object.u_id.id).update(packet_allocated = False)
        # return redirect(reverse('movement:allocate_new_packet')+ '?m_id=' + str(self.object.u_id.m_id.id) + '&u_id=' + str(self.object.u_id.id))
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(Create_Packet_DetailCreateListView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Create New Packet Detail'
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
            return models.Packet_Detail.objects.filter(u_id_id=self.request.session.get('session_u_id', 0)).order_by('id')

class Create_BrigadeCreateListView(LoginRequiredMixin,generic.CreateView, generic.ListView):
    template_name = 'movement/create_brigade.html'
    model = models.Brigade
    form_class = forms.BrigadeForm
    context_object_name = 'brigade_create_list'
    success_url = '/movement/create_brigade'
    paginate_by = 5

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # self.object.created_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(Create_BrigadeCreateListView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Create New Brigade'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context

    def get_queryset(self):
        self.request.session['session_chain'] = 1
        return models.Brigade.objects.all().order_by('id')

class Create_UnitCreateListView(LoginRequiredMixin,generic.CreateView, generic.ListView):
    template_name = 'movement/create_unit.html'
    model = models.Unit
    form_class = forms.UnitForm
    context_object_name = 'unit_create_list'
    success_url = '/movement/create_unit'
    paginate_by = 5

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # self.object.created_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(Create_UnitCreateListView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Create New Unit'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context

    def get_queryset(self):
        self.request.session['session_chain'] = 1
        return models.Unit.objects.all().order_by('id')

class _Update_UnitView(LoginRequiredMixin,generic.UpdateView):
    template_name = 'movement/update_unit.html'
    form_class = forms.UnitForm
    model = models.Unit
    success_url = '/movement/create_unit'

    def get_context_data(self, **kwargs):
        context = super(_Update_UnitView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Update Unit'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context

class Update_UnitView(LoginRequiredMixin,generic.UpdateView):
    template_name = 'movement/update_unit.html'
    form_class = forms.UnitForm
    model = models.Unit
    success_url = '/movement/update_delete_unit_list'

    def get_context_data(self, **kwargs):
        context = super(Update_UnitView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Update Unit'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context

class _Update_BrigadeView(LoginRequiredMixin,generic.UpdateView):
    template_name = 'movement/update_brigade.html'
    form_class = forms.BrigadeForm
    model = models.Brigade
    success_url = '/movement/create_brigade'

    def get_context_data(self, **kwargs):
        context = super(_Update_BrigadeView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Update Brigade'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context

class Update_BrigadeView(LoginRequiredMixin,generic.UpdateView):
    template_name = 'movement/update_brigade.html'
    form_class = forms.BrigadeForm
    model = models.Brigade
    success_url = '/movement/update_delete_brigade_list'

    def get_context_data(self, **kwargs):
        context = super(Update_BrigadeView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Update Brigade'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context

class Update_Movement_PlanView(LoginRequiredMixin,generic.UpdateView):
    template_name = 'movement/update_movement_plan.html'
    form_class = forms.Movement_PlanForm
    model = models.Movement_Data
    success_url = '/movement/update_delete_movement_plan_list'

    def get_context_data(self, **kwargs):
        context = super(Update_Movement_PlanView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Update Movement Plan'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context

class _Update_CP_DetailView(LoginRequiredMixin,generic.UpdateView):
    template_name = 'movement/update_cp_detail.html'
    form_class = forms.CP_DetailForm
    model = models.CP_Detail
    # success_url = '/movement/update_delete_packet_detail_list'

    def get_success_url(self):
        return reverse_lazy('movement:allocate_new_cp')+ '?m_id=' + str(self.object.m_id.id) + '&cp_id=' + str(self.object.id) + '&cp_c=' + str(self.model.objects.filter(m_id_id = self.object.m_id.id).count() - 1)

    def get_context_data(self, **kwargs):
        context = super(_Update_CP_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Update Allocated CP'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        context['testa'] = self.request.session['session_m_id']
        return context

class Update_CP_DetailView(LoginRequiredMixin,generic.UpdateView):
    template_name = 'movement/update_cp_detail.html'
    form_class = forms.CP_DetailForm
    model = models.CP_Detail
    success_url = '/movement/update_delete_cp_detail_list'

    def get_context_data(self, **kwargs):
        context = super(Update_CP_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Update Allocated CP'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context

class _Update_Unit_DetailView(LoginRequiredMixin,generic.UpdateView):
    template_name = 'movement/update_unit_detail.html'
    form_class = forms.Unit_DetailForm
    model = models.Unit_Detail
    # success_url = '/movement/update_delete_packet_detail_list'

    def get_success_url(self):
        return reverse_lazy('movement:allocate_new_unit')+ '?m_id=' + str(self.object.m_id.id) + '&u_id=' + str(self.object.id) + '&u_c=' + str(self.model.objects.filter(m_id_id = self.object.m_id.id).count() - 1)

    def get_context_data(self, **kwargs):
        context = super(_Update_Unit_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Update Allocated Unit'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context

class Update_Unit_DetailView(LoginRequiredMixin,generic.UpdateView):
    template_name = 'movement/update_unit_detail.html'
    form_class = forms.Unit_DetailForm
    model = models.Unit_Detail
    success_url = '/movement/update_delete_unit_detail_list'

    def get_context_data(self, **kwargs):
        context = super(Update_Unit_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Update Allocated Unit'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context

class _Update_Packet_DetailView(LoginRequiredMixin,generic.UpdateView):
    template_name = 'movement/update_packet_detail.html'
    form_class = forms.Packet_DetailForm
    model = models.Packet_Detail
    # success_url = '/movement/update_delete_packet_detail_list'

    def get_success_url(self):
        return reverse_lazy('movement:allocate_new_packet')+ '?m_id=' + str(self.object.u_id.m_id.id) + '&u_id=' + str(self.object.u_id.id) + '&p_c=' + str(self.model.objects.filter(u_id_id = self.object.u_id.id).count() - 1)


    def get_context_data(self, **kwargs):
        context = super(_Update_Packet_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Update Allocated Packet'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context

class Update_Packet_DetailView(LoginRequiredMixin,generic.UpdateView):
    template_name = 'movement/update_packet_detail.html'
    form_class = forms.Packet_DetailForm
    model = models.Packet_Detail
    success_url = '/movement/update_delete_packet_detail_list'

    def get_context_data(self, **kwargs):
        context = super(Update_Packet_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Update Allocated Packet'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context

class _Delete_Unit_DetailView(LoginRequiredMixin,generic.DeleteView):
    template_name = 'movement/confirm_delete_unit_detail.html'
    model = models.Unit_Detail

    def get_success_url(self):
        return reverse_lazy('movement:allocate_new_unit')

    def get_context_data(self, **kwargs):
        context = super(_Delete_Unit_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Delete allocated unit'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_unit_detail_list'
        else:
            context['cancel_url'] = 'movement:allocate_new_unit'
        return context

class Delete_Unit_DetailView(LoginRequiredMixin,generic.DeleteView):
    template_name = 'movement/confirm_delete_unit_detail.html'
    model = models.Unit_Detail
    success_url = reverse_lazy('movement:update_delete_unit_detail_list')

    def get_context_data(self, **kwargs):
        context = super(Delete_Unit_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Delete allocated unit'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_unit_detail_list'
        else:
            context['cancel_url'] = 'movement:allocate_new_unit'
        return context

class _Delete_UnitView(LoginRequiredMixin,generic.DeleteView):
    template_name = 'movement/confirm_delete_unit.html'
    model = models.Unit
    success_url = reverse_lazy('movement:create_unit')

    def get_context_data(self, **kwargs):
        context = super(_Delete_UnitView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Delete unit'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_unit_list'
        else:
            context['cancel_url'] = 'movement:create_unit'
        return context

class Delete_UnitView(LoginRequiredMixin,generic.DeleteView):
    template_name = 'movement/confirm_delete_unit.html'
    model = models.Unit
    success_url = reverse_lazy('movement:update_delete_unit_list')

    def get_context_data(self, **kwargs):
        context = super(Delete_UnitView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Delete unit'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_unit_list'
        else:
            context['cancel_url'] = 'movement:create_unit'
        return context

class _Delete_Packet_DetailView(LoginRequiredMixin,generic.DeleteView):
    template_name = 'movement/confirm_delete_packet_detail.html'
    model = models.Packet_Detail

    def get_success_url(self):
        if self.model.objects.filter(u_id_id = self.object.u_id.id).count() - 1 > 0:
            models.Unit_Detail.objects.filter(id = self.object.u_id.id).update(packet_allocated = True)
        else:
            models.Unit_Detail.objects.filter(id = self.object.u_id.id).update(packet_allocated = False)
        return reverse_lazy('movement:allocate_new_packet')
        # success_url = reverse('movement:allocate_new_unit')+ '?m_id=' + str(self.object.m_id.pk) + '&cp_id=' + str(self.object.pk)
        # success_url = reverse_lazy('movement:allocate_new_unit')+ '?m_id=' + str(model.objects.all().last().m_id.id) + '&cp_id=' + str(model.objects.all().last().id)

    def get_context_data(self, **kwargs):
        context = super(_Delete_Packet_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Delete allocated CP'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_packet_detail_list'
        else:
            context['cancel_url'] = 'movement:allocate_new_packet'
        return context

class Delete_Packet_DetailView(LoginRequiredMixin,generic.DeleteView):
    template_name = 'movement/confirm_delete_packet_detail.html'
    model = models.Packet_Detail
    success_url = reverse_lazy('movement:update_delete_packet_detail_list')

    def get_context_data(self, **kwargs):
        context = super(Delete_Packet_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Delete allocated packet'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_packet_detail_list'
        else:
            context['cancel_url'] = 'movement:allocate_new_packet'
        return context
        return context

class Delete_Movement_PlanView(LoginRequiredMixin,generic.DeleteView):
    template_name = 'movement/confirm_delete_movement_plan.html'
    model = models.Movement_Data
    success_url = reverse_lazy('movement:update_delete_movement_plan_list')

    def get_context_data(self, **kwargs):
        context = super(Delete_Movement_PlanView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Delete movement plan'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        return context

class _Delete_CP_DetailView(LoginRequiredMixin,generic.DeleteView):
    template_name = 'movement/confirm_delete_cp_detail.html'
    model = models.CP_Detail

    def get_success_url(self):
        return reverse_lazy('movement:allocate_new_cp')
        # success_url = reverse('movement:allocate_new_unit')+ '?m_id=' + str(self.object.m_id.pk) + '&cp_id=' + str(self.object.pk)
        # success_url = reverse_lazy('movement:allocate_new_unit')+ '?m_id=' + str(model.objects.all().last().m_id.id) + '&cp_id=' + str(model.objects.all().last().id)

    def get_context_data(self, **kwargs):
        context = super(_Delete_CP_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Delete allocated CP'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_cp_detail_list'
        else:
            context['cancel_url'] = 'movement:allocate_new_cp'
        return context

class Delete_CP_DetailView(LoginRequiredMixin,generic.DeleteView):
    template_name = 'movement/confirm_delete_cp_detail.html'
    model = models.CP_Detail
    success_url = reverse_lazy('movement:update_delete_cp_detail_list')

    def get_context_data(self, **kwargs):
        context = super(Delete_CP_DetailView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Delete allocated CP'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_cp_detail_list'
        else:
            context['cancel_url'] = 'movement:allocate_new_cp'
        return context

class _Delete_BrigadeView(LoginRequiredMixin,generic.DeleteView):
    template_name = 'movement/confirm_delete_brigade.html'
    model = models.Brigade
    success_url = reverse_lazy('movement:create_brigade')

    def get_context_data(self, **kwargs):
        context = super(_Delete_BrigadeView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Delete brigade'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_brigade_list'
        else:
            context['cancel_url'] = 'movement:create_brigade'
        return context

class Delete_BrigadeView(LoginRequiredMixin,generic.DeleteView):
    template_name = 'movement/confirm_delete_brigade.html'
    model = models.Brigade
    success_url = reverse_lazy('movement:update_delete_brigade_list')

    def get_context_data(self, **kwargs):
        context = super(Delete_BrigadeView, self).get_context_data(**kwargs)
        context['title'] = 'Movement - Delete brigade'
        context['sidebar'] = 'Movement'
        context['year'] = datetime.now().year
        if self.request.session.get('session_chain', 0) == 0:
            context['cancel_url'] = 'movement:update_delete_brigade_list'
        else:
            context['cancel_url'] = 'movement:create_brigade'
        return context
