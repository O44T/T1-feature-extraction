# Curved lines

This page contains how to draw curved lines

## How  the script works

the script is modified to draw curved lines where a T1 event occurs. The start, stop and step points must be adjusted in advance of running the script, for example there is a dataset file and the first frame name is im000301 and the last frame name is im000499 then the following order below must be followed,

- Start point = 301
- Stop point = 499
- Step point = 1

```
b = np.arange(start=301, stop=307, step=1, dtype=int)
```
## How to get the curved lines
```
 def getCurve(x0,y0,angle,curvature):
                    t = np.arange(35)
                    x = t
                    y = curvature * t*t
                
                    x_new = x*math.cos(angle*np.pi/180) - y*math.sin(angle*np.pi/180) + x0
                    y_new = x*math.sin (angle*np.pi/180) + y*math.cos (angle*np.pi/180) + y0
                
                    plt.plot(x_new, y_new, 'r', linewidth = 6)
 ```
 in the above script x0 and y0 are the coordinate of the t1 event occurs, the angle between curved lines and x axis is defined as angle.
 for the next step the created curved lines plotted on the top of the images.
 
 ## What the script requires 
 
 Firstly the script has been  executed according to below data text file order,

- 3.0500000e+02 5.6000000e+01 4.9100000e+02 -78 -10 -255 -192 -0.0045 -0.0005 0.0012 0.0012
- 3.0600000e+02 5.6000000e+01 4.9100000e+02 -78 -10 -255 -192 -0.0045 -0.0005 0.0012 0.0012
- 3.0600000e+02 4.5800000e+02 5.8900000e+02 -127 -65 -303 -240 0.0012 0.0012 -0.0045 0.0015

Columns order is like that; Frame nanme, x0, y0, angle1, angle2, angle3, angle4, curvature1, curvature2, curvature3, curvature4

for the healtier results Frame name, x0, y0, angle between curved lines and x axis and the curvature of each lines are needed.











<img src="https://user-images.githubusercontent.com/63856517/82141615-be392880-983f-11ea-8e3e-98d819d0fa5d.jpg" width="300" height="300" /> <img src="https://user-images.githubusercontent.com/63856517/82141738-81216600-9840-11ea-91ba-793864becb77.jpg" width="300" height="300" /> <img src="https://user-images.githubusercontent.com/63856517/82141796-e07f7600-9840-11ea-8fca-45fb8d519c20.PNG" width="100" height="100" />
