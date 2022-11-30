from django.shortcuts import render
from django.views import View

from nyc.boroughs import boroughs


class CityView(View):
    def get(self, request):
        return render(request=request, template_name='city.html', context={'boroughs': boroughs.keys()})


class BoroughView(View):
    def get(self, request, borough):
        return render(
            request=request,
            template_name='borough.html',
            context={'borough': borough, 'activities': boroughs[borough].keys()},
        )

class ActivityView(View):
    def get(self, request, borough, activity):
        print(borough, activity)
        return render(
            request=request,
            template_name='activity.html',
            context={'borough': borough, 'activity': activity, 'places': boroughs[borough][activity].keys()},
        )


class VenueView(View):
    class VenueView(View):
        def get(self, request, borough, activity, venue):
            print(borough, activity, venue)
            return render(
            request=request, 
            template_name= 'venue.html',
            context={'borough': borough, 'activity': activity, 'locations': boroughs[borough][activity][venue].keys()},

        )
