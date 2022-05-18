# Javelin-throw analysis
## Uncovering the objective
The primary objective in the sport of javelin throw is to achieve the maximum distance of flight of javelin. This distance traveled by the javelin is dependent mainly on the angle of release of the javelin and the approach run to gain velocity. </br></br>
The javelin throw is different from all other overhead throws as it is more of an over-arm whip and flip motion that uses the efforts of the entire body. Terms such as fling, flip, the whip are much more descriptive and result in a more relaxed sequentially efficient delivery in which the arm of the athlete gets involved in the projection only after the major muscles of the legs, hips, and trunk have been utilized.</br></br>
The best javelin throw of all time was performed by Jan Zelezny, of the Czech Republic in 1966. The result was 98.48m. In the second place, comes Johannes Vetter of Germany in 2017, with a distance of 94.44m. In third place, comes Thomas Rohler, also from Germany, with a throw of 93.90m, in 2017.</br></br>
The flight distance of the javelin is determined by the release parameters such as the angle of release, the height of release, and velocity of release, as well as by the forces that act on the javelin during its flight. The former is under the control of the thrower, whereas the latter is not.</br></br>
The objective here is to find the optimal body posture of the athlete at each step during the approach phase for achieving maximum javelin flight. We make use of an open-source framework, called Mediapipe, introduced by Google to build a machine learning model that analyzes the body posture of the athlete at each step in the approach phase and the release phase.
## Methodology
The body posture of top javelin throw athletes was measured by building a machine learning model that estimates the body posture of an athlete in each frame of videos collected from the internet. These athletes include:</br>
- Neeraj Chopra</br>
- Johannes Vetter</br>
- Thomas Rohler</br>
- Andreas Hofmann</br>
- Magnus Kirt</br>


Since the information such as the number of steps taken in the approach phase varied from one video to another, all the videos are trimmed such that each of them consists of the last six steps, which is generally referred to as the crossover phase. After undergoing trimming, we remain with videos that have 90 frames each. According to studies conducted at Concordia University, NE, on analyzing the biomechanics behind javelin throw, seven main muscle groups play a major role in determining the velocity gained by the athlete in the approach phase. These muscle groups are as follows:</br>
- Gastrocnemius muscle</br>
- Soleus muscle</br>
- Quadriceps</br>
- Hamstrings</br>
- Rectus Abdominis</br>
- Triceps</br>
- Rhomboids </br>


To measure the position of these muscle groups, we calculate 8 different angles from the mediapipe Pose framework. The landmarks of these angles are as shown in the image below:</br></br>
![Picture1](https://user-images.githubusercontent.com/84195790/168995043-7f9e17ca-6468-4880-85a9-38fd72919457.png)

The pose-estimation model is then implemented, which iterates through all the videos to calculate the eight different angles of each frame of the video, and these angles collected are stored in separate CSV(comma separated values) files. After this process, the angles obtained from each video are analyzed to find the position of the athlete when each of the 6 steps in the crossover phase is placed and the position of the athlete during the release phase. </br></br>
These angles at each step in the approach phase are stored in 7 separate CSV file which is used for further analysis. Each of the final CSV files that are used to derive the optimal position contains the following features: </br>
- Left hip angle
- Right hip angle
- Left knee angle
- Right knee angle
- Left trunk angle
- Right trunk angle
- Elbow angle
- Shoulder angle
- Height of athlete
- Weight of athlete
- Distance traveled by javelin

After this process, regression models were built for all the CSV files of the 7 steps to find the optimal body position to achieve a different range of distances. 
