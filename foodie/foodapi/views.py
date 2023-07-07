from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import foods,cartitems,UserSignup,reviews
from .serializers import RegSerializer,RugSerializer,FugSerializer
from rest_framework.request import Request

# Create your views here.
@api_view(['GET'])
def getfooddata(request):
    items = foods.objects.all()
    serializer = RegSerializer(items,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getidfooddata(request,id):
    item = foods.objects.get(fid=id)
    serializer = RegSerializer(item)
    return Response(serializer.data)

@api_view(['GET'])
def getcartdata(request,id):
    items = cartitems.objects.filter(userid=id)
    serializer = RugSerializer(items,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addcartdata(request):
    serializer = RugSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def remcartdata(request,id):
    obj = cartitems.objects.get(cid=id)
    obj.delete()
    return Response({'status':200})

# @api_view(['POST'])
# def login_view(request):
#     username = request.data.get('username')
#     password = request.data.get('password')

#     user = authenticate(request,username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return Response({'message': 'Login successful'})
#     else:
#         return Response({'message': 'Invalid credentials'})

# @api_view(['POST'])
# def signup_view(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     email = request.data.get('email')

#     # Check if username is already taken
#     if User.objects.filter(username=username).exists():
#         return Response({'message': 'Username already exists'})

#     # Create the new user
#     user = User.objects.create_user(username=username, password=password, email=email)

#     return Response({'message': 'Signup successful'})

# @api_view(['GET'])
# def getusername(request):
#     username = str(request.user)
#     return JsonResponse({'username':username})

# @api_view(['POST'])
# def logout_view(request):
#     logout(request)
#     return Response({'message': 'Logout Successful'})

# @api_view(['GET'])
# def islogged(request):
#     if request.user.is_authenticated:
#         return Response(True)
#     else:
#         return Response(False)
    
@api_view(['POST'])
def usersignup(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    if UserSignup.objects.filter(username=username).exists():
        return Response({'message': 'Username already exists'})

    # Create the new user
    user = UserSignup.objects.create(username=username, password=password, email=email)

    return Response({'message': 'Signup successful'})

@api_view(['POST'])
def userlogin(request):
    username = request.data.get('username')
    password = request.data.get('password')
    userobj=UserSignup.objects.get(username=username,password=password)
    if(userobj):
        return Response({'username': username, 'userid': userobj.userid})
    else:
        return Response({'message': 'Invalid credentials'})
    
@api_view(['GET'])
def getallrevs(request,id):
    items = reviews.objects.filter(fid = id)
    serializer = FugSerializer(items,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def putrev(request):
    serializer = FugSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getrate(request,id):
    try:
        item = reviews.objects.filter(fid=id)
        rates = 0
        for i in item:
            rates = rates+i.rate
        try:
            rates = rates/len(item)
        except:
            rates = 0
    except reviews.DoesNotExist:
        rates = 0
    return Response(int(rates))