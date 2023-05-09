from django.shortcuts import render, redirect
from .models import Category, Photo, Work, Image

# UNI-ISOL views

def add(request):
    if request.method == 'POST':
        # get all the data
        data = request.POST
        # get image from name tag
        c_image = request.FILES.get('cover_image')

        work = Work.objects.create(
            name=data['name'], 
            description=data['description'], 
            cover_image=c_image
        )
        return redirect('homepage')
        #print("data: ", data)
        #print("image: ", cover_image)
    return render(request, 'photos/add.html')

def homepage(request):
    works = Work.objects.all()
    context = {'works': works}
    return render(request, 'photos/homepage.html', context)

def workDetail(request, pk):
    detailed_work = Work.objects.get(id=pk)
    all_images = Image.objects.filter(name=detailed_work)
    context = {
        'detailed_work' : detailed_work,
        'all_images' : all_images       
    }

    # add images
    if request.method == 'POST':
        images = request.FILES.getlist('images')
        for img in images:
            new_image = Image.objects.create(
                name = detailed_work,
                image = img
            )
        return redirect('homepage')
    return render(request, 'photos/workDetail.html', context)

# Create your views here.
""" 
def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()    
    context = {'categories' : categories, 'photos' : photos}
    return render(request, 'photos/gallery.html', context) 

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {'photo' : photo}
    return render(request, 'photos/photo.html', context) 
 """
""" def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        print("data: ", data)
        # check if category already exists or cretate a new one
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image, 
        )
        return redirect('gallery')

    context = {'categories' : categories}
    return render(request, 'photos/add.html', context)  """