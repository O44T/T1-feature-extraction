## dataset_05: derived features

**Video:** Exp_0295 

Total number of frames video: 13777 

The variables listed below are calculated using end and middle points. Then there are one set of file named *end* and other named *mid*, respectively.

Frames in *dataset_05_1*: 20 - 4000 // part1 = 20 - 2000 ; part2 = 2001 - 4000  
Frames in *dataset_05_2*: 4001 - 7000    
Frames in *dataset_05_3*: 7001 - 9000

**Total number of positive T1 events:** 10170

Given that there is no connection between variables, some variables hasn't been included in the current table. Curvature and orientation can be found in [data/dataset_03](https://github.com/O44T/T1-feature-extraction/tree/master/data/dataset_03 "Curvature") and [data/dataset_04](https://github.com/O44T/T1-feature-extraction/tree/master/data/dataset_04 "Orientation"). 

**Images:** Check folder [data/dataset_02](https://github.com/O44T/T1-feature-extraction/tree/master/data/dataset_02 "Images"). There are 9 parts: images.part%.rar. Frames 20 - 1993

### Column labels

**dataset_05** is a 34-column table containing information of those 4-fold nodes that appear in the foam flow. 
The columns are:
    
<table>
    <thead>
        <tr>
            <th>Frame Number</th>
            <th colspan=2>Vertex ; col = 2-3</th>
            <th colspan=1>&alpha; ; col = 4-7</th>
            <th colspan=1>Area ; col = 8</th>
            <th colspan=1>Side ; col = 9-12</th>
            <th colspan=1>Perimeter ; col = 13</th>
            <th colspan=1>&zeta; ; col = 14-17</th>
            <th colspan=1>Length ; col = 18-21</th>
            <th colspan=1>Angle ; col = 22-25</th>
            <th colspan=1>Arc Length ; col = 25-29</th>
            <th colspan=1>Area film ; col = 30-33</th>
            <th colspan=1>T1 ; col = 34</th>
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
            <th>&zeta;</th>
            <th>&ell;</th>
            <th>&theta;</th>
            <th>s</th>
            <th>a_f</th>
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

#### Lengths: chord &ell;, theta &theta; and arc length s

In this section, **Columns 18-29** are explained. **Columns 18-21** are the distance between the vertex and the end or middle points (it depends on the file name), as shown in figure named &ell;. If the film is curved, the length &ell; is equivalent to the circle chord. **Columns 22-25** are the angle &theta; defined in the Figure below. Finally, **columns 26-29** are the arc length **s** = R&theta;, length of the film. When the film is straight, the arc length is the chord, i.e. s = &ell;.

<img src = "https://github.com/O44T/T1-feature-extraction/blob/master/data/dataset_05/sketch/Fig_Length.png" width = "700" style="background-color:blue;" /> 

#### Area between film and chord

**Columns 30-33** are the area between the film and the circle chord &ell;, the green sector shown in the figure below. If the film is straight, the area is equal to zero. 

<img src = "https://github.com/O44T/T1-feature-extraction/blob/master/data/dataset_05/sketch/Fig_AreaFilm.png" width = "500">

#### T1 event 

The last column, **column 34**, in the table points out whether or not the 4-fold vertex is a T1 event. 

    T1 event yes = 1 | T1 event no = 0
