from django.urls import reverse_lazy
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView
from menu.models import Dish
from comments.models import Comment
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView
from .forms import ContactForm,ReservationForm,ReservationQueryForm
from .models import Reservation


def IndexView(request):
    dishes = Dish.objects.exclude(Food_Category__name='İçecek').order_by('-id')[:8]
    comments = Comment.objects.all().order_by('-id')[0:4]
    context = {
        'dishes':dishes,
        'comments':comments,
    }
    return render(request,'index.html',context)
    
class AboutView(TemplateView):
    template_name='about.html'


class ContactView(SuccessMessageMixin,FormView):
    template_name = 'contact.html'
    form_class=ContactForm
    success_url = reverse_lazy('contact')
    success_message = "Mesajınızı Aldık! En kısa sürede görüşmek üzere!!"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ReservationView(SuccessMessageMixin,FormView):
    template_name='reservation.html'
    form_class = ReservationForm
    success_url = reverse_lazy('reservation')
    success_message = "Rezervasyonunuz Aldık! Afiyet Olsun!!"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def ReservationQuery(request):
    if request.method == 'POST':
        form = ReservationQueryForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            reservation = Reservation.objects.filter(Email=email).first()
            if reservation:
                context = {'reservation': reservation ,'form': form}
                return render(request, 'reservationQuery.html', context)
            else:
                messages.error(request, 'Rezervasyon Bulunamadı')
    else:
        form = ReservationQueryForm()
    
    return render(request, 'reservationQuery.html', {'form': form})

def ReservationDelete(request,reservation_id):
    reservation = get_object_or_404(Reservation,id = reservation_id)
    reservation.delete()
    messages.info(request,'Rezervasyonunuz Başarı İle İptal Edilmiştir.Dilerseniz Yeni Randevu Oluşturabilirsiniz')
    return redirect('reservation')
