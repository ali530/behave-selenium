# SDAIA Automation Project (Ali Hummadi)

This is a test automation project covering:
- API testing (Valid & Invalid login, protected resource access)
- UI testing (search functionality on SDAIA website using valid, invalid search in addetion to edge-cases)

Using:
- Python + Behave (BDD)
- Selenium + Xvfb for headless browser testing
- Docker + Kubernetes CronJob to run the tests on a schedule

## Pre-requisites

Make sure the following tools are installed:

- Docker Desktop
- Minikube (with Docker driver)
- kubectl
- Python 
- Google Chrome + chromedriver (if running UI tests locally)

## Running

1. Start Minikube:
```bash
minikube start --driver=docker
& minikube -p minikube docker-env | Invoke-Expression
```

2. Build the Docker image:
```bash
docker build -t behave-sdaia-test .
```

3. Apply the CronJob:
```bash
kubectl apply -f cronjob.yaml
```

4. Run a job manually (optional):
```bash
kubectl create job --from=cronjob/behave-automation-job manual-run
```

5. Check the logs:
```bash
kubectl logs <pod-name>
```

6. Copy the test report from Minikube:
```bash
minikube cp minikube:/tmp/reports/report.json ./reports/report.json
```

## Notes
- Feature files cover both API and UI scenarios.
- Logging is implemented to track test steps and results.
- The Dockerfile and cronjob.yaml are ready and tested.
- Report is saved as JSON report.