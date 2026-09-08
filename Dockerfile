FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p ~/.streamlit
RUN echo '[server]\nheadless = true\nport = 8501\nenableXsrfProtection = false\n' > ~/.streamlit/config.toml

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
