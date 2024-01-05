from django.shortcuts import render
# TemplateViewを使うことで、簡単にテンプレートを表示することができます。
# HTMLのテンプレートをレンダリングするために使用される
# レンダリングはデータを処理もしくは演算することで画像や映像・テキストなどを表示させることです。
# from django.views.generic import TemplateView
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy

# Create your views here.
class TopView(TemplateView):
    # Viewクラスのtemplate_nameフィールドは、Viewで表示するテンプレートの名前を定義するためのフィールドです。テンプレートファイルの相対パスを指定します。
    template_name = "top.html"

# 一覧ページ用
class ProductListView(ListView):
     model = Product
    #  テンプレート名をデフォルトから変更したい場合は、Viewクラスにtemplate_nameを指定します。
    #  テンプレートファイルの相対パスで指定する必要があります。
     template_name = "list.html"
    #  「paginate_by」で1ページに表示する数を指定します。1ページに3件表示するように指定しました。
     paginate_by = 3


# 詳細ページ用
class ProductDetailView(DetailView):
     model = Product
    #  テンプレート名をデフォルトから変更したい場合は、Viewクラスにtemplate_nameを指定します。
    #  テンプレートファイルの相対パスで指定する必要があります。
    #  template_name = "detail.html"


# 新規作成用
# 商品を新規作成するためのViewを追加します。
    #  CreateViewクラスを継承したViewクラスを定義することで、新規作成フォームを効率的に作成できる  
    #  CreateViewは、モデルを作成するためのビュークラスです。
    #  フォームの表示や入力内容の処理を、自動で処理してくれます。
    #     具体的には、CreateViewには以下のような機能が提供されています。
    #     ・フォームの表示
    #     ・フォームのバリデーションチェック
    #     ・バリデーションエラーがあった場合の処理
    #     ・データベースへの保存
class ProductCreateView(CreateView):
    #  Product：対象のModelクラスを指定する
     model = Product
    #  '__all__'：新規作成時にユーザが入力するフィールドを指定する※ここでは、全フィールドを指定する
     fields = '__all__'


# 編集用
# UpdateViewは、既存のデータを更新するフォームを表示し、ユーザがフォームを送信するとそのデータを更新するViewです。
# UpdateViewを使用することで、フォームの表示、バリデーションチェック、データの更新を自動化することができます。
class ProductUpdateView(UpdateView):
     model = Product
    #  UpdateViewで使用される、fieldsパラメータは、フォームで更新可能なフィールドを指定するのに使用されます。
        # fieldsには、配列でフィールド名を指定します。値が1つであっても配列にする必要があります。
        #  UpdateViewでfieldsに指定していないフィールドは、フォームに表示されません。もちろん、更新もされません。
     fields = '__all__'
    #  template_name_suffix
    #  '_update_form'	デフォルトのTemplateファイル名が新規作成フォームと同じ「product_form.html」になるため、
    #  template_name_suffixで編集用のTemplateファイル名を指定するこの場合、
    #  Templateファイル名は「product_update_form.html」となる
     template_name_suffix = '_update_form'

# 削除用
class ProductDeleteView(DeleteView):
     model = Product
    #  DeleteViewにおいて、success_url属性にリダイレクト先のURLを指定することにより、データを削除した後にどのページに遷移させるかを制御することができます。
     success_url = reverse_lazy('list')
    #DeleteViewは単一のデータだけでなく、複数のデータも一括で削除できる
     # DeleteViewは、ユーザが削除操作を実行する前に、確認ページを表示することもできます。
     # 削除操作が簡単に実行できてしまうので、DeleteViewを使用する場合は慎重に設計する必要があります。

