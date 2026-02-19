import psutil
import time
import firebase_admin
from firebase_admin import credentials, db

# Firebase yapılandırması
cred = credentials.Certificate("firebase-service-account.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'YOUR_DATABASE_URL'
})

# Firebase referansı
ref = db.reference('kazanc')

# İşlemci yükünü ölç
while True:
    cpu_percent = psutil.cpu_percent(interval=1)
    
    # Firebase'e gönder
    ref.set(cpu_percent)
    
    # 1 saniye bekle
    time.sleep(1)