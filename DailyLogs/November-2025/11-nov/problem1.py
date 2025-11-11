# docker clearner script

import docker

def main():
    client = docker.from_env()
    print("starting docker cleanup...")

    #clean stopped containers
    stopped_containers = client.containers.list(all=True, filters={"status":"exited"})
    for cont in stopped_containers:
        print(f"Removing container: {cont.name}")
        cont.remove()


if __name__ == "__main__":
    main()