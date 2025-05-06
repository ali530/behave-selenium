# SDAIA Automation Project (Ali Hummadi)

This is a test automation project covering:
- API testing (Valid login, Invalid login, and protected resource access)
- UI testing (search functionality on SDAIA website using differnt scenarious for valid, invalid, and edge-cases search)

Using:
- Python + Behave (BDD)
- Selenium 
- Xvfb for headless browser testing (to run on Kubernetes)
- Docker + Kubernetes CronJob to run the tests on a schedule

---

##  Pre-requisites

Make sure the following tools are installed:

- Docker Desktop (with WSL2 enabled)
- Minikube (with Docker driver)
- kubectl
- Python 3.10+ 
- Google Chrome + chromedriver (if running UI tests locally)

---



## Running the Project

### 🔹 Option 1: Run Locally (Python)

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up `.env` variables if needed

3. Run all tests:
```bash
behave -f json.pretty -o reports/report.json -f pretty
```

4. Run specific tests:
```bash
behave --tags=@api      # API only
behave --tags=@ui       # UI only
```

---

### 🔹 Option 2: Run on Kubernetes (Minikube)

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

5. Check the Jobs:
```bash
kubectl get cronjob
```

6. Check the pods:
```bash
kubectl get pod
```

7. Check the logs:
```bash
kubectl logs <pod-name>
```

8. Copy the test report from Minikube:
```bash
minikube cp minikube:/tmp/reports/report.json ./reports/report.json
```

---

##  Notes

- Feature files cover both API and UI scenarios.
- Logging is implemented to track test steps and results.
- The Dockerfile and cronjob.yaml are ready and tested.
- Report is saved as JSON.
