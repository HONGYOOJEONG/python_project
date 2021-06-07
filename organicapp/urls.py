from django.urls import path
from organicapp import views

urlpatterns=[
    path('',views.main),
    path('seed_list/',views.seed_list),
    path('seed_detail/',views.seed_detail),
    path('plantation_insect/',views.plantation_insect),
    path('plantation_idetail/',views.plantation_idetail),
    path('plantation_imageList/',views.plantation_imageList),
    path('plantation_imageDetail/',views.plantation_imageDetail),
    path('plantation_magazineList/',views.plantation_magazineList),
    path('plantation_magazineDetail/',views.plantation_magazineDetail),
    path('board/list/', views.board_list),
    path('board/insert/', views.board_insert),
    path('board/insert_ok/', views.board_insert_ok),
    path('board/detail/', views.board_detail),
    path('board/update/', views.board_update_data),
    path('board/update_ok/', views.board_update_ok),
    path('board/reply/', views.board_reply),
    path('board/reply_ok/', views.board_reply_ok),
    path('board/delete/', views.board_delete),
    path('board/delete_ok/', views.board_delete_ok),
    path('introduce_hong/',views.introduce_hong),
    path('login/',views.login),
    path('logout/',views.logout),
    path('main/',views.main),
    path('login_main/',views.login_main),
    path('book_list/',views.book_list),
    path('book_detail/',views.book_detail)


]