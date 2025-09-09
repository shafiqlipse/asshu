from django.shortcuts import render, redirect, get_object_or_404

from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse


from django.contrib import messages


# from dashboard.filters import *
from xhtml2pdf import pisa
from io import BytesIO

# Create your views here.
from .models import *
from .forms import *


def Membera(request):

    if request.method == "POST":
        form = MemberForm(request.POST, request.FILES)

        if form.is_valid():
            # admin_user = User.objects.get_or_create(username="admin")
            # Assign the currently logged-in user
            form.save()
            messages.success(request, "Form submitted successfully!")
            return redirect("addmember")

        else:
            # Add form-specific error messages for individual fields
            messages.error(request, "Form is not valid. Please check your input.")
            print(f"Form errors: {form.errors}")

    else:
        form = MemberForm()

    context = {"form": form}
    return render(request, "member_new.html", context)





from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO


from .filters import MemberFilter  # Assume you have created this filter


def Members(request):
    # Get all members
    members = Member.objects.all()

    # Apply the filter
    member_filter = MemberFilter(request.GET, queryset=members)
    filtered_members = member_filter.qs

    if request.method == "POST":
        # Check which form was submitted
        if "Accreditation" in request.POST:
            template = get_template("member_acred.html")
            filename = "Asshu_Accreditation.pdf"
        elif "Certificate" in request.POST:
            template = get_template(
                "certificate_temaplate.html"
            )  # Your certificate template
            filename = "Filtered_Certificate.pdf"
        else:
            return HttpResponse("Invalid form submission")

        # Generate PDF
        context = {"members": filtered_members}
        html = template.render(context)

        # Create a PDF
        pdf_buffer = BytesIO()
        pisa_status = pisa.CreatePDF(html, dest=pdf_buffer)

        if pisa_status.err:
            return HttpResponse("We had some errors <pre>" + html + "</pre>")

        pdf_buffer.seek(0)

        # Return the PDF as a response
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="{filename}"'
        response.write(pdf_buffer.getvalue())
        return response
    else:
        # Render the filter form
        return render(request, "members.html", {"filter": member_filter})


def member_details(request, id):
    member = Member.objects.get(id=id)

    context = {"member": member}
    return render(request, "member.html", context)


def member_update(request, id):
    member = get_object_or_404(Member, id=id)

    if request.method == "POST":
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, "Member information updated successfully!")
            return redirect("member", id=member.id)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = MemberForm(instance=member)

    context = {
        "form": form,
        "member": member,
    }
    return render(request, "update_member.html", context)

def activate_member(request, id):
    member = get_object_or_404(Member, id=id)
    member.status = "Verified"
    member.save()
    messages.success(request, "Member Verified successfully.")  # alert message
    return redirect("members") 

def member_delete(request, id):
    stud = Member.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("members")

    return render(request, "delete_member.html", {"obj": stud})


import csv
from django.http import HttpResponse


def export_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="data.csv"'

    # Create a CSV writer object using the HttpResponse as the file.
    writer = csv.writer(response)

    # Write the header row
    writer.writerow(
        [
            "id",
            "first_name",
            "last_name",
            "school",
            "designation",
            "contact",
            "district",
            "region",
        ]
    )  # Replace with your model's fields

    # Write data rows
    for obj in Member.objects.all():
        writer.writerow(
            [
                obj.id,
                obj.first_name,
                obj.last_name,
                obj.school,
                obj.designation,
                obj.contact,
                obj.district,
                obj.region,
            ]
        )  # Replace with your model's fields

    return response
