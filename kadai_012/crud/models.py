from django.db import models
from django.urls import reverse


class Category(models.Model):
    # name	CharField	max_length=200	カテゴリ名を文字列で定義する最大文字列長は200
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

# Create your models here.
class Product(models.Model):
    #  CharField型：文字列フィールドを表し、最大長を指定することができます
    #  商品名は文字列なのでCharFieldとして、200文字までの制限を付けています。
    name = models.CharField(max_length=200)
    #  金額はマイナスの値がないため、PositiveIntegerFieldとしています
    price = models.PositiveIntegerField()
    #  BooleanField型：ブール値を表し、TrueまたはFalseを保持することができます
    #  DateTimeField型：日付と時刻を表し、年月日時分秒が格納されます
    #  IntegerField型：整数を表し、範囲内のあらゆる数値を格納できます
     
    #  「1：多」のリレーションを追加するには、「多」のModelにForeignKeyフィールドを設定します。この場合は、Productクラスに設定します。
    #  ForeignKeyは「多：1」のリレーションで、「多」側のモデルで使用されます。
    #  ForeignKeyフィールドを使用すると、あるモデルが別のモデルの主キーを参照できます。つまり、親モデルから子モデルに対する参照が作られます。
    #  on_deleteは紐づいているデータが削除された場合の振る舞いを指定します。Categoryが削除された場合、Categoryに紐づいているProductをどうするかを指定するという意味です。
    #  フィールド名 = models.ForeignKey(Modelクラス, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
        # CASCADE	データが削除されると、関連するすべてのデータが削除される
        # PROTECT	関連するデータがあると削除できない
        # SET_NULL	データが削除されると、関連するすべてのデータがNULLに設定される
        # SET_DEFAULT	データが削除されると、関連するすべてのデータがデフォルト値に設定される
        # SET()	データが削除されると、関連するすべてのデータが指定値に設定される
        # DO_NOTHING	データが削除されても、関連するデータに対して何も行われない

    # 商品Modelに画像フィールドを追加します。
        # ImageFieldは、画像ファイルをアップロードするためのフィールドです。
        # このフィールドでは、ファイルアップロードを処理する際に必要な機能が組み込まれており、簡単に画像アップロード機能を実装することができます。
        # アップロードされた画像ファイルはDjangoのメディアフォルダ内に保存され、そのパスがデータベースに保存されます。
            # blankはフォームに必須項目でないことを示す。Trueの場合、必須入力とはなりません。Falseの場合、必須入力となります。デフォルト値はFalseです。
            # default='noImage.png'	は省略時はデフォルト画像として、noImage.pngが使用される
    img = models.ImageField(blank=True, default='noImage.png')

    # 商品Modelに商品詳細の説明を追加するためのフィールドを追加します。
        #  複数行になることが予想されるため、TextField型で作成します。
        #  空（blank）やnullを許可するために、パラメータに「blank=True, null=True」を追加
    explanation = models.TextField(blank=True, null=True)
     
# マイグレーションとは、Modelに加えた修正をデータベースに反映することです。 
# マイグレーションファイルとは、マイグレーションコマンドを実行するのに必要なファイルです。
     
    #  Model内に「str(self)」を定義すると、一覧画面で表示される名称を変更できます。
    def __str__(self):
        return self.name
     
    #  新規作成画面で「登録」ボタンをクリックした際に、どの画面に遷移するのかをModelに指定します。
    #  ここでは、新規作成後に一覧画面へ遷移するように指定します。
     # 新規作成・編集完了時のリダイレクト先
    #  get_absolute_url関数を定義し、reverse関数の引数に「list」を指定することで、新規作成後に一覧画面へ遷移します。
    def get_absolute_url(self):
        #  reverse：名前からURLを取得する
        #  reverse関数は、URLパターンの名前を使って、任意のViewに関連付けられたURLを逆引きするための関数です。
        #  「逆引き」なのでreverseという関数名になっています。
        return reverse('list')
