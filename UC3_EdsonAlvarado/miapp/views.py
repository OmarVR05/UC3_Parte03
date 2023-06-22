from django.shortcuts import render, HttpResponse, redirect




def index(request):
    return render(request,'index.html')

def inicios(request):
    cursos = ['Gestion de base de datos', 'Dinamica de sistemas', 'LP3', 'Teoria general de sistemas', 'Algoritmo de computacion grafica', 'Gestion de procesos', 'Legislacion informatica']
    return render(request, 'inicios.html', {'cursos': cursos})