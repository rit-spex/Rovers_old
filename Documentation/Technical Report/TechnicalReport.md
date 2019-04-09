# RIT Space Exploration Rovers Technical Report

<center>

![logo](Figures/SPEX_Logo.png)

</center>

# Rover Design

## Mechanical Systems

### Rocker-Bogie Suspension

The rocker bogie suspension system is NASA's preferred suspension system for martian 
rovers. The rocker bogie system reduces the motion of the main vehicle 
body by half compared to other suspension systems. Each of the 
rover's six wheels has an independent motor. The two front and two rear 
wheels have individual steering motors which allow the vehicle to turn in 
place. Each wheel also has cleats, providing grip for climbing in soft 
sand and scrambling over rocks. The maximum speed of the robots operated 
in this way is limited to eliminate as many dynamic effects as possible 
so that the motors can be geared down, thus enabling each wheel to 
individually lift a large portion of the entire vehicle's mass.

The term "bogie" comes from old railroad systems. A bogie is a train undercarriage with wheels that can swivel 
to curve along a track. The term "rocker" comes from the design of the differential, which keeps the rover body 
balanced, enabling it to "rock" up or down depending on the various positions of the multiple wheels. 

#### Materials Choice

To build much of the suspension and cradle PVC was chosen as the primary material. 
PVC pipes have been in use for over 60 years. When compared with traditional pipe materials, 
PVC offers valuable energy savings during production, low cost distribution and a safe, 
maintenance-free lifetime of service. PVC pipes will not degrade to damage the environment and 
suffer fewer breaks / leaks than other alternatives.

PVC is also very easy to work with. The pipes are rigid and easy to cut. Plenty of fittings 
and adapters are available in every hardware store in America. It is also quite inexpensive 
when compared to other materials we looked at including machined aluminum and PLA 
(Polylactic Acid) 3D prints. While these were still used in some places the majority of 
construction was done in PVC. PVC also comes together quite quickly. While 3D printing and 
machining aluminum or other metals allows more freedom, most of what we needed were the pipes 
as created by the PVC.

### Differential Design

What prevents the rover body from tipping all the way forward or backward 
around the rocker pivots? If you build a model rover and you attach the 
rockers to the body with an axle or two pivot pins, the body will tip 
forward or backward until it hits the ground! In the real rovers the two 
rockers connect to each other and to the body through a mechanism called a 
differential. The differential is what keeps the body level. Relative to the
body, when one rocker goes up, the other rocker goes down. Relative to the 
ground, the body angle is halfway between the angles of the two rockers. 
There are a couple of ways to make this work, a differential gearbox or a 
differential bar. Our team chose the differential bar to keep space free 
in the rover body as well as closer mimic MSL.

The middle of the bar is connected to the body with a pivot and the two ends
are connected to the two rockers through some short links. If you hold the
model rover body steady in midair and tilt one rocker up, one end of the
bar will go back, the other end will go forward, and the other rocker
will tilt down (see the animations below).

The Mars Exploration Rovers did not use a differential bar because it would 
interfere with the solar panels. But the Mars Science Laboratory does not 
have that problem because it is nuclear powered and has no solar panels. 
The SPEX rover does not have solar pannels either so this was not a concern 
for us.

### Body Design

Like a car body, the rover body is a strong, outer layer that protects the rover's computer and electronics 
(which are basically the equivalent of the rover's brains and heart). 
The rover body thus keeps the rover's vital organs protected and temperature-controlled. 
It's important that the electronics not get too hot or too cold in the rover body. 
In our case, we are more worried about them getting too hot. The sides of the body are designed to be 
breathable and there is a fan pulling air into the rover to keep them cool. For a real mission,
 (such as to the moon or mars) these temperatures could be much more extreme.

#### Materials Choice

The rover body which houses most of the electronics of the rover was made from ABS 
(Acrylonitrile butadiene styren) sheets. ABS is a common thermoplastic polymer typically 
used for injection molding applications. This engineering plastic is popular due to its low 
production cost and the ease with which the material is machined by plastic manufacturers. 
Better yet, its natural benefits of affordability and machinability do not hinder the ABS 
material’s desired properties:  

- Impact Resistance
- Structural Strength and Stiffness
- Chemical Resistance
- Excellent High and Low Temperature Performance
- Great Electrical Insulation Properties
- Easy to Paint and Glue

These sheets were cut down to size and then holes and ventilation were drilled out when 
necessary. 

#### Air flow

TODO

- Dust from bottom
- Left to right flow with push / pull fans was chosen

#### Upward mobility

TODO 

- Space was left open as there might be other parts added in the future

## Electrcal Systems

### Part Selection

Why motors, raspi pwn hat etc...

### Power Delivery

The Rocker-Bogie suspension design requires individually powered wheels. To power these motors, the Raspberry Pi, and the various other control elements, a 14.8V Lithium-Polymer battery is used. From the battery, the power system is split into two sections—a 12V section powering the motors, and a 5V section powering the Pi and other control elements. This is done with two seperate buck transformers, lowering the voltages to the required levels. Each motor is operated by a motor controller, and the motors are fused in pairs. The entire system is fused by way of the main power switch, which contains a 60A resettable fuse. 

### Motor Control

To control the rover, a Raspberry Pi running Raspbian is used as a central processor, with a codebase written in Python. A separate PWM driver is used to allow the Pi to output the six individual PWM signals necessary to control the motors.

## Software Stack

TODO

# Testing
