from django.shortcuts import render

# Create your views here.
def index(request):
    if(request.method == "POST"):
        form = carForm(request.POST)

        if(form.is_valid()):
            carModel.objects.create(carMake = request.POST["carMake"], carModel = request.POST["carModel"], year = request.POST["year"], milesPerGallon = request.POST["milesPerGallon"])
        else:
            print(form.errors)
            allEntries = carModel.objects.all()
            context = {
                "someErrors": form.errors,
                "allEntries": allEntries,
                'form': carForm()
            }
            return render(request, "ValidationApp/index.html", context)