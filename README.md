# **Market APP**

**Daftar isi :**<br/>
[Tugas 2](#tugas-2)<br/>
[Tugas 3](#tugas-3)

**Muhammad Fauzan Jaisyurrahman**<br/>
**2206814040**<br/>
**PBP C**<br/>

Tautan untuk menuju aplikasi TukaTuku dapat diakses melalui [TukaTuku](https://tukatuku-web.adaptable.app/main/).

# **Tugas 2**
## **Langkah pengerjaan tugas 2 PBP**
1. Membuat direktori bernama `tukatuku` kemudian mengksesnya pada shell
2. Membuat *virtual environment* Python untuk mengisolasi proyek Python dengan menggunakan perintah `python -m venv env`.
3. Mengaktifkan *virtual environment* dengan perintah `env\Scripts\activate.bat` (Windows) *Virtual environment* akan aktif dan ditandai dengan `(env)` di baris input terminal.
4. Membuat file `requirements.txt` di dalam direktori proyek dan isi dengan daftar *dependencies* yang dibutuhkan untuk proyek. Contoh beberapa *dependencies* yang akan digunakan sebagai berikut.
```txt
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
5. Mengunduh semua *dependencies* pada `requirements.txt` dengan perintah `python -m pip install -r requirements.txt`.
6. Membuat proyek Django dengan nama `tukatuku_web` menggunakan perintah `django-admin startproject tukatuku_web .`.
7. Menambahkan `*` pada `ALLOWED_HOSTS` di dalam `settings.py` yang berada di dalam direktori `tukatuku_web` untuk mengizinkan akses dari semua host.
```python
...
ALLOWED_HOSTS = ["*"]
...
```
8. Kembali ke *command prompt* atau *terminal shell* dan jalankan server dengan perintah `python manage.py runserver` di dalam direktori proyek (pastikan ada file `manage.py` di sana). Lalu akses http://localhost:8000 di peramban web untuk melihat animasi roket yang menandakan bahwa aplikasi Django Anda telah berhasil dibuat.
9. Untuk menghentikan server, cukup dengan menekan tombol `Ctrl+C` di *command prompt* atau *terminal shell*. Pastikan juga untuk menonaktifkan *virtual environment* dengan menggunakan perintah `deactivate`.
10. Buat file `.gitignore` untuk menentukan berkas-berkas dan direktori-direktori yang harus diabaikan oleh Git. Isilah file tersebut dengan teks berikut.
```.gitignore
# Django
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# Backup files
*.bak 

# If you are using PyCharm
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# File-based project format
*.iws

# IntelliJ
out/

# JIRA plugin
atlassian-ide-plugin.xml

# Python
*.py[cod] 
*$py.class 

# Distribution / packaging 
.Python build/ 
develop-eggs/ 
dist/ 
downloads/ 
eggs/ 
.eggs/ 
lib/ 
lib64/ 
parts/ 
sdist/ 
var/ 
wheels/ 
*.egg-info/ 
.installed.cfg 
*.egg 
*.manifest 
*.spec 

# Installer logs 
pip-log.txt 
pip-delete-this-directory.txt 

# Unit test / coverage reports 
htmlcov/ 
.tox/ 
.coverage 
.coverage.* 
.cache 
.pytest_cache/ 
nosetests.xml 
coverage.xml 
*.cover 
.hypothesis/ 

# Jupyter Notebook 
.ipynb_checkpoints 

# pyenv 
.python-version 

# celery 
celerybeat-schedule.* 

# SageMath parsed files 
*.sage.py 

# Environments 
.env 
.venv 
env/ 
venv/ 
ENV/ 
env.bak/ 
venv.bak/ 

# mkdocs documentation 
/site 

# mypy 
.mypy_cache/ 

# Sublime Text
*.tmlanguage.cache 
*.tmPreferences.cache 
*.stTheme.cache 
*.sublime-workspace 
*.sublime-project 

# sftp configuration file 
sftp-config.json 

# Package control specific files Package 
Control.last-run 
Control.ca-list 
Control.ca-bundle 
Control.system-ca-bundle 
GitHub.sublime-settings 

# Visual Studio Code
.vscode/* 
!.vscode/settings.json 
!.vscode/tasks.json 
!.vscode/launch.json 
!.vscode/extensions.json
.history
```

## **Membuat aplikasi dengan nama `main` pada proyek**
1. Buka *command prompt* pada direktori utama dan aktifkan *virtual environment* dengan perintah `env\Scripts\activate.bat`.
2. Membuat aplikasi `main` dengan perintah `python manage.py startapp main`
3. Mendaftarkan aplikasi `main` ke proyek dengan menambahkan `'main'` pada `INSTALLED_APPS` di dalam file `settings.py`.
```python
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```
 
## **Membuat model pada aplikasi `main`**
1. Pada langkah ini, ubah file `models.py` yang terdapat di dalam direktori aplikasi `main` untuk mendefinisikan model baru dengan nama `MarketStock` dan memiliki atribut wajib sebagai berikut.
* `name` sebagai nama item dengan tipe `CharField`.
* `amount` sebagai jumlah item dengan tipe `IntegerField`.
* `description` sebagai deskripsi item dengan tipe `TextField`.<br/>
Kemudian menambahkan atribut `price` dan `category`.
2. Isi file `models.py` dengan kode berikut.
```python
from django.db import models

class MarketStock(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.BigIntegerField()
    category = models.CharField(max_length=255)
```
3. Jalankan perintah `python manage.py makemigrations` untuk membuat migrasi model lalu jalankan perintah `python manage.py migrate` untuk menerapkan migrasi ke dalam basis data lokal.

> [!IMPORTANT]
> Setiap kali melakukan perubahan pada model, seperti menambahkan atau mengubah atribut, perlu melakukan migrasi untuk merefleksikan perubahan tersebut.

## **Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML**
1. Buat direktori baru bernama `templates` di dalam direktori aplikasi `main` buat file `main.html` di dalamnya.
2. Buka file `views.py` pada direktori `main` dan tambahkan baris kode di paling atas `from django.shortcuts import render`. Ini akan mengimpor fungsi render dari modul django.shortcuts, yang akan digunakan untuk melakukan proses rendering tampilan HTML dengan menggunakan data yang diberikan.
3. Buat fungsi `show_stock` dengan parameter `request`. Di dalam fungsi ini, buatlah sebuah dictionary `context` yang berisi data yang akan dikirimkan ke tampilan. Setelah itu, gunakan fungsi `render` dengan tiga argumen, yaitu `request` (objek permintaan HTTP yang dikirim oleh pengguna), nama file HTML yang akan digunakan untuk me-render tampilan, dan `context` (dictionary yang berisi data untuk digunakan dalam tampilan yang dinamis). Setelah itu, kembalikan hasil rendering tersebut.
```python
from django.shortcuts import render

# Create your views here.

def show_stock(request):
    context = {
        'name': 'Buku Tulis SIDU',
        'amount': 20,
        'description' : 'Buku tulis sekolah merk SIDU',
        'price' : 5000,
        'category' : 'Book'
    }

    return render(request, "main.html", context)
```
4. Buka file `main.html` yang telah dibuat sebelumnya dan lakukan perubahan pada kode yang tadinya statis menjadi kode Django yang sesuai untuk menampilkan data. Gunakan sintaks Django `{{ }}` untuk memasukkan data dari `context` yang telah dikirimkan oleh fungsi `show_stocks`.

## **Membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`**
Jika belum ada, buat file `urls.py` di dalam direktori main. Konfigurasi routing URL aplikasi `main` dengan melakukan perubahan pada file `urls.py` yang berada dalam direktori `main`.
```python
from django.urls import path
from main.views import show_stock

app_name = 'main'

urlpatterns = [
    path('', show_stock, name='show_stock'),
]
```

## **Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`**
Untuk menjalankan aplikasi yang dibuat perlu dilakukan konfigurasi routing proyek. Tambahkan path yang mengarah ke aplikasi tersebut di dalam file `urls.py` yang berada di dalam direktori proyek.
```python
"""
URL configuration for inventory_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
]
```

## **Melakukan deployment ke Adaptable**
1. Login [Adaptable.io](https://adaptable.io/) dengan menggunakan akun GitHub yang digunakan untuk membuat proyek.
2. Jika sudah login, silakan tekan tombol `New App`. Pilih `Connect an Existing Repository`.
3. Hubungkan [Adaptable.io](https://adaptable.io/) dengan GitHub dan pilih `All Repositories` pada proses instalasi.
4. Pilihlah repositori proyek aplikasi yang telah diunggah ke GitHub serta branch untuk deployment.
5. Pilihlah `Python App Template` sebagai template deployment.
6. Pilih `PostgreSQL` sebagai tipe basis data yang akan digunakan.
7. Sesuaikan versi Python dengan spesifikasi aplikasimu. Untuk mengeceknya, nyalakan virtual environment dan jalankan perintah `python --version`.
8. Pada bagian `Start Command` masukkan perintah `python manage.py migrate && gunicorn (main directory).wsgi`.
9. Masukkan nama aplikasi yang juga akan menjadi nama domain situs web aplikasimu.
10. Centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai proses deployment aplikasi.

## **Bagan Client Request and Response - Django**
![alt-text](image/bagan.png)
User akan melakukan *request* HTTP aplikasi `main` dan diterima oleh *web browser*,lalu URL *mapping* dilakukan oleh `urls.py` untuk meneruskan *request* HTTP ke `views.py`. Kemudian *request* HTTP dikembalikan oleh view menjadi *response* yang berupa HTML *page. Pada proses pengembalian, view memproses data yang dibutuhkan via `models.py` dan *template* yang akan menampilkan data tersebut.

## **Penggunaan Virtual Environment**
Virtual environment digunakan untuk mengelola dependensi, menjaga kebersihan lingkungan pengembangan, dan menghindari konflik antara versi Python dan paket-paket Python yang berbeda. Ini menjadi praktik yang umum dalam pengembangan perangkat lunak Python yang bersih dan teratur. Pembuatan aplikasi web berbasis Django sangat memungkinkan. Namun, bisa saja dapat terjadi risiko konflik *dependencies* antar proyek yang menyebabkan proyek yang sedang dibangun menjadi runyam.

## **MVC, MVT, MVVM, serta perbedaan ketiganya**

MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah tiga pola desain (design patterns) yang umum digunakan dalam pengembangan perangkat lunak, terutama dalam pengembangan aplikasi berbasis web. Mereka membantu dalam mengatur dan memisahkan komponen-komponen aplikasi untuk meningkatkan keterbacaan, skalabilitas, dan pemeliharaan.

1.MVC (Model-View-Controller)

Controller : Perantara antara Model dan View. Controller menerima input dari pengguna melalui View, memprosesnya, berinteraksi dengan Model untuk mengambil atau memodifikasi data, dan kemudian memperbarui tampilan (View) sesuai dengan hasilnya 

2.MVT (Model-View-Template)

Template : Komponen unik dari MVT yang mengurus bagian presentasi tampilan, seperti HTML. Template berisi markup HTML dengan kode templat yang akan diisi dengan data dari Model

3.MVVM (Model-View-ViewModel)

ViewModel : Komponen unik dari MVVM yang berfungsi sebagai perantara antara Model dan View. ViewModel mengambil data dari Model dan memprosesnya menjadi bentuk yang dapat langsung ditampilkan oleh View. ViewModel juga berisi logika yang terkait dengan tampilan

Tabel perbedaan ketiga pola ini

| **MVC** | **MVT** | **MVVM** |
| --- | --- | --- |
| Input diterima langsung oleh Controller | Input diterima langsung oleh put diterima langsung oleh View | Input diterima langsung oleh put diterima langsung oleh View |
| View dan Controller memiliki relasi many-to-many | View dan Template memiliki relasi one-to-one | View dan ViewModel memiliki relasi one-to-many |
| View bertanggung jawab terhadap Model yang akan diteruskan | View tidak bertanggung jawab terhadap Model, Template yang akan memperbarui Model | View tidak bertanggung jawab terhadap Model, ViewModel yang akan memperbarui View |

# **Tugas 3**
## **Langkah pengerjaan tugas 3 PBP (Implementasi *Data Delivery*)**

### Membuat input `form`

1. Pertama, membuat berkas baru `forms.py` pada direktori `main` serta menambahkan kode berikut.

    ```python
    from django.forms import ModelForm
    from main.models import MarketStock

    class ProductForm(ModelForm):
        class Meta:
            model = MarketStock
            fields = ["name", "price", "description", "amount"]
    ```


2. Kedua, mengubah fungsi `show_stock` pada `views.py` dengan kode berikut.

    ```python
    def show_stock(request):
        products = MarketStock.objects.all()

        context = {
            'name' : 'Muhammad Fauzan Jaisyurrahman',
            'class' : 'PBP - C',
            'products' : products,
        }

        return render(request, "main.html", context)
    ```

### Menambahkan fungsi pada `views` dan membuat routing URL

Membuat fungsi untuk melihat atau mengembalikan data yang telah dimasukkan melalui `form`. Sebelum membuat fungsi baru pada views tambahkan beberapa *import* berikut.

```py
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import ProductForm
from django.urls import reverse
from main.models import MarketStock
from django.core import serializers
```

#### **Format HTML**

1. pertama,  buat fungsi baru bernama `create_product` dengan parameter `request` dan sertakan kode berikut.

    ```python
    def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_stock'))

    context = {'form': form}
    return render(request, "create_product.html", context)

    ```

2. Membuat berkas HTML baru (*template create product*) dengan nama `create_product.html` pada direktori `main/templates`.
    ```HTML
    {% extends 'base.html' %} 

    {% block content %}
    <h1>Add New Product</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Product"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```

3. Menampilkan barang-barang yang tersedia dalam bentuk tabel serta membuat tombol `Add New Product` pada `main.html`.

    ```HTML
    h2 class="section-title">Product List</h2>
        <table>
            <tr>
                <th>Name</th>
                <th>Price</th>
                <th>Description</th>
                <th>Category</th>
                <th>Amount</th>
            </tr>

            {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

            {% for product in products %}
                <tr>
                    <td>{{ product.name }}</td>
                    <td>{{ product.price }}</td>
                    <td>{{ product.description }}</td>
                    <td>{{ product.category }}</td>
                    <td>{{ product.amount }}</td>
                </tr>
            {% endfor %}
        </table>

        <div class="total-item">
            <p>You have {{ products|length }} items in your application</p>
        </div>

        <a href="{% url 'main:create_product' %}" class="add-product-btn">Add New Product</a>
    </div>
    ```

#### **Format XML**

Tambahkan fungsi `show_xml` dengan parameter `request` yang me-return `HttpResponse` berisi data yang sudah di-serialize menjadi XML.

```py
def show_xml(request):
    data = MarketStock.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

#### **Format JSON**

Tambahkan fungsi `show_json` dengan parameter `request` yang me-return `HttpResponse` berisi data yang sudah di-serialize menjadi JSON.

```py
def show_json(request):
    data = MarketStock.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

#### **Format XML *by* ID**

Tambahkan fungsi `show_xml_by_id` dengan parameter `request` yang me-return `HttpResponse` berisi data yang sudah di-serialize.

```py
def show_xml_by_id(request, id):
    data = MarketStock.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

#### **Format JSON *by* ID**

Tambahkan fungsi `show_json_by_id` dengan parameter `request` yang me-return `HttpResponse` berisi data yang sudah di-serialize.

```py
def show_json_by_id(request, id):
    data = MarketStock.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

Setelah pembuatan fungsi `show` selesai, buat routingnya dengan menambahkan path pada `urlpattern` di dalam berkas `urls.py`.

```py
from django.urls import path
from main.views import show_stock, create_product, show_xml, show_json, show_json_by_id, show_xml_by_id

app_name = 'main'

urlpatterns = [
    path('', show_stock, name='show_stock'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]
```

Input form sudah selesai dibuat dan siap digunakan. Jalankan command `python manage.py runserver` dan kunjungi http://localhost:8000 mencobanya.

## ***Screenshoot* Postman**

Berikut adalah *screenshoot* hasil mengakses kelima URL melalui Postman

1. HTML
    ![alt-text](image/html.png)
2. XML
    ![alt-text](image/xml.png)
3. JSON
    ![alt-text](image/json.png)
4. XML *by* ID
    ![alt-text](image/xmlbyid-6.png)
5. JSON *by* ID
    ![alt-text](image/jsonbyid-6.png)

## **Perbedaan antara form `POST` dan form `GET` dalam Django**

Di Django, `POST` dan `GET` adalah dua metode HTTP yang digunakan untuk mengirim data dari browser ke server. Kedua metode ini memiliki peran dan karakteristik yang berbeda.

| Perbedaan | `POST` | `GET` |
| -- | -- | -- |
| Penggunaan Utama | Digunakan untuk mengirim data ke server, terutama ketika ingin mengirim data yang bersifat sensitif dan mempengaruhi status server | Digunakan untuk mengambil data dari server, terutama ketika ingin mengambil data tanpa mempengaruhi status server |
| Pengiriman Data | Data yang dikirim tidak terlihat di URL | Data yang dikirm terlihat dalam URL |
| Keamanan | Lebih aman untuk mengirim data sensitif | Kurang aman untuk data sensitif |

## **Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data**

| Perbedaan | XML | JSON | HTML |
|--|--|--|--|
| Tujuan Utama | XML digunakan untuk pertukaran data antara berbagai sistem dan platform. XML sering digunakan dalam layanan web, konfigurasi file, dan pertukaran data yang kompleks | JSON digunakan untuk pertukaran data di antara aplikasi web dan server. Ini telah menjadi format yang sangat populer untuk API web RESTful karena kemudahan penggunaannya dan pembacaan manusia yang mudah | HTML digunakan untuk membuat tampilan dan struktur halaman web yang dapat ditampilkan oleh peramban web |

## **Alasan mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern**
Berikut adalah kelebihan penggunaan JSON dalam pertukaran data:
1. Ringkas dan Mudah Dibaca: JSON adalah format yang ringkas dan mudah dibaca oleh manusia. Strukturnya terdiri dari pasangan "kunci-nilai" yang membuatnya mudah dipahami dan diinterpretasi oleh pengembang. Karena kemudahan keterbacaannya, JSON membuat proses pengembangan dan debugging lebih mudah.

2. Struktur Data yang Fleksibel: JSON mendukung struktur data yang sangat fleksibel, termasuk larik, objek bersarang, dan tipe data primitif. Ini memungkinkan Anda untuk mewakili data dengan tingkat kompleksitas yang berbeda, sehingga sesuai untuk berbagai jenis aplikasi web.

3. Lintas Platform dan Browser: JSON dapat digunakan di berbagai platform dan didukung oleh sebagian besar peramban web modern. Ini memastikan bahwa data dalam format JSON dapat diakses oleh berbagai jenis perangkat dan sistem operasi.