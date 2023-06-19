# Dockerfile

# Use the official Python base image
FROM pytorch/pytorch:latest
ENV PYTHONUNBUFFERED 1
# Set the working directory in the container
WORKDIR /app
RUN pip install --upgrade pip
# Copy the requirements.txt file to the container
COPY requirements.txt requirements.txt

# Install the project dependencies
RUN pip install -r requirements.txt

# Copy the project code to the container
COPY . .

# Expose port
EXPOSE 8000
ENTRYPOINT ["/app/docker-entrypoint.sh"]