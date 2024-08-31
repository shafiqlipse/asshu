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


def Teachera(request):

    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES)

        if form.is_valid():
            # admin_user = User.objects.get_or_create(username="admin")
            # Assign the currently logged-in user
            form.save()
            messages.success(request, "Form submitted successfully!")
            return redirect("addteacher")

        else:
            # Add form-specific error messages for individual fields
            messages.error(request, "Form is not valid. Please check your input.")
            print(f"Form errors: {form.errors}")

    else:
        form = TeacherForm()

    context = {"form": form}
    return render(request, "teacher_new.html", context)


# def nOfficials(request):
#     # Get all officials
#     nofficials = NOC.objects.all()

#     # Apply the filter
#     official_filter = nocFilter(request.GET, queryset=nofficials)
#     filtered_officials = official_filter.qs

#     if request.method == "POST":
#         # Check which form was submitted
#         if "Accreditation" in request.POST:
#             template = get_template("noc/accreditation.html")
#             filename = "Filtered_Accreditation.pdf"
#         elif "Certificate" in request.POST:
#             template = get_template("teams/offcert.html")  # Your certificate template
#             filename = "Filtered_Certificate.pdf"
#         else:
#             return HttpResponse("Invalid form submission")

#         # Generate PDF
#         context = {"officials": filtered_officials}
#         html = template.render(context)

#         # Create a PDF
#         pdf_buffer = BytesIO()
#         pisa_status = pisa.CreatePDF(html, dest=pdf_buffer)

#         if pisa_status.err:
#             return HttpResponse("We had some errors <pre>" + html + "</pre>")

#         pdf_buffer.seek(0)

#         # Return the PDF as a response
#         response = HttpResponse(content_type="application/pdf")
#         response["Content-Disposition"] = f'attachment; filename="{filename}"'
#         response.write(pdf_buffer.getvalue())
#         return response
#     else:
#         # Render the filter form
#         return render(request, "noc/noffs.html", {"filter": official_filter})


from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO


from .filters import TeacherFilter  # Assume you have created this filter


def Teachers(request):
    # Get all teachers
    teachers = Teacher.objects.all()

    # Apply the filter
    teacher_filter = TeacherFilter(request.GET, queryset=teachers)
    filtered_teachers = teacher_filter.qs

    if request.method == "POST":
        # Generate PDF
        template = get_template("acred.html")
        context = {"teachers": filtered_teachers}
        html = template.render(context)

        # Create a PDF
        pdf_buffer = BytesIO()
        pisa_status = pisa.CreatePDF(html, dest=pdf_buffer)

        if pisa_status.err:
            return HttpResponse("We had some errors <pre>" + html + "</pre>")

        pdf_buffer.seek(0)

        # Return the PDF as a response
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = (
            'attachment; filename="Filtered_Accreditation.pdf"'
        )
        response.write(pdf_buffer.getvalue())
        return response
    else:
        # Render the filter form
        return render(request, "teachers.html", {"filter": teacher_filter})


def teacher_details(request, id):
    teacher = Teacher.objects.get(id=id)

    context = {"teacher": teacher}
    return render(request, "teacher.html", context)


def teacher_update(request, id):
    teacher = get_object_or_404(Teacher, id=id)

    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, "Teacher information updated successfully!")
            return redirect("teacher", id=teacher.id)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = TeacherForm(instance=teacher)

    context = {
        "form": form,
        "teacher": teacher,
    }
    return render(request, "update_teacher.html", context)


def teacher_delete(request, id):
    stud = Teacher.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("teachers")

    return render(request, "delete_teacher.html", {"obj": stud})
