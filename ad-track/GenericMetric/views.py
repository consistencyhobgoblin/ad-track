from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

#def index(request):
#    dtNow = datetime.now()

#    sHtmlContent = "<html><head><title>Generic Metric</title></head><body>"
#    sHtmlContent += "<strong>Generic Metric Data Entry</strong> on " + dtNow.strftime("%A, %d %B, %Y at %X")
#    sHtmlContent += "</body></html>"

#    return HttpResponse(sHtmlContent)

def index(request):
    dtNow = datetime.now()

    return render(
    request,
    "GenericMetric/index.html",  # Relative path from the 'templates' folder to the template file
    # "index.html", # Use this code for VS 2017 15.7 and earlier
    {
        'title' : "Generic Metric",
        'message' : "Generic Metric Data Entry",
        'content': " on " + dtNow.strftime("%A, %d %B, %Y at %X")
    }
    )

# Create your views here.
