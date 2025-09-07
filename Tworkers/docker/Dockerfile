# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make the setup script executable (optional, if needed inside the container)
RUN chmod +x setup.sh

# Expose any ports if the agent runs a web service (optional)
# EXPOSE 8080

# Define the entrypoint for the container
# This will run the agent when the container starts
ENTRYPOINT ["python", "agent/agent.py"]

# Default command can be overridden at runtime
# For example, `docker run tworkers "create a script"`
CMD ["--help"]
