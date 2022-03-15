import datetime
from django import forms
from startex import models
from django.core.exceptions import ValidationError

class StartEx_PlanForm(forms.ModelForm):
    class Meta:
        model = models.StartEx_Plan
        exclude = ('created_by', 'created_at')

        widgets = {
            'description': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }

    # def __init__(self, *args, **kwargs):
    #     super(StartEx_PlanForm, self).__init__(*args, **kwargs)
        # self.fields['created_at'].label = "Creation date"
        # self.fields['created_by'].label = "Created by"


class SX_Unit_DetailForm(forms.ModelForm):
    class Meta:
        model = models.SX_Unit_Detail
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SX_Unit_DetailForm, self).__init__(*args, **kwargs)
        self.fields['sx_id'].label = "Applies to StartEx"
        self.fields['u_id'].label = "Unit"


class SX_Vehicle_DetailForm(forms.ModelForm):
    class Meta:
        model = models.SX_Vehicle_Detail
        fields = '__all__'
        # exclude = ('packet_allocated', 'packet_auto_populted',)

    def __init__(self, *args, **kwargs):
        super(SX_Vehicle_DetailForm, self).__init__(*args, **kwargs)
        self.fields['sx_u_id'].label = "Applies to unit"
        self.fields['sx_v_id'].label = "Vehicle Name"
        self.fields['qty'].label = "Quantity"


class SX_Vehicle_DataForm(forms.ModelForm):
    class Meta:
        model = models.SX_Vehicle_Data
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SX_Vehicle_DataForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Vehicle name"
        self.fields['model'].label = "Vehicle model"
        self.fields['category'].label = "Vehicle category"
