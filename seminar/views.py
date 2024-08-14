from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Avg
from django.core.paginator import Paginator
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    DeleteView,
    UpdateView,
    )
from .models import Seminar, Review
from .consts import ITEM_PER_PAGE
from .forms import VideoForm
from .models import Seminar, Video


def index_view(request):
    object_list = Seminar.objects.order_by('-id')
    ranking_list = Seminar.objects.annotate(avg_rating=Avg('review__rate')).order_by('-avg_rating')
    paginator = Paginator(ranking_list, ITEM_PER_PAGE)
    page_number = request.GET.get('page', 1)

    page_obj = paginator.page(page_number)
    return render(
        request,
        'seminar/index.html',
        {
            'object_list': object_list,

            # 'ranking_list': ranking_list,
            'page_obj': page_obj,
        }
    )


class ListSeminarView(LoginRequiredMixin,  ListView):
    template_name = 'seminar/seminar_list.html'
    model = Seminar
    paginate_by = ITEM_PER_PAGE

class DetailSeminarView(LoginRequiredMixin, DetailView):
    template_name = 'seminar/seminar_detail.html'
    model = Seminar



# when using class-based views (CBVs) like CreateView, you don’t manually define the form in your forms.py.
#  Instead, Django auto-generates the form based on the model and fields specified in the view.
# The CreateView auto-generates a form based on the model and fields you specify. Here’s how it works:
class CreateSeminarView(LoginRequiredMixin, CreateView):
    template_name = 'seminar/seminar_create.html'
    model = Seminar
    fields = ('title', 'text', 'category', 'thumbnail')
    success_url = reverse_lazy('list-seminar')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail-seminar', kwargs={'pk': self.object.id})


class DeleteSeminarView(LoginRequiredMixin, DeleteView):
    model = Seminar
    template_name = 'seminar/seminar_delete.html'
    success_url = reverse_lazy('list-seminar')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

class UpdateSeminarView(LoginRequiredMixin, UpdateView):
    model = Seminar
    template_name = 'seminar/seminar_update.html'
    fields = ('title', 'text', 'category', 'thumbnail')
    success_url = reverse_lazy('list-seminar')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

    def get_success_url(self):
        return reverse('detail-seminar', kwargs={'pk': self.object.id})


class CreateReviewView(LoginRequiredMixin,CreateView):
    model = Review
    template_name = 'seminar/review_form.html'
    fields = ('seminar', 'title', 'text', 'rate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seminar'] = Seminar.objects.get(pk=self.kwargs['seminar_id'])
        print(context)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail-seminar', kwargs={'pk': self.object.seminar.id})


def upload_video(request, seminar_id):

    if request.method == 'POST':
        print("Handling POST request")
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")
            video = form.save(commit=False)
            video.seminar = seminar
            video.save()
            return redirect('seminar_detail', pk=seminar.id)
    else:
        form = VideoForm()
    return render(request, 'seminar/upload_video.html', {'form': form, 'seminar': seminar})


def upload_video(request, seminar_id):
    print("Entering upload_video view")
    seminar = get_object_or_404(Seminar, pk=seminar_id)
    if request.method == 'POST':
        print("Handling POST request")
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")
            video = form.save(commit=False)
            video.seminar = seminar
            video.save()
            return redirect('detail-seminar', pk=seminar.id)
        else:
            print("Form is invalid")
    else:
        form = VideoForm()
    return render(request, 'seminar/upload_video.html', {'form': form, 'seminar': seminar})
