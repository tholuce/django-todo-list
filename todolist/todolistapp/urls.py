from django.urls import path
from todolistapp.views import IndexView, log_in, sign_up, profile, log_out, add_todo_item, delete_todo_item

app_name='todoapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', log_in, name='login'),
    path('signup/', sign_up, name='signup'),
    path('profile/', profile, name='profile'),
    path('logout/', log_out, name='logout'),
    path('todo/add/', add_todo_item, name='addtodo'),
    path('todo/delete/<int:item_id>', delete_todo_item, name='deletetodo')
]
