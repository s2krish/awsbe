import os
import logging
import redis

from django.shortcuts import render
from django.views.generic import TemplateView

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

        conn = redis.from_url('redis://redism1:6379/1', decode_responses=True)
        a_val = conn.get('a')

        kwargs.update({
            'USERNAME': os.environ.get('USERNAME'),
            'a_val': a_val
        })
        return super().get_context_data(**kwargs)
    

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })