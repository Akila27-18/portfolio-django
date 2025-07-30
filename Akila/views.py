from django.shortcuts import render, redirect

# Sample project data (static for now)
def get_projects():
    return [
        {"name": "Lotus Boutique", "url": "https://akila27-18.github.io/Lotus-Boutique/index.html", "image": "LB-logo.jpeg"},
        {"name": "Akila's Portfolio", "url": "https://akila27-18.github.io/Portfolio", "image": "portfolio.jpg"},
        {"name": "Nutrition Website", "url": "https://akila27-18.github.io/Nutrition/index.html", "image": "nutrition.jpg"},
        {"name": "Organic Farming Website", "url": "https://akila27-18.github.io/OrganicFarming", "image": "farming.png"},
        {"name": "Vetri Supermarket Billing Layout", "url": "https://akila27-18.github.io/billing", "image": "supermarket.jpg"},
        {"name": "Employee Payslip", "url": "https://akila27-18.github.io/payslip/", "image": "employee.jpg"},
        {"name": "Grocery Ecommerce Website", "url": "https://akila27-18.github.io/Grocery", "image": "grocery.jpg"},
        {"name": "Zahirx Service Website", "url": "https://akila27-18.github.io/Zahirx", "image": "zahirx.jpg"},
        {"name": "Medical Billing", "url": "https://akila27-18.github.io/medicalbilling", "image": "Medical.png"},
    ]

# Home Page
def home(request):
    return render(request, 'home.html')

# About Page
def about(request):
    return render(request, 'about.html')

# Projects Page
def projects_page(request):
    projects = get_projects()
    return render(request, 'projects.html', {'projects': projects})

# Contact Page
def contact(request):
    if request.method == 'POST':
        # You can handle form data here later
        return redirect('thankyou')
    return render(request, 'contact.html')

# Thank You Page
def thankyou(request):
    return render(request, 'thankyou.html')
