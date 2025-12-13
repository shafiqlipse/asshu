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


def studenta(request):

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            # admin_user = User.objects.get_or_create(username="admin")
            # Assign the currently logged-in user
            form.save()
            messages.success(request, "Form submitted successfully!")
            return redirect("addstudent")

        else:
            # Add form-specific error messages for individual fields
            messages.error(request, "Form is not valid. Please check your input.")
            print(f"Form errors: {form.errors}")

    else:
        form = StudentForm()

    context = {"form": form}
    return render(request, "student_new.html", context)





from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO


from .filters import StudentFilter  # Assume you have created this filter


def students(request):
    # Get all students
    students = Student.objects.all()

    # Apply the filter
    student_filter = StudentFilter(request.GET, queryset=students)
    filtered_students = student_filter.qs

    if request.method == "POST":
        # Check which form was submitted
        if "Accreditation" in request.POST:
            template = get_template("student_acred.html")
            filename = "Asshu_Accreditation.pdf"
        elif "Certificate" in request.POST:
            template = get_template(
                "certificate_student.html"
            )  # Your certificate template
            filename = "Filtered_Certificate.pdf"
        else:
            return HttpResponse("Invalid form submission")

        # Generate PDF
        context = {"students": filtered_students}
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
        return render(request, "students.html", {"filter": student_filter})


def student_details(request, id):
    student = Student.objects.get(id=id)

    context = {"student": student}
    return render(request, "student.html", context)


def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student information updated successfully!")
            return redirect("student", id=student.id)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = StudentForm(instance=student)

    context = {
        "form": form,
        "student": student,
    }
    return render(request, "update_student.html", context)

def activate_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.status = "Verified"
    student.save()
    messages.success(request, "Student Verified successfully.")  # alert message
    return redirect("students") 

def student_delete(request, id):
    stud = Student.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("students")

    return render(request, "delete_student.html", {"obj": stud})


import csv
from django.http import HttpResponse


def export_scsv(request):
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
    for obj in Student.objects.all():
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
