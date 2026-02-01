def simulate_cli(*args, **kwargs):
    print("CLI Commands:")
    for i, cmd in enumerate(args, 1):
        print(f"  {i}. {cmd}")

    print("\nFlags:")
    for key, value in kwargs.items():
        print(f"  --{key}={value}")

# Example usage
simulate_cli("deploy", "restart", env="prod", force=True, dry_run=False)