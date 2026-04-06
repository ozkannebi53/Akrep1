[app]
# (str) Uygulama Başlığı
title = Akrep1

# (str) Paket İsmi
package.name = akrep1

# (str) Paket Domaini
package.domain = org.ozkan

# (str) Ana dosya (main.py zaten yüklü)
source.dir = .

# (list) Dahil edilecek uzantılar
source.include_exts = py,png,jpg,kv,atlas

# (str) Uygulama versiyonu
version = 1.0

# (list) Gereksinimler (Kivy şart)
requirements = python3,kivy

# (str) Ekran yönü (Dikey lüks görünüm için portrait)
orientation = portrait

# (bool) Tam ekran mı?
fullscreen = 0

# (list) İzinler (Şimdilik standart, gerekirse ekleriz)
android.permissions = INTERNET

# (int) Android API seviyesi
android.api = 33

# (int) Minimum Android sürümü
android.minapi = 21

# (str) Android mimarisi
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
# (int) Log seviyesi
log_level = 2

# (int) Uyarıları gösterme
warn_on_root = 1
