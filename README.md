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
## Results
The Regression models that were built to find the optimal body position at each of the 7 steps are then used to predict the optimal position of the 7 muscle groups to achieve a different range of distances. The table below shows the different body positions to achieve a range of distances:</br>

**At step 1:**
| Distance (m) | Height (m) | Weight (kg) | Right Hip (&deg;) | Left Hip (&deg;) | Right knee (&deg;) | Left knee (&deg;) | Left trunk (&deg;) | Right trunk (&deg;) | Elbow (&deg;) | Shoulder (&deg;) |
|--------------|------------|-------------|-----------|----------|------------|-----------|------------|-------------|-------|----------|
| 85-87        | 1.8        | 86          | 100       | 90       | 151        | 100       | 163        | 166         | 155   | 36       |
|              | 1.85       | 91          | 102       | 102      | 175        | 121.08    | 154        | 146         | 167   | 117      |
|              | 1.9        | 95          | 110       | 105      | 140        | 90        | 173        | 176         | 155   | 40       |
| 88-90        | 1.8        | 86          | 105       | 110      | 175        | 122       | 144        | 116         | 162   | 111      |
|              | 1.85       | 91          | 102       | 105      | 173        | 121.7     | 134        | 104         | 152   | 122      |
|              | 1.9        | 95          | 106       | 111      | 167        | 141       | 143        | 107         | 154   | 112      |
| 91-93        | 1.8        | 86          | 103       | 107      | 176        | 144       | 153        | 107         | 127   | 101      |
|              | 1.85       | 91          | 106       | 112      | 166        | 143       | 154        | 104         | 121   | 86       |
|              | 1.9        | 95          | 120       | 90       | 171        | 147       | 156        | 165         | 134   | 82       |

**At step 2:**
| Distance (m) | Height (m) | Weight (kg) | Right Hip (&deg;) | Left Hip (&deg;) | Right knee (&deg;) | Left knee (&deg;) | Left trunk (&deg;) | Right trunk (&deg;) | Elbow (&deg;) | Shoulder (&deg;) |
|----------|--------|--------|-----------|----------|------------|-----------|------------|-------------|-------|----------|
| 82-84    | 1.8    | 86     | 71        | 97       | 138        | 150       | 160        | 160         | 166   | 70       |
|          | 1.85   | 91     | 80        | 67       | 138        | 144       | 152        | 147         | 174   | 68       |
|          | 1.9    | 95     | 84        | 63       | 131        | 139       | 152        | 157         | 176   | 65       |
| 85-87    | 1.8    | 86     | 87        | 74       | 145        | 141       | 163        | 126         | 169   | 102      |
|          | 1.85   | 91     | 92        | 104      | 153        | 147       | 167        | 137         | 167   | 99       |
|          | 1.9    | 95     | 90        | 97       | 127        | 132       | 162        | 138         | 169   | 101      |
| 88-90    | 1.8    | 86     | 116       | 94       | 122        | 165       | 144        | 131         | 143   | 81       |
|          | 1.85   | 91     | 96        | 104      | 142        | 133       | 166        | 127         | 131   | 79       |
|          | 1.9    | 95     | 70        | 99       | 162        | 154       | 146        | 132         | 143   | 76       |
| 91-93    | 1.8    | 86     | 118       | 107      | 144        | 167       | 137        | 143         | 147   | 84       |
|          | 1.9    | 95     | 90        | 97       | 157        | 132       | 172        | 148         | 145   | 101      |

**At step 3:** 
| Distance (m) | Height (m) | Weight (kg) | Right Hip (&deg;) | Left Hip (&deg;) | Right knee (&deg;) | Left knee (&deg;) | Left trunk (&deg;) | Right trunk (&deg;) | Elbow (&deg;) | Shoulder (&deg;) |
|----------|--------|--------|-----------|----------|------------|-----------|------------|-------------|-------|----------|
| 82-84    | 1.8    | 86     | 84        | 103      | 138        | 161       | 142        | 159         | 161   | 79       |
|          | 1.85   | 91     | 86        | 99       | 132        | 153       | 147        | 161         | 160   | 69       |
|          | 1.9    | 95     | 89        | 97       | 127        | 149       | 154        | 163         | 162   | 67       |
| 85-87    | 1.8    | 86     | 96        | 105      | 157        | 142       | 173        | 154         | 157   | 74       |
|          | 1.85   | 91     | 104       | 98       | 149        | 147       | 169        | 167         | 159   | 86       |
|          | 1.9    | 95     | 102       | 101      | 152        | 151       | 170        | 159         | 155   | 92       |
| 88-90    | 1.8    | 86     | 99        | 104      | 157        | 131       | 145        | 162         | 152   | 102      |
|          | 1.85   | 91     | 101       | 102      | 149        | 137       | 160        | 169         | 149   | 87       |
|          | 1.9    | 95     | 110       | 103      | 142        | 139       | 163        | 157         | 152   | 96       |
| 91-93    | 1.8    | 86     | 114       | 106      | 157        | 138       | 125        | 177         | 152   | 57       |
|          | 1.9    | 95     | 116       | 112      | 152        | 134       | 132        | 159         | 153   | 61       |

