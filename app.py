from kubernetes import client, config, watch
from datetime import datetime


def main():
    try:
        print("Starting event watcher...")
        config.load_incluster_config()
        v1 = client.CoreV1Api()
        w = watch.Watch()

        for event in w.stream(v1.list_event_for_all_namespaces):
            timestamp = event['object'].last_timestamp
            if timestamp:
                timestamp = timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
            else:
                timestamp = "N/A"

            message = event['object'].message
            reason = event['object'].reason
            namespace = event['object'].metadata.namespace
            name = event['object'].metadata.name
            type = event['type']

            log_message = f"Timestamp: {timestamp}, Type: {type}, Namespace: {namespace}, Name: {name}, Reason: {reason}, Message: {message}"
            print(log_message)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
