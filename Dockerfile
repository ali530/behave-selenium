FROM python:3.10-slim

# Install Chromium + dependencies
RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium \
    xvfb \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Setup environment for headed execution
ENV DISPLAY=:99

# Set working directory
WORKDIR /app
COPY . /app
RUN mkdir -p /app/reports

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run Behave with xvfb and generate JSON 
CMD xvfb-run -a behave -f json.pretty -o reports/report.json -f pretty