USER=mamad
UID=1000
GID=1000

echo $USER
# echo $UID
# echo $GID

cd DockerFile

sudo docker build  --network=host --build-arg UNAME=$USER --build-arg UID=$UID  -t ubuntu23_10:ProceduralMeshGeneration  .





