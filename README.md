# viteyss-site-3dWannd

3d Wannd is a 3d mesuring mouse to to be able to enter x,y,z as keybord.

#### for what it is

To trace dificult shaps / mesurmants. It use computer vision powertd by:
- opencv
- python
- viteyss-site-dziabong-harvester


#### setup

To set it up you need runing **viteyss-site-dziabong-harvester**

* Observator
    Camera / phone on trepod, not moving. Looking by front or back camera. It need to see **3dWannd**

* 3dWannd
    - phone with web browser on this site so `https://localhost:8081/yss/index.html#pageByName=3d%20Wannd`
    - select marker to show and show it on screen to `Observator`
    - position phone to `POI` clik button `set`

* Drawing device
    - you run `python3 ./bin/main.py`
    - this will connect to 
        `Observator` to get location of the Wannd
        and `3dWannd` to get moment of confirmation of location
    - this will emit specific macro 
        `blender make point at`
        in `edit mode`
        it will press
        shift + a
        plain
        g
        x tab y tab z enter
        


#### screenshot

This is a current status of site. Me as a ui eeehh.

![](./assets/TODO.png)

`version 250825`




#### it can

