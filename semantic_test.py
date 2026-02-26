import requests

def test_kubernetes_query():
    url = "http://127.0.0.1:8000/query"

    payload = {
        "q": "What is Kubernetes?"
    }

    response = requests.post(url, json=payload)

    if response.status_code != 200:
        raise Exception(f"Server returned {response.status_code}: {response.text}")

    answer = response.json()["answer"]

    assert "orchestration" in answer.lower(), "Missing 'orchestration' keyword"
    assert "container" in answer.lower(), "Missing 'container' keyword"

    print("✅ Kubernetes query test passed")

if __name__ == "__main__":
    test_kubernetes_query()
    print("All semantic tests passed!")