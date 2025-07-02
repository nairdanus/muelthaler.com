from django.shortcuts import render

def scroll_page_view(request):
    return render(request, 'kam/kam.html')
