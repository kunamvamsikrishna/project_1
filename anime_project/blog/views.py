from django.http import HttpResponse
from .models import *
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *

def create(request):
    if request.method == "POST":
        req= request.POST
        name = request.POST.get('name')
        des = request.POST.get('des')
        date = request.POST.get('date')
        rating = req.get('rating')
        Anime.objects.create(title=name,description=des,release_date=date,rating=rating)
        return redirect('rendeer')
        print(name,rating)
    return render(request,'from.html')

def rendeer(request):
    postt = Anime.objects.all()
    print(postt)
    context = {
        'posts': postt
    }
    return render(request,'dis.html',context)

def update_data(request,id):
    post = Anime.objects.get(id=id)
    if request.method == "POST":
        post.description = request.POST.get("des")
        post.save()
        return redirect('rendeer')
        # Anime.objects.update(title=name,description=des,release_date=date,rating=rating)
    context = {
        'post': post
    }
    return render(request,'update.html',context)

def delete_data(request,id):
    post  = Anime.objects.get(id=id)
    post.delete()
    return redirect("rendeer")

def delete(request, id):
    post = Anime.objects.get(id=id)
    post.delete()
    return HttpResponse("Post with id {} deleted successfully!".format(id))

def update(request, id):
    post = Anime.objects.get(id=id)
    post.title =  "JJK"
    post.description = "Updated Description"
    post.release_date = "2023-10-03"
    post.rating = 9.0
    post.save()
    return HttpResponse("Post with id {} updated successfully!".format(id))




def create_phone(request):
    if request.method =="POST":
        name=request.POST.get('name')
        company=request.POST.get('company')
        camera= request.POST.get('camera')
        price = request.POST.get('price')
        battery = request.POST.get('battery')
        post = Phone.objects.create(name=name,company=company,camera=camera,price=price,battery=battery)
    return render(request,'phone_c.html')

def  rendeer_phone(request):


    post=Phone.objects.all()
    context = {'phones':post}
    return render(request,'phone_dis.html',context)

def update_phone(request,id):
    post = Phone.objects.get(id=id)


    if request.method == "POST":
        post.name=request.POST.get("name")
        post.company=request.POST.get("company")
        post.camera=request.POST.get("camera")
        post.price=request.POST.get("price")    
        post.battery=request.POST.get("battery")
        post.save()
        return redirect('rendeer_phone')
    
    context={
        'phone':post
    }
    return render(request,'update_phone.html',context)

def delete_phone(request,id):
    post = Phone.objects.get(id=id)
    post.delete()
    return redirect('rendeer_phone')

@api_view(["GET", "POST"])
def get_user(request):
    if(request.method == "GET"):
        user= MyUser.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response({"data":serializer.data})
    elif(request.method == "POST"):
        serilizer = UserSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({"data":serilizer.data})
        return Response({"data":"created"})