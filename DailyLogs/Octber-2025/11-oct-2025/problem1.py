def log_event(*args, **kwargs):
    # Join all positional messages
    message = " | ".join(str(arg) for arg in args)

    # Format keyword metadata
    metadata = ", ".join(f"{key}={value}" for key, value in kwargs.items())

    # Final log line
    print(f"[LOG] {message} [{metadata}]")

# Example usage
log_event("Service started", "Container: nginx", timestamp="2025-10-11 22:47", level="INFO", source="DockerMonitor")