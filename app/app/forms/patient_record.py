from django import forms

YES_NO = (
    (1, "YES"),
    (0, "NO"),
)

class Record(forms.Form):
    feature_2 = forms.FloatField(required = True, widget=forms.TextInput(attrs={'class': "form-control", "oninput":"this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*?)\..*/g, '$1');"}))
    feature_3 = forms.FloatField(required = True, widget=forms.TextInput(attrs={'class': "form-control", "oninput":"this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*?)\..*/g, '$1');"}))
    feature_4 = forms.FloatField(required = True, widget=forms.TextInput(attrs={'class': "form-control", "oninput":"this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*?)\..*/g, '$1');"}))
    feature_5 = forms.FloatField(required = True, widget=forms.TextInput(attrs={'class': "form-control", "oninput":"this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*?)\..*/g, '$1');"}))
    feature_37 = forms.ChoiceField(required = True, choices = YES_NO, widget=forms.Select(attrs={'class':'form-select'}))
    feature_43 = forms.ChoiceField(required = True, choices = YES_NO, widget=forms.Select(attrs={'class':'form-select'}))
    feature_44 = forms.ChoiceField(required = True, choices = ((0, "0"), (2, "2"), (3, "3"), (4, "4"),
                                                                    (5, "5"), (6, "6"), (8, "8"), (9, "9")), widget=forms.Select(attrs={'class':'form-select'}))
