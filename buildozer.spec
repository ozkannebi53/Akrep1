[app]
title = Akrep1
package.name = akrep1
package.domain = org.ozkan

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Sadece gerekli olanlar, sürüm sabitleyici ile
requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
