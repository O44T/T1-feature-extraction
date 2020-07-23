## dataset_05: derived features

**Video:** Exp_0295 

Total number of frames video: 13777 

Frames in *dataset_05_1*: 20 - 4000  
Frames in *dataset_05_2*: 4001 - 7000    
Frames in *dataset_05_3*: 7001 - 9000

**Total number of positive T1 events:** 10170

**Images:** Check folder [data/dataset_02](https://github.com/O44T/T1-feature-extraction/tree/master/data/dataset_02 "Images"). There are 9 parts: images.part%.rar. Frames 20 - 1993

<img src = "https://github.com/O44T/T1-feature-extraction/blob/master/data/dataset_03/sketch/AllInfo.jpg" width = "400"><img src = "https://github.com/O44T/T1-feature-extraction/blob/master/data/dataset_03/sketch/VectorField.jpg" width = "400">

### Column labels

**dataset_05** is a 28-column table containing information of those 4-fold nodes that appear in the foam flow. 
The columns are:
    
<table>
    <thead>
        <tr>
            <th>Frame Number</th>
            <th colspan=2>Vertex ; col = 2-3</th>
            <th colspan=1>&alpha; ; i = {1,4} ; col = 4-7</th>
            <th colspan=1>Area ; col = 8</th>
            <th colspan=1>Side ; i = {1,4} ; col = 9-12</th>
            <th colspan=1>Perimeter ; col = 13</th>
            <th colspan=1>ArcLength; i = {1,4}</th>
            <th colspan=1>Area below film; i = {1,4}</th>
            <th colspan=1>; i = {1,4}</th>
            <th>Total area</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>index</th>
            <th>x_c</th>
            <th>y_c</th>
            <th>&alpha;_i</th>
            <th>A</th>
            <th>d_{e,i}</th>
            <th>P</th>
            <th>&beta;</th>
            <th>yes or no</th>
            <th>yes or no</th>
            <th>yes or no</th>
        </tr>
    </tbody>
</table>

#### Nodes and angles 

The 4-fold vertex is label as (x_c,y_c), **columns 2 and 3**. **Columns 4-7** are the angles of each film, positive 0<= &alpha; <360. Each angle appears on the table moving clockwise, as the figure shows. The angles are in **consecutive order**. The order of any derivated variable is the same: **clockwise**. 

<img src = "https://github.com/O44T/T1-feature-extraction/blob/master/data/dataset_05/sketch/Fig_AnglesOrder.png" width = "500" style="background-color:blue;" /> 

#### Polygon 

Figure shows the polygon for each 4-fold vertex and **columns 8-13** contain geometric information. **Column 8** is the polygon area, the transparent area in the figure below. **Columns 9-12** are the distance between two consequtive end points. In other words, they are the length of each side of the polygon. Finally, **column 13** is the perimeter of the polygon, i.e., P = d_{e,1} + d_{e,2} + d_{e,3} + d_{e,4}. 

<img src = "https://github.com/O44T/T1-feature-extraction/blob/master/data/dataset_05/sketch/Fig_Polygon.png" width = "500" style="background-color:blue;" /> 

#### Angles between films &zeta; 

Figure shows the definition of &zeta;, i.e. the angle between **two consequtive films**. **Columns 14-17** contain the four angles. It has been calculate using the dot product, but note that it is equal to &zeta;\_i = &alpha;\_{i+1} - &alpha;\_{i}. 

<img src = "https://github.com/O44T/T1-feature-extraction/blob/master/data/dataset_05/sketch/Fig_zeta.png" width = "500" style="background-color:blue;" /> 

#### Orientation

Using the four bubbles that close the central vertex, the eigenvectors are calculated to determine the major axis. The orientation is defined according to the direction of the major axis with respect to the [velocity field](https://github.com/O44T/T1-feature-extraction/blob/master/data/dataset_03/sketch/VectorField.jpg). The angle between those two vectors is <th>&beta;</th>.

<img src = "https://github.com/O44T/T1-feature-extraction/blob/master/data/dataset_03/sketch/Orientation_Sketch.png" width = "700">

#### T1 event 

The last column in the table points out whether or not the 4-fold vertex is a T1 event. 

    T1 event yes = 1 | T1 event no = 0