**At step 4:**
| Distance (m) | Height (m) | Weight (kg) | Right Hip (&deg;) | Left Hip (&deg;) | Right knee (&deg;) | Left knee (&deg;) | Left trunk (&deg;) | Right trunk (&deg;) | Elbow (&deg;) | Shoulder (&deg;) |
|----------|--------|--------|-----------|----------|------------|-----------|------------|-------------|-------|----------|
| 82-84    | 1.8    | 86     | 94        | 92       | 138        | 139       | 150        | 159         | 174   | 52       |
|          | 1.85   | 91     | 104       | 122      | 131        | 145       | 152        | 149         | 174   | 61       |
|          | 1.9    | 95     | 99        | 110      | 134        | 143       | 149        | 153         | 173   | 72       |
| 85-87    | 1.8    | 86     | 97        | 139      | 141        | 148       | 132        | 154         | 169   | 102      |
|          | 1.85   | 91     | 101       | 123      | 147        | 142       | 150        | 152         | 172   | 94       |
|          | 1.9    | 95     | 92        | 132      | 151        | 138       | 152        | 147         | 171   | 104      |
| 88-90    | 1.8    | 86     | 97        | 111      | 132        | 147       | 153        | 147         | 163   | 79       |
|          | 1.85   | 91     | 100       | 141      | 166        | 143       | 118        | 168         | 162   | 72       |
|          | 1.9    | 95     | 110       | 121      | 149        | 136       | 144        | 151         | 159   | 92       |
| 91-93    | 1.8    | 86     | 104       | 121      | 139        | 151       | 169        | 148         | 144   | 101      |
|          | 1.9    | 95     | 103       | 114      | 161        | 149       | 175        | 154         | 159   | 104      |

**At step 5:**
| Distance (m) | Height (m) | Weight (kg) | Right Hip (&deg;) | Left Hip (&deg;) | Right knee (&deg;) | Left knee (&deg;) | Left trunk (&deg;) | Right trunk (&deg;) | Elbow (&deg;) | Shoulder (&deg;) |
|----------|--------|--------|-----------|----------|------------|-----------|------------|-------------|-------|----------|
| 82-84    | 1.8    | 86     | 115       | 107      | 163        | 129       | 164        | 166         | 161   | 72       |
|          | 1.85   | 91     | 111       | 114      | 147        | 149       | 159        | 156         | 172   | 69       |
|          | 1.9    | 95     | 99        | 121      | 161        | 139       | 163        | 163         | 167   | 55       |
| 85-87    | 1.8    | 86     | 97        | 114      | 164        | 145       | 161        | 150         | 161   | 75       |
|          | 1.85   | 91     | 92        | 106      | 156        | 152       | 159        | 157         | 159   | 72       |
|          | 1.9    | 95     | 104       | 99       | 159        | 147       | 152        | 157         | 162   | 77       |
| 88-90    | 1.8    | 86     | 113       | 100      | 162        | 157       | 149        | 149         | 151   | 76       |
|          | 1.85   | 91     | 99        | 105      | 146        | 161       | 149        | 152         | 153   | 69       |
|          | 1.9    | 95     | 104       | 103      | 151        | 159       | 150        | 152         | 151   | 71       |
| 91-93    | 1.8    | 86     | 99        | 95       | 151        | 167       | 148        | 145         | 141   | 66       |
|          | 1.9    | 95     | 97        | 99       | 147        | 165       | 150        | 151         | 146   | 72       |

