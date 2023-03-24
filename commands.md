/opt/bitnami/mariadb/data/

build

docker build -t us-central1-docker.pkg.dev/truckbase-348717/testapp/testapp:v1 .
docker run -p 8000:8000 us-central1-docker.pkg.dev/truckbase-348717/testapp/testapp:v1

Deploy New:

docker push us-central1-docker.pkg.dev/truckbase-348717/testapp/testapp:v1

kubectl create deployment testapp --image=us-central1-docker.pkg.dev/truckbase-348717/testapp/testapp:v1
kubectl scale deployment testapp --replicas=3
kubectl autoscale deployment testapp --cpu-percent=80 --min=1 --max=5

kubectl expose deployment testapp --name=testapp-service --type=LoadBalancer --port 80 --target-port 8080


Update version:
docker build -t us-central1-docker.pkg.dev/truckbase-348717/testapp/testapp:v2 .
docker push us-central1-docker.pkg.dev/truckbase-348717/testapp/testapp:v2
kubectl set image deployment/testapp testapp=us-central1-docker.pkg.dev/truckbase-348717/testapp/testapp:v2


gcp test:

docker build -t us-central1-docker.pkg.dev/truckbase-348717/testapp/gcptest:v1
docker run -p 8000:8000 us-central1-docker.pkg.dev/truckbase-348717/testapp/gcptest:v1

docker push us-central1-docker.pkg.dev/truckbase-348717/testapp/gcptest:v1

kubectl create deployment gcptest --image=us-central1-docker.pkg.dev/truckbase-348717/testapp/gcptest:v1
kubectl expose deployment gcptest --name=gcptest-service --type=LoadBalancer --port 80 --target-port 8000

kubectl get deployment
kubectl get services
kubectl get hpa
kubectl get pods
kubectl get replicasets
gcloud container node-pools list --zone=us-central1-c --cluster=mtestapp


Scaling:

kubectl scale deployment testapp --replicas=1
kubectl scale deployment gcptest --replicas=1
gcloud container clusters resize testapp --node-pool pool-1 --num-nodes=3 --zone=us-central1-c

kubectl autoscale deployment testapp --min=1 --max=5 --cpu-percent=70


gcloud container clusters delete testapp --zone us-central1-c


kubectl create secret generic db-user --from-literal=db-username='db-admin'


gcloud container node-pools create node-pool-1 --cluster=sample-cluster