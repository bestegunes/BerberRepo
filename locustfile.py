from locust import HttpUser, task, between

# Tarayıcı gibi görünmesi için User-Agent header'ı ekliyoruz
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15"
}

class N11User(HttpUser):
    wait_time = between(1, 2.5)
    host = "https://www.n11.com" 

    @task
    def search(self):
        # Ana sayfa
        with self.client.get("/", name="Ana Sayfa", headers=HEADERS, catch_response=True) as response:
            print(f"Ana Sayfa status code: {response.status_code}")
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Ana sayfa yüklenemedi! Kod: {response.status_code}")

        # Telefon araması
        with self.client.get("/arama?q=telefon", name="Search telefon", headers=HEADERS, catch_response=True) as response:
            print(f"Telefon arama status code: {response.status_code}")
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Telefon araması başarısız! Kod: {response.status_code}")

    @task(2)
    def search_laptop(self):
        with self.client.get("/arama?q=laptop", name="Search laptop", headers=HEADERS, catch_response=True) as response:
            print(f"Laptop arama status code: {response.status_code}")
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Laptop araması başarısız! Kod: {response.status_code}")

    @task(1)
    def search_camera(self):
        with self.client.get("/arama?q=kamera", name="Search kamera", headers=HEADERS, catch_response=True) as response:
            print(f"Kamera arama status code: {response.status_code}")
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Kamera araması başarısız! Kod: {response.status_code}")
