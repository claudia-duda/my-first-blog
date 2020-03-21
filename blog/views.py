from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
    # methoud request and return the model for render , where mont the model  html
    