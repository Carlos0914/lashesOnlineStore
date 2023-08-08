from django.http import HttpRequest
from django.shortcuts import render, redirect
from app.models import Product, Agenda
import datetime
from dateutil.relativedelta import relativedelta
from calendar import monthrange
from django.views.decorators.csrf import csrf_protect
from django.contrib.admin.views.decorators import staff_member_required
from app.forms import CreateAppointmentForm
from app.controllers.appointments import create as createAppointment
# Create your views here



def index(request: HttpRequest):
    return render(request, "index.html", {})


def catalog(request: HttpRequest):
    products = Product.objects.all()
    for product in products:
        product.image_list = list(map(lambda x: x.image, product.images.all()))

    return render(request, "catalog.html", {"products": products})

@staff_member_required
def requests(request: HttpRequest):
    return render(request, "requests.html",{})


@csrf_protect
def schedule(request: HttpRequest):
    # Get the agenda for the following 6 months, if not available create the data as fully available
    if request.method == "POST":
        createAppointment(request)
        return redirect('/')

    info = []
    for i in range(6):
        appt = None
        date = datetime.date.today()+relativedelta(months=i)
        try:
            appt = Agenda.objects.get(year=date.year, month=date.month)
        except:
            appt = Agenda(year=date.year, month=date.month)
            appt.data = [{"spots": 9, "available": [None for _ in range(9)]} for _ in range(
                monthrange(appt.year, appt.month)[1])]
            appt.save()
        info.append(appt.data)
    rendered_form = CreateAppointmentForm()
    rendered_form = rendered_form.render("appointment_form.html")

    return render(request, "schedule.html", {"info": info, "form": rendered_form})


def location(request: HttpRequest):
    return render(request, "location.html", {})
