from django.shortcuts import render, redirect

# Create your views here.
from .forms import VpRmAllocationForm, RmCenterQuarterForm

# VP assigns vertex target to RMs
def vp_allocates_rm(request):
    if request.method == 'POST':
        form = VpRmAllocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('n_vp_allocates') 
    else:
        form = VpRmAllocationForm()
    
    return render(request, 'vp.html', {'form': form})


# RM assigns quarter-wise target to centers
def rm_allocates_center(request):
    if request.method == 'POST':
        form = RmCenterQuarterForm(request.POST)
        if form.is_valid():
            allocation = form.save(commit=False)
            allocation.rm_user = request.user 
            allocation.save()
            return redirect('n_rm_allocates')
    else:
        form = RmCenterQuarterForm()

    return render(request, 'rm.html', {'form': form})
    
