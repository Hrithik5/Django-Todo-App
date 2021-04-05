from django.shortcuts import render,redirect
from .models import List

# Create your views here.

def main(request):
    data = List.objects.all()
    return render(request,'todo_app/index.html', {'data': data})

def add(request):
    task_entered = request.POST['todoApp'] # Fetch the data entered into the field
    task = List(task = task_entered) # create a class object with the content given by the user
    task.save() # save it to the database
    return redirect(main) # return the updated page back
    
def deleteItem(request, todo_id):
    item = List.objects.get(id=todo_id) # fetch the item from the database whose id is selected
    item.delete() # delete the item
    return redirect(main) # return the updated page
    