from django.shortcuts import render

from .models import Employee

def index_view(request):
    writing_items = Employee.objects.all()

    context = {
        "writing_item": writing_items,
    }

    return render(request, "school/index.html", context)


def gallery_view(request):
    writing_items = Employee.objects.all()

    context = {
        "writing_item": writing_items,
    }

    return render(request, "school/gallery.html", context)


def portal_view(request):
    writing_items = Employee.objects.all()

    context = {
        "writing_item": writing_items,
    }

    return render(request, "school/portal.html", context)

def contacts_view(request):
    writing_items = Employee.objects.all()

    context = {
        "writing_item": writing_items,
    }

    return render(request, "school/contact.html", context)

def about_view(request):
    writing_items = Employee.objects.all()

    context = {
        "writing_item": writing_items,
    }

    return render(request, "school/about.html", context)