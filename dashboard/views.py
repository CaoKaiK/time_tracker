from django.shortcuts import render

from tracker.utils import get_date, next_month, prev_month

def groupView(request):
    return render(request, 'dashboard/group.html')

def flexView(request):
    # get today's day or process navigation
    d = get_date(request.GET.get('month', None))
    

    context = {
        'prev_month': prev_month(d),
        'next_month': next_month(d),
        'cur_month': f'month={d.strftime("%Y-%m")}',
        'month_name': d.strftime("%B %Y")
    }

    return render(request, 'dashboard/flextime.html', context)
