# Kubernetes Events Reader App

## Overview
This application reads all events from a Kubernetes cluster and exposes them to stdout.

## Deployment Steps

1. Build the Docker image:

2. Apply the Kubernetes configurations:

3. Deploy the application to Kubernetes:
Create a deployment file or use a tool like Helm to deploy the application with the created image, ensuring it uses the `event-reader` ServiceAccount.

## Accessing Logs
- Use logging tools like Loki and Grafana to read and visualize logs.
- Ensure your logging system is set up to capture stdout from Kubernetes pods.
