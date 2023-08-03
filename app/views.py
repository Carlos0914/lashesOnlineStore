from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import Context, Template
from django.template.loader import render_to_string
from app.models import Product, Appointment, Image
import datetime
from dateutil.relativedelta import relativedelta
from calendar import monthrange
from django.views.decorators.csrf import csrf_protect
from app.utils.get_query_params import getQueryAttribute
from app.forms import CreateAppointmentForm
# Create your views here


def index(request: HttpRequest):
    return render(request, "index.html", {})


def catalog(request: HttpRequest):
    products = Product.objects.all()
    for product in products:
        product.image_list = list(map(lambda x: x.image, product.images.all()))

    return render(request, "catalog.html", {"products": products})


@csrf_protect
def schedule(request: HttpRequest):
    # Get the agenda for the following 6 months, if not available create the data as fully available
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        if request.FILES["image"] is not None:
            image = Image(image=request.FILES['image'], alttext=request.POST.get("appointment_date"))
            image.save()
            print(image)

    info = []
    date = request.GET.get("date")
    for i in range(6):
        appt = None
        date = datetime.date.today()+relativedelta(months=i)
        try:
            appt = Appointment.objects.get(year=date.year, month=date.month)
        except:
            appt = Appointment(year=date.year, month=date.month)
            appt.days = [{"spots": 9, "available": [True for _ in range(9)]} for _ in range(
                monthrange(appt.year, appt.month)[1])]
            appt.save()
        info.append(appt.days)
    rendered_form = CreateAppointmentForm()
    rendered_form = rendered_form.render("appointment_form.html")

    return render(request, "schedule.html", {"info": info, "form": rendered_form})


def location(request: HttpRequest):
    return render(request, "location.html", {})
