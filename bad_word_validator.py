from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import ValidationError

BAD_WORDS = ['star wars', 'election', 'tomato']
def validate_no_bad_words(content):
  if any([word in content.lower() for word in BAD_WORDS]):
    raise ValidationError('This post contains bad words!')
 
class Post(models.Model):
  author = models.ForeignKey(User, null=True, blank=True, on_delete=CASCADE)
  content = models.CharField(max_length=140, validators=[validate_no_bad_words])
  created_on models.DateTimeField('date created', auto_now_add=True)
  
  def __str__(self):
  return '{}: {}'.format(self.author, self.content[0:20])

'''
# in views.py
def add_post(request):
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
      new_post = Post.objects.create(
        content = form.cleaned_data['content'],
        author = request.user
      )
      new_post.save()
    else:
      print(form.errors)
'''
