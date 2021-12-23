from django.shortcuts import render
from django.http import HttpResponse
from .resources import CompanyResource
from tablib import Dataset
from .models import Company

def export(request):
    person_resource = CompanyResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response

def home(request):
    if request.method == 'POST':
        person_resource = CompanyResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(),format='xls')
        print(imported_data)
        for (a,b,c,d,e,f) in imported_data:
            print(c)


            data = a
            valuta = b
            descrizione = c
            addebiti = d
            accrediti = e
            descrizioneestesa = f


            Company.objects.create(
                data=data,
                valuta=valuta,
                descrizione=descrizione,
                addebiti=addebiti,
                accrediti=accrediti,
                descrizioneestesa=descrizioneestesa,

                )





        # 	print(data[1])
        # 	value = Company(
        # 		data[0],
        # 		data[1],
        # 		data[2],
        # 		data[3],
        # 		)
        # 	value.save()       
        
        #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        #if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'upload.html')

# # Create your views here.

def details(request):
    all_data = Company.objects.all()
    context = {
        "all_data": all_data
    }
    return render(request, 'details.html', context)

def details_new(request):
    all_data = Company.objects.filter(descrizione='Accredito Beu Con Contabile')
    context = {
        "all_data": all_data
    }
    return render(request, 'details-new.html', context)
