from locust import HttpUser, task, between
import random
import json

class PetStoreUser(HttpUser):
    wait_time = between(1, 2)
    host = "https://petstore.swagger.io/v2"
    pet_id = random.randint(100000, 999999)  # Her kullanıcı farklı ID kullanır

    # Create Pet (Positive)
    @task
    def create_pet(self):
        payload = {
            "id": self.pet_id,
            "name": "Fluffy",
            "photoUrls": ["string"],
            "status": "available"
        }
        with self.client.post("/pet", json=payload, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Create Pet failed! {response.status_code}")

    # Read Pet (Positive)
    @task
    def get_pet(self):
        with self.client.get(f"/pet/{self.pet_id}", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Get Pet failed! {response.status_code}")

    # Update Pet (Positive)
    @task
    def update_pet(self):
        payload = {
            "id": self.pet_id,
            "name": "FluffyUpdated",
            "photoUrls": ["string"],
            "status": "sold"
        }
        with self.client.put("/pet", json=payload, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Update Pet failed! {response.status_code}")

    # Delete Pet (Positive)
    @task
    def delete_pet(self):
        with self.client.delete(f"/pet/{self.pet_id}", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Delete Pet failed! {response.status_code}")

    # Get Pet (Negative) – Invalid ID
    @task
    def get_nonexistent_pet(self):
        invalid_id = -99999
        with self.client.get(f"/pet/{invalid_id}", catch_response=True) as response:
            if response.status_code == 404:
                response.success()
            else:
                response.failure(f"Expected 404, got {response.status_code}")

    # Delete Pet (Negative) – Invalid ID
    @task
    def delete_nonexistent_pet(self):
        invalid_id = -99999
        with self.client.delete(f"/pet/{invalid_id}", catch_response=True) as response:
            if response.status_code == 404:
                response.success()
            else:
                response.failure(f"Expected 404, got {response.status_code}")
