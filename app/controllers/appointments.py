from app.forms import CreateAppointmentForm
from app.models import Request, Image

hours = ["09:00AM", "10:00AM", "11:00AM", "12:00PM", "01:00PM",
         "02:00PM", "03:00PM", "04:00PM", "05:00PM", "06:00PM"]


def create(request):
    try:
        form = CreateAppointmentForm(request.POST)
        year, month, day = map(int, form.data["appointment_date"].split('-'))
        appt = Request.objects.create(year=year, month=month, day=day)
        appt.data = {
            'hour': hours[form.data["hour"]],
            'service': form.data["service"],
            'name': form.data["name"],
            'phone_number': form.data["phone_number"],
            'message': form.data["message"]
        }

        if request.FILES["image"] is not None:
            image = Image(
                image=request.FILES['image'], alttext=request.POST.get("appointment_date"))
            image.save()
            appt.data["image"] = image.image.name
        appt.save()
    except:
        return {"status": 500, "message": "Something went wrong, try again in a few seconds"}
    return {"status": 200, "message": "Appointment created"}
