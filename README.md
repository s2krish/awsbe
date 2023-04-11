# Notes

docker build -t us-central1-docker.pkg.dev/zippy-parity-381314/awsbe/awsbe:v1 .
docker push us-central1-docker.pkg.dev/zippy-parity-381314/awsbe/awsbe:v1

kubectl create deployment awsbe --image=us-central1-docker.pkg.dev/zippy-parity-381314/awsbe/awsbe:v1 --node-selector=highcpu

kubectl scale deployment awsbe --replicas=3
kubectl autoscale deployment awsbe2 --cpu-percent=80 --min=1 --max=5
kubectl expose deployment awsbe --name=awsbe-service --type=LoadBalancer --port 80 --target-port 8000


kubectl expose deployment awsbe2 --name=awsbe-service --type=LoadBalancer --port 80 --target-port 8000


Update:
kubectl set image deployment/awsbe awsbe=us-central1-docker.pkg.dev/zippy-parity-381314/awsbe/awsbe:v2

kubectl set image deployment/awsbe2 awsbe2=us-central1-docker.pkg.dev/zippy-parity-381314/awsbe/awsbe:v2

## apply secret
kubectl apply -f secret.yaml


## scaling

gcloud container clusters resize cluster-1 --node-pool highcpu --num-nodes=3 --zone=us-central1-c
gcloud contaienr cluster update cluster-1 --enable-autoscale --min-nodes=1 --max-nodes=10


# deploy redis-docker


docker build -t us-central1-docker.pkg.dev/zippy-parity-381314/envsubst/envsubst:v1 .
docker push us-central1-docker.pkg.dev/zippy-parity-381314/envsubst/envsubst:v1