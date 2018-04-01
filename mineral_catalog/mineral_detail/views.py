from django.shortcuts import render


def mineral_detail(request, miner):
    try:
        get_category = Category.objects.get(name=d['category'])
    except Category.DoesNotExist:
        get_category = Category.objects.create(name=d['category'])
        get_category.save()

    return render(request, 'detail.html')
