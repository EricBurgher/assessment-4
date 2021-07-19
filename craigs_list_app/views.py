from django.shortcuts import render
from django.http import HttpResponse
from craigs_list_app.models import Categories, Posts

def index(request):
    info = {
        "all_categories": Categories.objects.all()
    }
    return render(request, "pages/categories/category_list.html", info)

def category_detail(request, category_id):
    try:
        category = Categories.objects.get(id=category_id)
    except:
        return HttpResponse("A category with id {category_id} doesn't exist!")

    info = {
        "category": category
    }
    return render(request, "pages/categories/category_detail.html", info)

def post_list(request, category_id):
    try:
        category = Categories.objects.get(id=category_id)
    except:
        return HttpResponse("A category with id {category_id} doesn't exist!")
    info = {
        "category": category
    }
    return render(request, "pages/posts/post_list.html", info)

def post_new(request, category_id):
     try:
         category = Categories.objects.get(id=category_id)
     except:
         return HttpResponse(f"A category with id {category_id} doesn't exist!")
     form = PostsForm(request.POST or None, initial={"category": category})
     return process_post_form(request, "Add", form, category)


def post_update(request, category_id, post_id):
     try:
         post = Posts.objects.get(id=post_id)
     except:
         return HttpResponse(f"A post with id {post_id} doesn't exist!")
     form = PostsForm(request.POST or None, instance=post)
     return process_post_form(request, "Update", form, post.category)

def process_post_form(request, action, form, category):
     post = None
     if request.method == "POST":
         try:
             post = form.save()
             return redirect("post_detail", category_id=post.category.id, post_id=post.id)
         except:
             return HttpResponse("Wamp wamp!")
     info = {
         "action": action,
         "category": category,
         "form": form
     }
     return render(request, "pages/posts/post_form.html", info)

def post_delete(request, category_id, post_id):
     try:
         post = Posts.objects.get(id=post_id)
         post.delete()
     except:
         return HttpResponse(f"A post with id {post_id} doesn't exist!")

     return redirect("post_list", category_id=category_id)