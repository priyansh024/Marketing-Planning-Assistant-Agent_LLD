# -------- Stage 1: Builder --------
FROM python:3.11-slim AS builder

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential

# Copy requirements
COPY requirements.txt .

# Install dependencies globally (IMPORTANT CHANGE)
RUN pip install --no-cache-dir -r requirements.txt


# -------- Stage 2: Runtime --------
FROM python:3.11-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local /usr/local

# Copy project files
COPY . .

# Create non-root user
RUN useradd -m appuser
USER appuser

# Expose port
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]