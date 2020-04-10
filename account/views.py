from django.shortcuts import render, HttpResponse, redirect

from police.models import Police
from police.views import  policeview


def login(request):

    if request.method == "POST":
        userType = request.POST.get("userType")

        if userType == "Police":
            username = request.POST.get("username")
            password = request.POST.get("password")
            police = Police.objects.all().filter(username=username, password=password)


            for pol in police:
                print(pol.policeId)
                request.session['id'] = pol.policeId
                request.session['userType']="Police"

            if police:
                return redirect(policeview)
            else:

                return redirect(login)

    return render(request, "Account/login.html", {})



