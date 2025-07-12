from django.shortcuts import render

# Create your views here.

# views.py

from django.shortcuts import render, redirect
from .forms import AssignRegionForm, AssignCenterForm, BatchForm, EnrollmentForm
from .models import CreateBatch, Enrollment, AssignRegion, AssignCenter

def assign_region_to_rm(request):
    if request.method == 'POST':
        form = AssignRegionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('n_assign_region')  
    else:
        form = AssignRegionForm()
        
    assignments = AssignRegion.objects.select_related('rm_user')
    return render(request, 'assign.html', {
        'vpform': form,
        'region_assign': assignments
    })


def assign_center_to_cm(request):
    if request.method == 'POST':
        form = AssignCenterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('n_assign_center')  
    else:
        form = AssignCenterForm()
        
    assignments = AssignCenter.objects.select_related('cm_user')
    return render(request, 'assign.html', {
        'rmform': form,
        'center_assign': assignments
    })


# CM creates batches
def create_batch(request):
    if request.method == 'POST':
        form = BatchForm(request.POST)
        if form.is_valid():
            batch = form.save(commit=False)
            batch.cm_user = request.user  # Logged-in CM
            batch.save()
            return redirect('n_create_batch')
    else:
        form = BatchForm()

    return render(request, 'create_batch.html', {'form': form})


# CM enrolls students to batches
def enroll_student(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('n_batchdetails')
    else:
        form = EnrollmentForm()

    return render(request, 'create_batch.html', {'form': form})


def batch_list(request):
    batches = CreateBatch.objects.all().order_by('-start_date')  # newest first
    return render(request, 'batch_list.html', {'batches': batches})


from django.shortcuts import render, get_object_or_404, redirect

def batch_details(request, pk):
    batch = get_object_or_404(CreateBatch, pk=pk)
    enroll = Enrollment.objects.filter(batch=batch)

    show_form = False
    form = EnrollmentForm(initial={'batch': batch})

    if request.method == 'POST' and request.user.role == 'cm':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.batch = batch  # Assign batch manually
            enrollment.save()
            return redirect('batch_detail', pk=batch.pk)  # reload page

        show_form = True  # if form invalid, still show form

    # If CM clicked "Add Enrollment" (GET param)
    if request.GET.get('add') == '1' and request.user.role == 'cm':
        show_form = True

    return render(request, 'project_details.html', {
        'batch': batch,
        'enroll': enroll,
        'form': form,
        'show_form': show_form
    })
