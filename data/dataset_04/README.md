## dataset_04: points-on-film

**Video:** Exp_0295 

Total number of frames video: 13777 

Frames in *dataset_04_1*: 20 - 4000  
Frames in *dataset_04_2*: 4001 - 7000

**Images:** Check folder [data/dataset_02](https://github.com/O44T/T1-feature-extraction/tree/master/data/dataset_02 "Images"). There are 9 parts: images.part%.rar. Frames 20 - 1993

<img src = "https://github.com/O44T/T1-feature-extraction/blob/master/data/dataset_03/sketch/AllInfo.jpg" width = "400"><img src = "https://github.com/O44T/T1-feature-extraction/blob/master/data/dataset_03/sketch/VectorField.jpg" width = "400">

### Column labels

dataset_04 is a 21-column table containing information of those 4-fold nodes that appear in the foam flow. 
The columns are:
    
<table>
    <thead>
        <tr>
            <th>Frame Number</th>
            <th colspan=2>Vertex</th>
            <th colspan=4>Nodes; i = {1,4}</th>
            <th>Orientation</th>
            <th>T1 event</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>index</th>
            <th>x_c</th>
            <th>y_c</th>
            <th>x_{m,i}</th>
            <th>y_{m,i}</th>
            <th>x_{e,i}</th>
            <th>y_{e,i}</th>
            <th>&beta;</th>
            <th>yes or no</th>
        </tr>
    </tbody>
</table>

#### Nodes

For each film 
The 4-fold vertex is label as (x_c,y_c), columns 2 and 3. The codes detect those four films at the 4-fold node (see Fig. a). Then, there are two dots for each film, one at the middle (x_m,y_m) and the other at the end of the film (x_e,y_e) (see Fig. b). The groups of 4 values (x_m,y_m,x_e,y_e) are concatenated next to each other. As a result, columns from 3 to 19 are the nodes on the film. 

<img src = "https://github.com/O44T/T1-feature-extraction/blob/master/data/dataset_04/sketch/Dots.png" width = "700" style="background-color:blue;" /> 

#### Orientation

Using the four bubbles that close the central vertex, the eigenvectors are calculated to determine the major axis. The orientation is defined according to the direction of the major axis with respect to the [velocity field](https://github.com/O44T/T1-feature-extraction/blob/master/data/dataset_03/sketch/VectorField.jpg). The angle between those two vectors is <th>&beta;</th>.

<img src = "https://github.com/O44T/T1-feature-extraction/blob/master/data/dataset_03/sketch/Orientation_Sketch.png" width = "700">

#### T1 event 

The last column in the table points out whether or not the 4-fold vertex is a T1 event. 

    T1 event yes = 1 | T1 event no = 0
