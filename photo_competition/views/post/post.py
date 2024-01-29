from django.shortcuts import render
from django.views import View
from models_app.models import Post

'''
class PostListView(View):
как отфильтровать посты со стасщим опубликован
'''


class PostListView(View):
    def get(self, request, *args, **kwargs):
        p = [1, 2, 3]
        # posts = Post.objects.filter(status=Post.????).order_by(
        #     '-updated_at'
        # )

        # return render(
        #     request,
        #     'index.html',
        #     context={
        #         'posts': Post.objects.all()
        #     }
        # )
        return render(
            request,
            'index.html',
            context={
                'posts': p
            }
        )


def index(request):
    return render(request, 'photo_competition/index.html', {})


class PostCreateView(View):
    def post(self, request, *args, **kwargs):
        data = request.Post
        ...
