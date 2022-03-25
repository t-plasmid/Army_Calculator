import datetime
from django import forms
from . import models
from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _


class Movement_PlanForm(forms.ModelForm):

    class Meta:
        model = models.Movement_Data
        exclude = ['created_by']

        widgets = {
            'description': forms.Textarea(attrs = {'class': 'editable medium-editor-textarea'}),
            'start_date': forms.DateInput(attrs = {'class':'form-control', 'type':'date'}),
            'start_time': forms.DateInput(attrs = {'class':'form-control', 'type':'Time'})
        }

        # help_texts = {
        #     'cp_no': 'Note: The last CP detail entered here will be used as the Release Point (RP). In that case, the Halt Time you specify will be ignored.',
        # }

    def __init__(self, *args, **kwargs):
        super(Movement_PlanForm, self).__init__(*args, **kwargs)
        self.fields['speed'].label = "Average speed (km/h)"
        self.fields['traffic_density'].label = "Traffic density (veh/km)"
        self.fields['packet_gap'].label = "Packet gap (min)"
        self.fields['unit_gap'].label = "Unit gap (min))"
        self.fields['route_name'].initial = "Test"

    # def clean_start_time(self):
    #     data = self.cleaned_data['start_time']
    #
    #     # check if a time is not in the past.
    #     if data < datetime.time.now():
    #         raise ValidationError(_('Invalid time - time in past'))
    #
    #         # return cleaned data.
    #         return data

    def clean_start_date(self):
        data = self.cleaned_data['start_date']

        # check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError('Invalid date - date in past')

        # return cleaned data.
        return data


class BrigadeForm(forms.ModelForm):

    class Meta:
        model = models.Brigade
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BrigadeForm, self).__init__(*args, **kwargs)
        self.fields['brigade'].label = "Brigade name"


class CP_DetailForm(forms.ModelForm):

    class Meta:
        model = models.CP_Detail
        fields = '__all__'

        help_texts = {
            'cp_no': 'Note: The last CP detail entered here will be used as the Release Point (RP). In that case, the Halt Time you specify will be ignored.',
        }

    def __init__(self, *args, **kwargs):
        super(CP_DetailForm, self).__init__(*args, **kwargs)
        self.fields['m_id'].label = "Applies to Route"
        self.fields['cp_no'].label = "Critical Point (CP)"
        self.fields['distance'].label = "Distance (km)"
        self.fields['halt_time'].label = "Halt time (min)"


class Unit_DetailForm(forms.ModelForm):

    class Meta:
        model = models.Unit_Detail
        exclude = ['packet_allocated']

    def __init__(self, *args, **kwargs):
        super(Unit_DetailForm, self).__init__(*args, **kwargs)
        self.fields['m_id'].label = "Applies to Route"
        # if self.request.session['session_chain'] == 0:
        #     self.fields['m_id'].widget.attrs['disabled'] = False
        # else:
        #     self.fields['m_id'].widget.attrs['disabled'] = True


class Packet_DetailForm(forms.ModelForm):

    class Meta:
        model = models.Packet_Detail
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Packet_DetailForm, self).__init__(*args, **kwargs)
        self.fields['u_id'].label = "Applies to Unit"

class UnitForm(forms.ModelForm):

    class Meta:
        model = models.Unit
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UnitForm, self).__init__(*args, **kwargs)
        self.fields['unit'].label = "Unit name"
