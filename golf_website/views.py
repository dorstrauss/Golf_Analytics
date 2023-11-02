from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from golf_website.forms import GolfUserCreationForm
from golf_website.models import GolfUser, Swing
from golf_website.sensors_logic.subscriber_thread import MQTTSubscriberThread, MQTT_BROKER
from golf_website.tables import SwingTable
from golf_website.filters import SwingFilter


class SignUpView(CreateView):
    form_class = GolfUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class SwingView(LoginRequiredMixin, TemplateView):
    template_name = 'swing.html'


@login_required
def swing_listener(request):

    subscriber_thread = MQTTSubscriberThread(mqtt_broker=MQTT_BROKER,
                                             client_name='Golf-Analytics-listener',
                                             topic=f'Golf-Analytics/{get_sensor_id_from_user(request.user)}',
                                             qos=0)
    subscriber_thread.start()
    subscriber_thread.join()
    swing_results = subscriber_thread.swing_results
    try:
        Swing(user=request.user, distance=swing_results['distance'], swing_speed=swing_results['swing_speed']).save()
    except Exception as ex:
        swing_results['error_message'] = handel_db_error(ex)

    return JsonResponse(swing_results)


def get_sensor_id_from_user(user: GolfUser):
    sensor_id = GolfUser.objects.get(pk=user.pk).sensor_id
    return sensor_id


def handel_db_error(exception: Exception):
    if type(exception) == ValidationError:
        return 'Swing distance and speed must be a positive number!'


class SwingHistoryView(LoginRequiredMixin, SingleTableMixin, FilterView):
    table_class = SwingTable
    filterset_class = SwingFilter
    paginate_by = 8

    def get_queryset(self):
        return Swing.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_table_empty'] = len(self.get_queryset()) == 0
        return context

    def get_template_names(self):
        if self.request.htmx:
            template_name = "swings_history_htmx_partial.html"
        else:
            template_name = "swings_history_htmx.html"

        return template_name
