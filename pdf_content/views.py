import os
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from fpdf import FPDF

def pdf_write_data(request):
    url = settings.SITE_URL
    if request.method == 'POST':
        pdf_content = request.POST['pdf_content']
        current_date_and_time = datetime.now().strftime("%Y-%m-%d-%H.%M.%S")
        state_file_name = 'studio45_' + current_date_and_time + '.pdf'
        path = 'studio45_pdf'
        full_path = os.path.join(path, state_file_name)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        pdf.cell(200, 10, txt="studio45", ln=1, align='C')
        pdf.cell(200, 10, txt=pdf_content,ln=2, align='C')
        pdf.output(full_path)
        if os.path.exists(full_path):
            with open(full_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/pdf")
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(full_path)
                return response
    return render(request, 'pdf/generate_pdf.html', {'url': url})
# Create your views here.
