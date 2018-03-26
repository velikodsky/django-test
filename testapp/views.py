from django.shortcuts import render

def post_list(request):
    return render(request, 'testapp/post_list.html', {})
