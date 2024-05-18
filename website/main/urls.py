from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('postanovka/', views.postanovka, name='postanovka'),
    path('yravnenie/', views.yravnenie, name='yravnenie'),
    path('analiz/', views.analiz, name='analiz'),
    path('zakl/', views.zakl, name='zakl'),
    path('pred/', views.pred, name='pred'),
    path('obraz/', views.obraz, name='obraz'),
    path('gg/', views.gg, name='gg'),
    path('fig01/', views.fig01, name='fig01'),
    path('tabl/', views.tabl, name='tabl'),
    path('yravcv/', views.yravcv, name='yravcv'),
    path('yravdv/', views.yravdv, name='yravdv'),
    path('kin/', views.kin, name='kin'),
    path('yprav/', views.yprav, name='yprav'),
    path('anali/', views.anali, name='anali'),
    path('dvvp/', views.dvvp, name='dvvp'),
    path('xoty/', views.xoty, name='xoty'),
    path('xotyokr/', views.xotyokr, name='xotyokr'),
    path('vota/', views.vota, name='vota'),
    path('votaokr/', views.votaokr, name='votaokr'),
    path('x_ot_y_okr_fi/', views.x_ot_y_okr_fi, name='x_ot_y_okr_fi'),
    path('x_ot_y_okr_op/', views.x_ot_y_okr_op, name='x_ot_y_okr_op'),
    path('dvvo/', views.dvvo, name='dvvo'),
    path('biz1/', views.biz1, name='biz1'),
    path('biz2/', views.biz2, name='biz2'),
    path('kil3/', views.kil3, name='kil3'),
    path('yef4/', views.yef4, name='yef4'),
    path('biz5/', views.biz5, name='biz5'),
    path('iv6/', views.iv6, name='iv6')
]
