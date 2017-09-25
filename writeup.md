# Drone Project Thesis
_Author: Daniel Cheng_<br>
_Date: 9/2 to 9/17_

[//]: # (better name based off of thesis?)

## Project Brainstorming

## Initial Timeline / Sprint Plan
initial take photo and save to site

## Existing App Evaluation / Magic Quadrant
__Objective__: Find existing software / apps with the following capabilities:
1. Automate flying missions
2. Cache photos
3. Enable triggering for FLY NOW feature
+image quality/focusing 
+image size, etc.
+posting to SFTP (move these to the SDK section?)

[//]: # (check spelling, cost, system availability)
### Dimensions:
* Logistics: Cost, system availability (= color)
* Target Audience (Enterprise vs Hobbyist)
* Similar to surveying/photogrammetry vs flying custom missions and active tracking for own

### Native DJI Go4 App

Features Supported
* Automatic caching of photos
* Good focus / image quality

missing Features
* __Mission  Automation__: 
### Hobbyist Apps for Recreation
These apps target single user consumer flying drones primarily for personal recreation. 

Their interface is very similar to the native DJI Go4 App (in essence they've provided an extra UI layer for further customization off of the DJI SDK). 
purely for recreation. They enhance the automation section (what's that called??) in the app (such as Follow Me, Active Track, Waypoint Missions, Orbit, and Panorama). For example, for the waypoint missions, these apps allow you to mark destinations on a map, then convert these into a drone mission--unlike the DJI Go4 App which requires you to fly the drone through all these destinations before rerunning.

In increasing order of both cost and customizability:
1. Airnest 
2. DJI Ultimate Flight
3. Litchi
4. Autopilot

__Airnest__<br>
Airnest markets themselves as "simply and easy to use" with a "Photostop style" interface. For example, for waypoint missions, the app allows users to simply "paint a line" on a map, and the app converts that into mission instructions for the drone.

In my user tests, the app unfortunately failed to live up to its promise of being extraordinarily simple and easy to use. Missions could indeed be drawn with the flick of a finger, but editing those missions proved nearly impossible. For example, when I attempted to move the auto generated waypoint, I could literally find only one exact pixel spot where the app would respond to my touch.

However, Airnest is free to use and functions as a convenient starter entry app for those wishing for a more flexible mission automation tool.

__DJI Ultimate Flight and Litchi__<br>
These next two apps offer very similar features, with DJI Ultimate Flight coming in at $20, and Litchi at $20-25 depending on the system. Litchi is by far the most popular hobbyist drone app when browsing forums and drone enthusiast sites, and for good reason. 

Litchi allows users to create far more customized automated missions than would be possible in the native DJI app. This includes:
* Taking pictures (single shot and timed shot) at a waypoint
* Recording video at a waypoint
* Rotating the gimbal to focus on a point of interest 
* Pausing and hovering at a waypoint

All of these actions are programmatically tied to a waypoint, and a series of waypoints are then joined to together to run as an automated mission. Users simply tap to create a waypoint, then tap again to toggle the various actions for each waypoint. The series of waypoints are then uploaded as a missiont to the drone. All that's left is to hit "Run Mission" and the app will fly the drone from start to finish!
 
Both apps have very similar layouts to the DJI Go4 App, with a first-person video stream in front, camera options on the side, and toggling options for camera settings, waypoint behavior, etc.

A couple differentiating features between the two:
Additional features
* Litchi Mission Planning hub
* DJI panoramas and orbits during waypoint missions 

![Litchi landing screen](writeup_images/litchi_landingscreen.JPG)

__Autopilot__

[//]: # (include screenshot)

### Enterprise Apps for Surveyance
These apps diverge from the native DJI UI--while they do provide flight automation, the app itself is a tool, a means towards an end. 
That end is photogrammetry--generating a high-resolution or even 3D model via scores and hundreds of drone pictures. Hence enterprise is their target.
1. Flying Precision
2. Pix4D
3. Drone Deploy

### Logistics 
_Cost_

_System Availibility_


## SDK Exploration

## App Building

## App Troubleshooting

## Web Service

## Final Architecture

## Future Work