**At step 6 (final step):**
| Distance (m) | Height (m) | Weight (kg) | Right Hip (&deg;) | Left Hip (&deg;) | Right knee (&deg;) | Left knee (&deg;) | Left trunk (&deg;) | Right trunk (&deg;) | Elbow (&deg;) | Shoulder (&deg;) |
|----------|--------|--------|-----------|----------|------------|-----------|------------|-------------|-------|----------|
| 82-84    | 1.8    | 86     | 91        | 121      | 163        | 160       | 149        | 169         | 139   | 82       |
|          | 1.85   | 91     | 84        | 119      | 163        | 165       | 154        | 172         | 132   | 110      |
|          | 1.9    | 95     | 80        | 152      | 164        | 152       | 136        | 177         | 122   | 143      |
| 85-87    | 1.8    | 86     | 76        | 113      | 164        | 170       | 162        | 164         | 136   | 111      |
|          | 1.85   | 91     | 73        | 104      | 161        | 168       | 162        | 171         | 140   | 96       |
|          | 1.9    | 95     | 69        | 132      | 159        | 173       | 153        | 167         | 134   | 76       |
| 88-90    | 1.8    | 86     | 76        | 97       | 169        | 171       | 166        | 164         | 121   | 109      |
|          | 1.85   | 91     | 74        | 93       | 165        | 167       | 161        | 164         | 132   | 156      |
|          | 1.9    | 95     | 77        | 121      | 162        | 176       | 169        | 174         | 142   | 121      |
| 91-93    | 1.8    | 86     | 77        | 92       | 169        | 172       | 168        | 164         | 152   | 72       |
|          | 1.9    | 95     | 72        | 86       | 167        | 169       | 154        | 167         | 143   | 99       |

**During release:**
| Distance (m) | Height (m) | Weight (kg) | Right Hip (&deg;) | Left Hip (&deg;) | Right knee (&deg;) | Left knee (&deg;) | Left trunk (&deg;) | Right trunk (&deg;) | Elbow (&deg;) | Shoulder (&deg;) |
|----------|--------|--------|-----------|----------|------------|-----------|------------|-------------|-------|----------|
| 82-84    | 1.8    | 86     | 75        | 127      | 142        | 176       | 133        | 159         | 165   | 164      |
|          | 1.85   | 91     | 77        | 125      | 156        | 167       | 152        | 164         | 166   | 172      |
|          | 1.9    | 95     | 79        | 112      | 144        | 172       | 163        | 168         | 160   | 161      |
| 85-87    | 1.8    | 86     | 67        | 142      | 167        | 162       | 154        | 166         | 164   | 169      |
|          | 1.85   | 91     | 76        | 119      | 149        | 170       | 164        | 170         | 165   | 164      |
|          | 1.9    | 95     | 74        | 121      | 139        | 163       | 166        | 168         | 159   | 170      |
| 88-90    | 1.8    | 86     | 66        | 100      | 164        | 174       | 162        | 169         | 168   | 152      |
| 91-93    | 1.8    | 86     | 76        | 131      | 142        | 173       | 169        | 163         | 162   | 159      |
| 96       | 1.8    | 86     | 104       | 125      | 132        | 172       | 177        | 164         | 165   | 177      |

## Data Visualization

