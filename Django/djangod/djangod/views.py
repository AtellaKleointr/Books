from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class BookDetailView(TemplateView):
    template_name = 'book_detail.html'

class StatisticsView(TemplateView):
    template_name = 'statistics.html'