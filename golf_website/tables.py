import django_tables2 as tables
from golf_website.models import Swing


class SwingTable(tables.Table):
    class Meta:
        model = Swing
        template_name = "django_tables2/bootstrap4.html"
