from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import product
from django.utils import timezone

def home(request):
    products=product.objects
    return render(request,'products/home.html',{"Product":products})

@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            Prod=product()
            Prod.title=request.POST['title']
            Prod.body=request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                Prod.url=request.POST['url']
            else:
                Prod.url='http://'+request.POST['url']
            Prod.icon=request.FILES['icon']
            Prod.image=request.FILES['image']
            Prod.pub_date= timezone.datetime.now()
            Prod.hunter=request.user
            Prod.save()#to insert the values into the model
            return redirect('/products/'+str(Prod.id))
            
        else:
            return render(request,'products/create.html',{"error":"fill in the mandatory fields"})

    else:
        return render(request,'products/create.html')

def detail(request,product_id):
    Product=get_object_or_404(product,pk=product_id)
    return render(request,'products/detail.html',{'product':Product})

@login_required(login_url="/accounts/signup")
def upvote(request,product_id):
    if request.method == 'POST':
        Product=get_object_or_404(product,pk=product_id)
        Product.votes_total=Product.votes_total+1
        Product.save()
        return redirect('/products/'+str(Product.id))