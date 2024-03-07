FROM python:3.8.12-slim

# Update package lists
RUN apt-get update && \
    apt-get install -y --no-install-recommends tk

# Set the working directory in the container
WORKDIR /app

# Copy your Python script(s) into the container
COPY . .

# Command to run the Tkinter application
CMD ["python3", "main.py"]
