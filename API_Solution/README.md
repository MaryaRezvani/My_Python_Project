## Currency Converter API Call Implementation
## Currency Convertor Streamlit UI

### Steps to Run the Streamlit App:
- Save the Code: Save the above code in a file named `app.py`.
- Install Streamlit: If you haven't installed Streamlit yet, install it using pip:
  ```bash
  pip install streamlit
  ‍‍‍‍```
- Run the App: In your terminal or command prompt, navigate to the directory where `app.py` is saved and run:
  ```bash
  streamlit run app.py
  ```
- Open Browser: Open the provided URL (e.g., `http://localhost:8501`) in your web browser to view the application.

### Implementing Cache with TTL
Sometimes, you may want cached results to expire after a certain period. this is not directly supported by `@cache` or `@lru_cache`, but you can third_party libraries or implement your own TTL cache.

### Using cachetools for TTL
The `cachetools` library provides a varietty of cache implements, including TTLCache, which supports time-to-live functionality.
```bash
pip install cachetools
```
![image](https://github.com/user-attachments/assets/01565dd0-d87b-468e-bbc6-6fb77a3275da)

