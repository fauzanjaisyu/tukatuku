# **Market APP**

**Tugas 2 - Mata Kuliah PBP**

**Muhammad Fauzan Jaisyurrahman**<br/>
**2206814040**<br/>
**PBP C**<br/>

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
