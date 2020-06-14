## dataset_03: angle, curvature and orientation

**Video:** Exp_0295 

Total number of frames video: 13777 

Frames in *dataset_03*: 20 - 1993   
Frames in *dataset_03_1*: 20 - 4000

**Images:** Check folder [data/dataset_02](https://github.com/O44T/T1-feature-extraction/tree/master/data/dataset_02 "Images"). There are 9 parts: images.part%.rar. Frames 20 - 1993

<img src = "https://github.com/O44T/T1-feature-extraction/blob/master/data/dataset_03/sketch/AllInfo.jpg" width = "400"><img src = "https://github.com/O44T/T1-feature-extraction/blob/master/data/dataset_03/sketch/VectorField.jpg" width = "400">

### Column labels

dataset_03 is a 13-column table containing information of those 4-fold nodes that appear in the foam flow. 
The columns are:
    
<table>
    <thead>
        <tr>
            <th>Frame Number</th>
            <th colspan=2>Vertex</th>
            <th colspan=4>Film Angles</th>
            <th colspan=4>Film Curvature</th>
            <th>Orientation</th>
            <th>T1 event</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>index</th>
            <th>x_c</th>
            <th>y_c</th>
            <th>&alpha;_1</th>
            <th>&alpha;_2</th>
            <th>&alpha;_3</th>
            <th>&alpha;_4</th>
            <th>&kappa;_1</th>
            <th>&kappa;_2</th>
            <th>&kappa;_3</th>
            <th>&kappa;_4</th>
            <th>&beta;</th>
            <th>yes or no</th>
        </tr>
    </tbody>
</table>

#### Film angles and curvatures

Each 4-fold vertex is conected to four films. For each of those four films, their angles and curvatures were calculated. 
The angle is defined as the arctan between the central point and each of the four nodes (blue dots). The film curvature is determined as the osculating circle using the previous two points and the central point in the film.

<img src = "https://raw.githubusercontent.com/O44T/T1-feature-extraction/master/data/dataset_03/sketch/4FoldVertex.png" width = "200" style="background-color:blue;" />  <img src = "https://github.com/O44T/T1-feature-extraction/blob/master/data/dataset_03/sketch/FilmsCurvature.png" width = "200">

![Curvature Plot](https://github.com/O44T/T1-feature-extraction/blob/master/data/dataset_03/sketch/testAnimated.gif)

#### Orientation

Using the four bubbles that close the central vertex, the eigenvectors are calculated to determine the major axis. The orientation is defined according to the direction of the major axis with respect to the [velocity field](https://github.com/O44T/T1-feature-extraction/blob/master/data/dataset_03/sketch/VectorField.jpg). The angle between those two vectors is <th>&beta;</th>.

<img src = "https://github.com/O44T/T1-feature-extraction/blob/master/data/dataset_03/sketch/Orientation_Sketch.png" width = "700">

#### T1 event 

The last column in the table points out whether or not the 4-fold vertex is a T1 event. 

    T1 event yes = 1 | T1 event no = 0
