from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import FitnessClass, UserClass
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

def classes(request):
    classes = FitnessClass.objects.all()
    my_classes = UserClass.objects.filter(user=request.user).values_list('fitness_class', flat=True) if request.user.is_authenticated else []
    return render(request, 'classes.html', {'classes': classes, 'my_classes': list(my_classes)})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserClass, FitnessClass

@login_required
def my_classes(request):
    # Fetch all user classes for the current user
    user_classes = UserClass.objects.filter(user=request.user)

    valid_classes = []

    # Loop over user classes and only include those with a valid fitness_class
    for uc in user_classes:
        try:
            # Check if the fitness_class is valid (exists in the database)
            fitness_class = uc.fitness_class
            # If the fitness_class exists, add it to valid_classes
            valid_classes.append(fitness_class)
        except FitnessClass.DoesNotExist:
            # If the fitness_class no longer exists, delete the UserClass entry
            uc.delete()

    # Prepare classes and their IDs for rendering
    my_classes = [c.id for c in valid_classes]


    # Render the template with valid classes only
    return render(request, 'classes.html', {'classes': valid_classes, 'my_classes': my_classes})


@login_required
@require_POST
def add_to_my_classes(request, class_id):
    fitness_class = get_object_or_404(FitnessClass, id=class_id)
    existing = UserClass.objects.filter(user=request.user, fitness_class=fitness_class).exists()
    
    # Check if the class is already in the user's classes
    if existing:
        return JsonResponse({'status': 'error', 'message': "This class is already in your list."})

    # Check the capacity of the class
    if fitness_class.capacity > 0:
        UserClass.objects.create(user=request.user, fitness_class=fitness_class, date=timezone.now().date())
        fitness_class.capacity -= 1
        fitness_class.save()
        return JsonResponse({'status': 'success', 'message': f"{fitness_class.name} successfully added to your classes!"})
    else:
        return JsonResponse({'status': 'error', 'message': "This class is full."})

@login_required
@require_POST
def remove_from_my_classes(request, class_id):
    fitness_class = get_object_or_404(FitnessClass, id=class_id)
    try:
        user_class = UserClass.objects.get(user=request.user, fitness_class=fitness_class)
        user_class.delete()
        fitness_class.capacity += 1  # Increase capacity when class is removed
        fitness_class.save()
        return JsonResponse({'status': 'success', 'message': f"{fitness_class.name} successfully removed from your classes!"})
    except UserClass.DoesNotExist:
        logger.error("Attempted to remove a class that does not exist for user %s: %s", request.user.username, fitness_class.id)
        return JsonResponse({'status': 'error', 'message': "This class is not in your list."})
    except Exception as e:
        logger.exception("Error occurred while removing class: %s", str(e))
        return JsonResponse({'status': 'error', 'message': "An unexpected error occurred."})