import random

from django import forms
from django.shortcuts import render, get_object_or_404

from .models import Mineral


def mineral_detail(request, mineral_id):
    mineral = get_object_or_404(Mineral, pk=mineral_id)

    class MineralForm(forms.ModelForm):
        class Meta:
            model = Mineral
            fields = ['strunz', 'crystal_system', 'cleavage', 'mohs_scale',
                      'unit_cell', 'color', 'crystal_symmetry',
                      'luster', 'streak', 'diaphaneity', 'optical_prop',
                      'refractive_index', 'crystal_habit',
                      'specific_gravity', 'group']
            labels = {
                'strunz': 'Strunz Classification',
                'mohs_scale': 'Mohs Scale Hardness'
            }

    mineral_form = MineralForm(instance=mineral)

    all_mineral_count = Mineral.objects.all().count()
    rand_num = random.randint(1, all_mineral_count)

    context = {
        'mineral': mineral,
        'mineral_form': mineral_form,
        'rand_mineral': rand_num,
    }

    return render(request, 'detail.html', context)
