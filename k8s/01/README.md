# Kubernetes Exercises:

These exercises can be done completely locally, be sure to brush your knowledge based on the subjects we discussed in class.


:fire: <u>Create a folder for each task</u> :fire:

## Task 1

Create a Deployment and Service.
* <u>Details</u>:
  * <u>Port</u>: 8080
  * <u>Image</u>: ubuntu
  * <u>Replicas</u>: 3
* After you deploy the files, the Ubuntu pods will enter 'Completed' status, in order to change that, you have to change the __command__ and __args__ for the ubuntu pods.
* Use the following command and args:
  * tail -f /dev/null
* Deploy the new Deployment and make sure the pod are __Running__.
---
## Task 2
:sunny: For this task, make sure your <u>LOCAL</u> cluster is created from the <u>k3d</u> solution, because it allows the usage of more than 1 node easily.

You can install K3D - [THIS LINK](https://k3d.io/v5.4.9/) 

You may use this command to create your cluster.
```
k3d cluster create dev --agents 3
```

* Add to the deployment from [Task 1](#task-1) - PodAffinity settings
  * Refer to this Document: [Link](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#an-example-of-a-pod-that-uses-pod-affinity)
  * Make sure you use only - "preferredDuringSchedulingIgnoredDuringExecution"
  * Note these are LABEL selectors, so you need to select correctly.
  * set the TopologyKey to - "kubernetes.io/hostname"

:green_circle: Verify by running the "describe" command on your replicas and make sure they are scheduled on different nodes.

---
## Task 3 

Add a configmap with a custom index.html to your Nginx.
  * Recreate your K3d Cluster so it can mount your Volumes
    * ```
        k3d cluster create NAME [flags]
        -v, --volume [SOURCE:]DEST[@NODEFILTER[;NODEFILTER...]]              Mount volumes into the nodes (Format: [SOURCE:]DEST[@NODEFILTER[;NODEFILTER...]]

        - Example: `k3d cluster create --agents 2 -v /my/pat:mypath@agent:0,1 -v /tmp/test:/tmp/other@server:0`
        ```
        
        
    <u>/tmp/test - is the path on your HOST (your laptop)</u>


  * Create a deployment object with 1 replica and Service Object.
    * Set image to Nginx
    * Set port to 80
  * Create a ConfigMap object with this [content](./content.txt)
  * Apply the provider Storage class
  ```
  kubectl apply -f sc.yaml
  ```
  * Create the PersistentVolume and PersistentVolumeClaim using the provided [helper_yaml](Volumes_example.yaml)
  * In your deployment - add the Volumes and VolumesMounts sections as specified in this [document](https://kubernetes.io/docs/concepts/storage/volumes/#hostpath-configuration-example)
  * your MountPath should be - "/usr/share/nginx/html/"
  * Use the 
  ```
  kubectl port-forward svc/[SERVICE_NAME] 8080:80
  ```
    * Open your browser http://localhost:8080 and verify it worked, you should see the text from the configmap.

## Task 4

Create a helm chart - ``` helm create [chart_name]```

:star: TIP: Create another chart, so it helps you reference the structure. 


Delete the following:
* Content of 'templates' folder [KEEP _HELPERS.TPL FILE!!!!]
* Delete 'Charts' folders
* Delete Values.yaml file.

Now you should have an empty 'templates' folders and you can begin.

* Create a values.yaml file
* Create in the 'Templates' folder - a configMap, Deployment and Service  objects.
* The Service should have:
  * Port 80 and Target port 80
  * Type ClusterIP
* The ConfigMap should have the following environment variables:
  * Student Name - Your Name
  * Class Number - 35670-10
* The deployment should have the following specs:
  * 1 Container with port 80
  * Environment Variables taken from the configMap
  * Image Nginx
  * Using Command and Args, make sure you print those environment variables

Install the Chart and if it's all successfull, the pod will enter Completed state and the logs will show the output of the environment variables.