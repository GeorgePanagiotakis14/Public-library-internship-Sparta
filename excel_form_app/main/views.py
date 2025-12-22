from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import pandas as pd
from .forms import UploadExcelForm
from .models import Person
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import PersonForm
from .models import Person
from django.db.models import Value, IntegerField
from django.db.models.functions import Cast
from django.db.models import Func

def home(request):
    return render(request, 'home.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def clean(value):
    if pd.isna(value):
        return None
    return str(value).strip()

@login_required
def show_people(request):
    people = Person.objects.all()

    from_num = request.GET.get('from_num')
    to_num = request.GET.get('to_num')

    if from_num and to_num:
        people = people.filter(
            ari8mosEisagoghs__regex=r'^\d+$',
            ari8mosEisagoghs__gte=from_num,
            ari8mosEisagoghs__lte=to_num
        )

    return render(request, 'main/people.html', {
        'people': people
    })


@login_required
def upload_excel(request):
    if request.method == 'POST':
        form = UploadExcelForm(request.POST, request.FILES)

        if form.is_valid():
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)

            added = []
            updated = []
            skipped = []

            for index, row in df.iterrows():
                ari8mos = clean(row.get('ΑΡΙΘΜΟΣ ΕΙΣΑΓΩΓΗΣ'))

                if ari8mos is None:
                    skipped.append({
                        'row': index + 2,
                        'reason': 'Missing ΑΡΙΘΜΟΣ ΕΙΣΑΓΩΓΗΣ'
                    })
                    continue

                obj, was_created = Person.objects.update_or_create(
                    ari8mosEisagoghs=ari8mos,  # PRIMARY KEY
                    defaults={
                        'hmeromhnia_eis': clean(row.get('ΗΜΕΡΟΜΗΝΙΑ ΕΙΣΑΓΩΓΗΣ')),
                        'syggrafeas': clean(row.get('ΣΥΓΓΡΑΦΕΑΣ')),
                        'koha': clean(row.get('ΣΥΓΓΡΑΦΕΑΣ KOHA')),
                        'titlos': clean(row.get('ΤΙΤΛΟΣ')),
                        'ekdoths': clean(row.get('ΕΚΔΟΤΗΣ')),
                        'ekdosh': clean(row.get('ΕΚΔΟΣΗ')),
                        'etosEkdoshs': clean(row.get('ΕΤΟΣ ΕΚΔΟΣΗΣ')),
                        'toposEkdoshs': clean(row.get('ΤΟΠΟΣ  ΕΚΔΟΣΗΣ')),
                        'sxhma': clean(row.get('ΣΧΗΜΑ')),
                        'selides': clean(row.get('ΣΕΛΙΔΕΣ')),
                        'tomos': clean(row.get('ΤΟΜΟΣ')),
                        'troposPromPar': clean(row.get('ΤΡΟΠΟΣ ΠΡΟΜΗΘΕΙΑΣ ΠΑΡΑΤΗΡΗΣΕΙΣ')),
                        'ISBN': clean(row.get('ISBN')),
                        'sthlh1': clean(row.get('Στήλη1')),
                        'sthlh2': clean(row.get('Στήλη2')),
                    }
                )
                
                record_info = {
                    'ari8mos': ari8mos,
                    'titlos': obj.titlos,
                    'syggrafeas': obj.syggrafeas,
                }

                if was_created:
                    added.append(record_info)

                else:
                    updated.append(record_info)

            return render(request, 'upload_result.html', {
                'added': added,
                'updated': updated,
                'skipped': skipped,
            })

    else:
        form = UploadExcelForm()

    return render(request, 'upload_excel.html', {'form': form})



class RegexpReplace(Func):
    function = 'REGEXP_REPLACE'
    arity = 3

def add_person(request):

    last_number = (
        Person.objects
        .exclude(ari8mosEisagoghs__isnull=True)
        .exclude(ari8mosEisagoghs__exact='')
        .annotate(
            clean_num=Cast(
                RegexpReplace(
                    'ari8mosEisagoghs',
                    Value(r'\..*$'),   # <-- ΕΔΩ Η ΔΙΟΡΘΩΣΗ
                    Value('')
                ),
                IntegerField()
            )
        )
        .order_by('-clean_num')
        .values_list('clean_num', flat=True)
        .first()
    )

    next_number = (last_number or 0) + 1

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.ari8mosEisagoghs = str(next_number)
            person.save()
            return redirect('add_person')
    else:
        form = PersonForm()

    return render(
        request,
        'main/add_person.html',
        {
            'form': form,
            'next_number': next_number
        }
    )
