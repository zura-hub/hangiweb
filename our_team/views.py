
from django.shortcuts import render, get_object_or_404
from .models import GroupPhoto, Employee,  Team
from main.models import lists

def team(request):
    groupphoto = GroupPhoto.objects.all()
    employees = Employee.objects.all()
    list_items = lists.objects.all()
    teams = Team.objects.all()
    return render(request, 'our_team/team.html', {'team':teams, 'GroupPhoto':groupphoto, 'employees': employees,  'lists': list_items})

def employee_detail(request, employee_id):
    list_items = lists.objects.all()
    teams = Team.objects.all()
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'our_team/employee_detail.html', {'team':teams, 'employee': employee,  'lists': list_items})