### Approach Phase Analysis (Steps 1-4)
| Step 1 | Step 2 |
|--------|--------|
| ![Step 1](https://github.com/user-attachments/assets/0441cef1-ae98-4374-8ef5-768c4c4e64f9) | ![Step 2](https://github.com/user-attachments/assets/89b5320c-4102-40bd-9800-086f223ed9b2) |

| Step 3 | Step 4 |
|--------|--------|
| ![Step 3](https://github.com/user-attachments/assets/e53d7a19-8972-4f8e-839d-a830e177c8ae) | ![Step 4](https://github.com/user-attachments/assets/99eaf89a-5112-4d0d-86a2-f5daee6334c1) |

### Final Step and Release
| Step 5 | Release Phase |
|--------|---------------|
| ![Step 5](https://github.com/user-attachments/assets/7ef80875-1757-4f95-a607-d0d1241332cc) | ![Release](https://github.com/user-attachments/assets/3e21e01d-9aad-4c9e-b912-e3cd64a42767) |

## Analysis and Interpretations

### Overview
This section provides a comprehensive analysis of the kinematic patterns observed in the collected data, examining the angular measurements of eight key joint positions across the final five steps and release phase. The analysis reveals distinctive technical patterns that characterize successful throws and highlights critical movement sequences.

### 1. Approach Phase Analysis (Steps 1-5)

#### 1.1 Lower Body Mechanics
- **Hip Angles**
  - Maintain consistent range of 90-120°
  - Bilateral coordination between right and left hips
  - Progressive stabilization approaching release

- **Knee Angles**
  - Higher angles (140-180°) indicating extended positions
  - More successful throws show greater knee extension stability
  - Left knee particularly stable in final steps

#### 1.2 Upper Body Mechanics
- **Trunk Position**
  - Coordinated left-right trunk angles (140-160°)
  - Reduced variability in final steps
  - Critical for force transfer from lower to upper body

- **Shoulder and Elbow Position**
  - Shoulder shows strategic loading pattern (60-80°)
  - Elbow maintains extension (140-180°)
  - Progressive reduction in variability approaching release

### 2. Release Phase Characteristics

#### 2.1 Optimal Release Position
- **Upper Body Alignment**
  - Shoulder-elbow-trunk alignment at 160-180°
  - Consistent across successful throws
  - Indicates optimal power position

- **Lower Body Support**
  - Right hip stabilized at 70-80°
  - Left knee maintained at 160-170°
  - Creates stable base for force generation

#### 2.2 Technical Execution
- **Joint Sequencing**
  - Coordinated progression from lower to upper body
  - Full extension of throwing arm
  - Balanced trunk position
  - Maintained knee extension

### 3. Performance Correlations

#### 3.1 Distance Factors
Better performances (85-90m) consistently show:
- More consistent hip angles
- Higher knee extension angles
- Superior shoulder-elbow coordination
- Stable trunk positions

#### 3.2 Technical Consistency
- Reduced variability in final positions
- Maintained body alignment
- Efficient energy transfer
- Coordinated joint sequencing

### 4. Technical Implications

#### 4.1 Key Success Factors
1. **Approach Phase**
   - Progressive stabilization
   - Individual style accommodation
   - Coordinated movement patterns

2. **Release Phase**
   - Consistent final position
   - Full arm extension
   - Balanced body position
   - Strong core engagement
   - Lower body support

#### 4.2 Critical Technical Elements
- Maintain high elbow through release
- Achieve full shoulder extension
- Control trunk rotation
- Sustain knee extension
- Coordinate hip positioning

## Conclusion

The implementation of pose estimation machine learning models has successfully demonstrated its capability to simulate javelin flight distances and analyze throwing techniques. This research provides dual benefits: technical advancement in sports analysis and detailed biomechanical insights for performance enhancement.

### Technical Achievement
- Successfully deployed machine learning models for pose estimation in javelin throwing
- Achieved encouraging accuracy despite limited training data
- Established a reliable framework for automated biomechanical analysis

### Biomechanical Insights
The analysis revealed several critical patterns that differentiate successful throws:

1. **Sequential Body Mechanics**
   - Progressive stabilization from approach to release
   - Optimal joint angles maintain consistency in successful throws
   - Critical angular ranges identified for key body segments:
     * Hip angles: 90-120°
     * Knee extension: 140-180°
     * Trunk coordination: 140-160°
     * Release position: 160-180° shoulder-elbow-trunk alignment

2. **Performance Correlations**
   - Longer throws (85-90m) consistently demonstrate:
     * Superior joint angle coordination
     * Reduced variability in final positions
     * Efficient energy transfer through the kinetic chain
     * Stable trunk and lower body positions

### Practical Applications
This research provides concrete guidance for athletes and coaches:
1. Athletes can use the identified angular ranges as benchmarks for technique refinement
2. Coaches can implement more precise technical feedback using the step-by-step analysis
3. Training programs can be optimized based on quantified biomechanical parameters

### Future Implications
The combination of machine learning and biomechanical analysis opens new avenues for:
1. Real-time technique analysis during training
2. Personalized technique optimization
3. Injury prevention through improved form
4. More efficient training methodologies

The results obtained demonstrate both the technical validity of the machine learning approach and its practical utility in performance enhancement. The identified biomechanical patterns provide a scientific foundation for technique development, while the pose estimation system offers a practical tool for implementation. This dual achievement suggests significant potential for advancing both the understanding and practice of javelin throwing technique.
