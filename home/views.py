import json

from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template import loader
from django.template import Context
from django.conf import settings

from models import Portfolio


class HomePageView(TemplateView):
    """
    View for rendering home page
    """
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["user"] = Portfolio.objects.get()
        return context


class SendMessage(View):

    def post(self, request, *args, **kwargs):
        ctx = {}
        if request.is_ajax():
            name = request.POST.get('name')
            email = request.POST.get('email')
            number = request.POST.get('number')
            message = request.POST.get('message')

            thanks_template = loader.get_template('email/thanks.html')
            msg_received_template = loader.get_template('email/message_received.html')
            context = Context({'name': name, 'email': email, 'number': number, 'message': message})
            thanks_rendered = thanks_template.render(context)
            msg_received_rendered = msg_received_template.render(context)
            thanks_text_content = "Received your message"
            text_content = "Received one message"
            thanks_html_content = thanks_rendered
            msg_received_html_content = msg_received_rendered
            from_email = settings.DEFAULT_FROM_EMAIL
            thanks_msg = EmailMultiAlternatives("Re: Savad Portfolio contact",
                        thanks_text_content, from_email, [email])
            thanks_msg.attach_alternative(thanks_html_content, "text/html")
            msg_received_msg = EmailMultiAlternatives("You have one message",
                        text_content, from_email, ['savadppns@gmail.com'])
            msg_received_msg.attach_alternative(msg_received_html_content, "text/html")
            try:
                # thanks_msg.send()
                msg_received_msg.send()
            except:
                pass
        return HttpResponse(json.dumps(ctx), content_type="application/x-json")

