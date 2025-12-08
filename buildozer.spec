[app]
title = MyApp
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 30
android.arch = armeabi-v7a
android.permissions = INTERNET
