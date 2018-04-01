import random


from django.shortcuts import render


from mineral_detail.models import Mineral

def index(request):
    all_minerals = Mineral.objects.all()
    rand_num = random.randint(1, all_minerals.count())

    context = {'minerals': all_minerals,
               'rand_mineral': rand_num}

    return render(request, 'index.html', context)
