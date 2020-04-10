from django.shortcuts import render
from assigncomplain.models import AssignComplainPolice
# Create your views here.
from police.models import Police


def policeview(request):

      polID = request.session.get('id')
      police = Police.objects.get(policeId=polID)
      print(police)
      assignComplainPolices = AssignComplainPolice.objects.all().filter(police=police)

      print(assignComplainPolices)
      if request.POST.get('assign'):
            print(444)
            status = request.POST.get('status')
            date = request.POST.get('date')
            time = request.POST.get('time')
            print(222)
            assignComId = int(request.POST.get('assignComId'))
            print(111)
            for assignComplainPol in assignComplainPolices:
                  if assignComplainPol.complainId==assignComId:
                        print(1222)
                        assignComplainPol.setmeetingdate=date
                        assignComplainPol.setmeetingtime = time
                        assignComplainPol.status = status
                        assignComplainPol.save()

      return render(request, "police_complain_list.html", {'assignComplainPolices': assignComplainPolices})

