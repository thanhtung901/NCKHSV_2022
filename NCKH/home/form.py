from .models import light_control
from django.forms import ModelForm, inlineformset_factory


class LightControlForm(ModelForm):
    class Meta:
        model = light_control

bookform = inlineformset_factory(light_control,
    fields =('status','time'), extra=1, can_delete = False)