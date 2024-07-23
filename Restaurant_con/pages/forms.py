from django import forms
from.models import Contact,Reservation
from datetime import date,datetime
import datetime

class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'İsminiz',
        }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Telefon Numaranız',
        }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Mailiniz',
        }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Mesajınız',
        }))
    
    class Meta:
        model = Contact
        fields=['name','phone','email','message']



class ReservationForm(forms.ModelForm):
    list_of_hours = {str(x)+'.00':str(x) +'.00' for x in range(9,19)}
    First_Name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'İsminiz',
        }))
    Last_Name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Soyisminiz',
        }))
    Phone = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Telefon Numaranız',
        }))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Mailiniz',
        }))
    person = forms.IntegerField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Kişi Sayısı',
        }))
    hour = forms.ChoiceField(choices=list_of_hours,widget=forms.Select(attrs={
        'class':'form-control',
    }))
    Date = forms.DateField(widget=forms.DateInput(attrs={
        'class' : 'form-control',
        'type':'date'
    }))

    class Meta:
        model = Reservation
        fields = ['First_Name','Last_Name','Phone','Email','person','hour','Date']
        
    def clean_Date(self):
        selected_date = self.cleaned_data.get('Date')
        str_selected_date = str(self.cleaned_data.get('Date'))
        selected_hour = self.cleaned_data.get('hour')
        if len(selected_hour) == 4:
            selected_hour = '0' + selected_hour
        date_ = datetime.datetime.strptime(str_selected_date,"%Y-%m-%d").date()
        day_name = date_.strftime('%A')

        if (day_name == 'Friday' or day_name  == 'Saturday' or day_name == 'Sunday') and (selected_hour =='9.00' or selected_hour =='18.00'): 
            raise forms.ValidationError("Girdiğiniz gün için 09.00 ve 18.00 saatleri mevcut değildir.")
        if selected_date and selected_date < date.today():
            raise forms.ValidationError("Girdiğiniz tarih " +str(date.today().__format__("%d.%m.%Y")) +" önce olamaz.")
        elif selected_hour and int(selected_hour[:2]) <= datetime.datetime.now().hour and selected_date == date.today:
            raise forms.ValidationError("Seçtiğiniz saat " + str(datetime.datetime.now().hour) + ".00'dan sonra olmalıdır.")
        return selected_date
    
class ReservationQueryForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Mailiniz'
    }))
