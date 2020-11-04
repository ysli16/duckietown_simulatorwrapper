## Preparation

0.Clone this repositary to your PC

1.Go to *simulator_help_files folder*. Edit file *docker-compose.yaml*. Change the 3 lines below **volumes** to 

`<path_to_repositary>/simulator_help_files/data:/data`

Replace *<path_to_repositary>* with the directory that you clone the repositary.

## Execution
### Build simulatorwrapper image

Run command

`dts devel build -f`

### Start related duckiebot containers

Run command `docker-compose up` from the directory where the file *docker-compose.yaml* resides.

### Start docker container

Run command

`dts devel run`

### Monitor and publish rostopic

Run command

`dts start_gui_tools fakebot`

or

`docker run -it --net host duckietown/dt-ros-commons:daffy-amd64 /bin/bash`

To monitor image publisher, run command `rqt_image_view` and select topic */fakebot/camera_node/image/compressed* .

To change wheel velocity, run command `rostopic pub /fakebot/wheels_driver_node/wheels_cmd /fakebot/kinematics_node 'auto','X','Y'`. Replace *X* and *Y* with desired velocity of left and right wheel, respectively. 
