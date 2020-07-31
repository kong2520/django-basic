from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from .models import Photo

def photo_list(request):
    # objects : ORM 관련 manager 가 objects라고 한다.
    # Photo 모델을 모두 가져와 매니져야 ! 이런 뜻이다.
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos})

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect

class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo','text'] #작성자(author), 작성시간(created)
    template_name = 'photo/upload.html'


    def form_valid(self, form):
        #author_id : 해당 필드_id 를 form에 할당해줘야한다. 장고 메뉴얼이다.
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            # 데이터올바르다면
            # instance : Photo model의 instance가 존재한다.
            # 그말은 즉 Photo model 을 save하는거랑 똑같다.
            form.instance.save()
            return redirect('/')
        else:
            # 폼오류시 form에 있는 값들을 그대로 다시 돌려줘서 render 해주는것
            return self.render_to_response({'form':form})

class PhotoDeleteView(LoginRequiredMixin,DeleteView):
    model = Photo
    success_url = '/' #지우고 나서 어디로 갈껀지
    template_name = 'photo/delete.html'

# 장고에서 UpdateView랑 UploadView에 template을 지정해주지 않으면 _form.html 을 같이 쓴다.
class PhotoUpdateView(LoginRequiredMixin,UpdateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/update.html'