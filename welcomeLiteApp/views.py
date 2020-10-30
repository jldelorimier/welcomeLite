from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello, world. You're at the welcomeLiteApp index.")

def create(request):
  if request.method == 'POST':
    # populate the form with the input details
    offer = OfferForm(request.POST)
    if offer.is_valid():
        offer.save()
        return redirect('index')
  else:
    # display a new form again
    offer = OfferForm()

  context = {
    'offer': offer
  }

  return render(request, 'new.html', context)
