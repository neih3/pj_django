from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import User

# Create your views here.

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        # Trích xuất URL
        request_url = request.build_absolute_uri()
        
        # Trích xuất method
        request_method = request.method
        
        # Trích xuất headers
        request_headers = request.headers
        
        # Trích xuất body
        request_body = request.body.decode('utf-8')  # decode body nếu cần
        
        # In ra các thành phần đã trích xuất
        print("Request URL:", request_url)
        print("Request Method:", request_method)
        print("Request Headers:", request_headers)
        print("Request Body:", request_body)
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User(username=username, password = password)
        user.save()
        # In ra form
        
        print("Username:", username)
        print("Password:", password) 
        print(type(username))
        #chuyển hướng sang link có name =  'login_form/'
        return redirect("login_form")
    else:
        return render(request, 'login.html')
def login_form(request):
    return render(request,'login_form.html')
