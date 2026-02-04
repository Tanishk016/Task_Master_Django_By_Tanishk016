
from django.shortcuts import render, redirect  # For the website
from .models import Task


from django.shortcuts import render, redirect, get_object_or_404

from .forms import TaskForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login  # To auto-login after signup


# ==========================
# PART 1: THE PROFESSIONAL WEBSITE
# ==========================

@login_required
def web_index(request):
    # 1. Handling the Input (The Form)
    if request.method == 'POST':
        form = TaskForm(request.POST) # Fill form with user data
        if form.is_valid():           # Check: Is it empty? Is it too long?
            task = form.save(commit=False)   
            task.user = request.user# Save to DB automatically
            task.save()
            return redirect('web_index')
    else:
        form = TaskForm() # Create an empty form for the page load

    # 2. Handling the Output (The List)
    tasks = Task.objects.filter(user=request.user).order_by('id')
    
    context = {
        'form': form,  # Send the form to HTML
        'tasks': tasks
    }
    return render(request, 'todo_api/index.html', context)

# SECURITY UPGRADE: Only allow POST requests for this action
@login_required
def delete_task(request, pk):
    # 1. SECURITY: Only find task if it belongs to ME (user=request.user)
    task = get_object_or_404(Task, pk=pk, user=request.user)
    
    # 2. SAFETY: Only delete if it's a POST request (not just a link click)
    if request.method == 'POST':
        task.delete()
        return redirect('web_index')
        
    # Optional: If someone tries a GET request, just send them home safely
    return redirect('web_index')

@login_required
def toggle_task(request, pk):
    # 1. SECURITY: Only find task if it belongs to ME
    task = get_object_or_404(Task, pk=pk, user=request.user)
    
    # 2. SAFETY: Only toggle if it's a POST request
    if request.method == 'POST':
        task.completed = not task.completed
        task.save()
        return redirect('web_index')
        
    return redirect('web_index')


@login_required
def edit_task(request, pk):
    # 🔒 SECURITY FIX: Only find the task if it belongs to the logged-in user!
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('web_index')
    else:
        form = TaskForm(instance=task)

    # Note: Ensure this path matches your folder structure!
    return render(request, 'todo_api/edit.html', {'form': form, 'task': task})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optional: Log them in immediately after signup
            login(request, user)
            return redirect('web_index')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})