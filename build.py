import os
import threading

threads = []

def build_application(app):
    threads.append(app)
    print(f"Building application {app}")
    os.system(f"cd {app} && mvn clean package")
    print(f"Application {app} finished building!")
    threads.remove(app)

def docker_compose_up():
    print("Running containers!")
    os.popen("docker-compose up --build -d").read()
    print("Pipeline finished!")

def build_all_applications():
    print("Starting to build applications!")
    applications = [
        "stateless/stateless-auth-api",
        "stateless/stateless-any-api",
        "stateful/stateful-auth-api",
        "stateful/stateful-any-api"
    ]
    for app in applications:
        thread = threading.Thread(target=build_application, args=(app,))
        thread.start()

def remove_remaining_containers():
    print("Removing all containers.")
    os.system("docker-compose down")
    containers = os.popen('docker ps -aq').read().strip().split('\n')
    if containers and containers[0]:
        print(f"There are still {len(containers)} containers created")
        for container in containers:
            print(f"Stopping container {container}")
            os.system(f"docker container stop {container}")
        os.system("docker container prune -f")

if __name__ == "__main__":
    print("Pipeline started!")
    build_all_applications()
    while threads:
        pass
    remove_remaining_containers()
    threading.Thread(target=docker_compose_up).start()