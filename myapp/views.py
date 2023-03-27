import logging
from django.shortcuts import render
from django.views.generic import TemplateView
import os

logger = logging.getLogger('ldjango')

class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        # print ("Hello world 23423432432")
        # print ('os.environ.get test', os.environ.get('ALARM_URL', 'no environment initialzed'))
        logger.info("Info log")
        logger.warn("Warning log")
        logger.debug("Debug log")
        logger.error("Error log")
        kwargs.update({
            'USERNAME': os.environ.get('USERNAME')
        })
        return super().get_context_data(**kwargs)
    

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })