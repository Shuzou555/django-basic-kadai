"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud import views

# URL設定では、ブラウザから送られるHTTPリクエストに応じて、表示するページを指示します。このことをルーティングといいます。
# path関数はルーティングを設定する際に使用します。
# 関数Viewの場合
# path(URL, 関数, name=URLの名前)
# クラスViewの場合
# path(URL, クラス.as_view(), name=URLの名前)
# path関数の第3引数には、URLに名前を付ける際に使用する名前を指定します。
# URLパターンに変数を含めるためには<>を使用します。
urlpatterns = [
    # 管理ページを表示できるように指定します
    path("admin/", admin.site.urls),
    # トップページを表示できるように指定します
    path('', views.TopView.as_view(), name="top"),
    # 一覧ページを表示できるように指定します
    path('crud/', views.ProductListView.as_view(), name="list"),
    # 詳細ページを表示できるように指定します 
    path('crud/detail/<int:pk>', views.ProductDetailView.as_view(), name='detail'),
    # ProductCreateViewクラスを実行するように指定します。
    path('crud/new/', views.ProductCreateView.as_view(), name="new"),
    # 編集画面にアクセスした場合のルーティングを設定します。
    path('crud/edit/<int:pk>', views.ProductUpdateView.as_view(), name="edit"),
    # 削除画面にアクセスした場合のルーティングを設定します。
    path('crud/delete/<int:pk>', views.ProductDeleteView.as_view(), name="delete"),
]
