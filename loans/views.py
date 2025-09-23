from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required # Import login_required
from .models import Loan
from .forms import LoanForm
# from assets.models import Asset # No longer needed for asset filter
# from django.contrib.auth import get_user_model # No longer needed for user filter

# User = get_user_model() # No longer needed for user filter

# 📋 Lista de préstamos
@login_required # Protect this view
def loan_list(request):
    all_loans = Loan.objects.select_related("asset", "user").all() # Start with all loans

    # Get filter parameters from GET request
    status_query = request.GET.get('status', '')

    # Apply filters
    if status_query:
        all_loans = all_loans.filter(status=status_query)

    prestamos = all_loans # The filtered queryset

    # Calculate metrics for the cards based on the filtered queryset
    total_loans = prestamos.count()
    active_loans = prestamos.filter(status="Activo").count()
    returned_loans = prestamos.filter(status="Devuelto").count()

    context = {
        "prestamos": prestamos,
        "status_query": status_query,
        "total_loans": total_loans,
        "active_loans": active_loans,
        "returned_loans": returned_loans,
        "loan_statuses": Loan._meta.get_field('status').choices, # Pass status choices to template
    }
    return render(request, "loans/loan_list.html", context)

# ➕ Crear préstamo
@login_required # Protect this view
def loan_create(request):
    if request.method == "POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loan_list")
    else:
        form = LoanForm()
    return render(request, "loans/loan_form.html", {"form": form})

# ✏️ Editar préstamo
@login_required # Protect this view
def loan_edit(request, pk):
    prestamo = get_object_or_404(Loan, pk=pk)
    if request.method == "POST":
        form = LoanForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            return redirect("loan_list")
    else:
        form = LoanForm(instance=prestamo)
    return render(request, "loans/loan_form.html", {"form": form})

# ❌ Eliminar préstamo
@login_required # Protect this view
def loan_delete(request, pk):
    prestamo = get_object_or_404(Loan, pk=pk)
    if request.method == "POST":
        prestamo.delete()
        return redirect("loan_list")
    return render(request, "loans/loan_confirm_delete.html", {"prestamo": prestamo})