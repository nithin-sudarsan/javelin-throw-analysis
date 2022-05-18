import cv2 as cv 
import mediapipe as mp
import time
import numpy as np
import os
import pandas as pd


 
mpDraw=mp.solutions.drawing_utils
mpPose=mp.solutions.pose
pose=mpPose.Pose(model_complexity=1, static_image_mode=False,smooth_landmarks=False, min_tracking_confidence=0.8)



#================================================================================================


def calculateangle(a,b,c):
    a=np.array(a)
    b=np.array(b)
    c=np.array(c)
    
    radians=np.arctan2(c[1]-b[1], c[0]-b[0])-np.arctan2(a[1]-b[1], a[0]-b[0])
    angle=np.abs(radians*180/np.pi)

    if angle>180: 
        angle=360-angle
    return angle 




directory = 'C:\\Users\\nithi\\Documents\\NITK research\\Athletes\\Kirt'





right_knee_video_angle_list=dict()
right_hip_video_angle_list=dict()
left_hip_video_angle_list=dict()
left_knee_video_angle_list=dict()
left_elbow_video_angle_list=dict()
right_trunk_video_angle_list=dict()
left_trunk_video_angle_list=dict()
left_shoulder_video_angle_list=dict()



# iterate over files in that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):

        cap=cv.VideoCapture(f)
        prevtime=0
       

        right_knee_angle_list=[]
        right_hip_angle_list=[]
        left_hip_angle_list=[]
        left_knee_angle_list=[]
        left_elbow_angle_list=[]
        right_trunk_angle_list=[]
        left_trunk_angle_list=[]
        left_shoulder_angle_list=[]


        try:
            counter=0
            stage=None
            while(True):
                success, img=cap.read()
                imgRGB=cv.cvtColor(img, cv.COLOR_BGR2RGB)
                results=pose.process(imgRGB)
                

                try:
                    landmarks=results.pose_landmarks.landmark
                    
                    #===============================================================================================================

                    right_ankle=[landmarks[mpPose.PoseLandmark.RIGHT_ANKLE.value].x,landmarks[mpPose.PoseLandmark.RIGHT_ANKLE.value].y]
                    right_knee=[landmarks[mpPose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mpPose.PoseLandmark.RIGHT_KNEE.value].y]
                    right_hip=[landmarks[mpPose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mpPose.PoseLandmark.RIGHT_HIP.value].y]
                    left_hip=[landmarks[mpPose.PoseLandmark.LEFT_HIP.value].x,landmarks[mpPose.PoseLandmark.LEFT_HIP.value].y]
                    left_knee=[landmarks[mpPose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mpPose.PoseLandmark.LEFT_KNEE.value].y]
                    left_ankle=[landmarks[mpPose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mpPose.PoseLandmark.LEFT_ANKLE.value].y]
                    right_shoulder=[landmarks[mpPose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mpPose.PoseLandmark.RIGHT_SHOULDER.value].y]
                    left_shoulder=[landmarks[mpPose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mpPose.PoseLandmark.LEFT_SHOULDER.value].y]
                    left_elbow=[landmarks[mpPose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mpPose.PoseLandmark.LEFT_ELBOW.value].y]
                    left_wrist=[landmarks[mpPose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mpPose.PoseLandmark.LEFT_WRIST.value].y]



                    #CALCULATE ANGLES
                    right_knee_angle=calculateangle(right_ankle,right_knee,right_hip)
                    right_hip_angle=calculateangle(right_knee,right_hip,left_hip)
                    left_hip_angle=calculateangle(right_hip,left_hip,left_knee)
                    left_knee_angle=calculateangle(left_ankle,left_knee,left_hip)
                    left_elbow_angle=calculateangle(left_shoulder,left_elbow,left_wrist)
                    right_trunk_angle=calculateangle(right_shoulder,right_hip,right_knee)
                    left_trunk_angle=calculateangle(left_shoulder,left_hip,left_knee)
                    left_shoulder_angle=calculateangle(left_hip,left_shoulder,left_elbow)
                    

                    #VISUALIZE
                    # cv.putText(img, str(("elbow:",elbow_angle,"\nhip angle:", hip_angle)), (100,80), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,255), 2,cv.LINE_AA)
                    
                    
                    
                    

                except:
                    pass

                if results.pose_landmarks:
                    mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS, mpDraw.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), mpDraw.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2))

                

                right_knee_angle_list.append(right_knee_angle)
                right_hip_angle_list.append(right_hip_angle)
                left_hip_angle_list.append(left_hip_angle)
                left_knee_angle_list.append(left_knee_angle)
                left_elbow_angle_list.append(left_elbow_angle)
                right_trunk_angle_list.append(right_trunk_angle)
                left_trunk_angle_list.append(left_trunk_angle)
                left_shoulder_angle_list.append(left_shoulder_angle)

                
                counter+=1
                #DISPLAYING FPS
                currtime=time.time()
                fps=1/(currtime-prevtime)
                prevtime=currtime
                cv.putText(img, str(int(fps)), (70,50), cv.FONT_HERSHEY_PLAIN ,3, (255,0,0), 3)
                cv.putText(img, str(int(counter)), (70,90), cv.FONT_HERSHEY_PLAIN ,3, (255,0,0), 3)
                #================================================================================

                cv.imshow('Image', img)
                if (cv.waitKey(85) & 0xFF==ord('q')):
                    break   
        except:
            pass
        

        right_knee_video_angle_list[filename]=right_knee_angle_list
        right_hip_video_angle_list[filename]=right_hip_angle_list
        left_hip_video_angle_list[filename]=left_hip_angle_list
        left_knee_video_angle_list[filename]=left_knee_angle_list
        left_elbow_video_angle_list[filename]=left_elbow_angle_list
        right_trunk_video_angle_list[filename]=right_trunk_angle_list
        left_trunk_video_angle_list[filename]=left_trunk_angle_list
        left_shoulder_video_angle_list[filename]=left_shoulder_angle_list
        



#================================================================================================




right_knee_video_angle_list=pd.DataFrame(right_knee_video_angle_list)
print(right_knee_video_angle_list)
right_knee_video_angle_list.to_csv('Angles2\\kirt\\right_knee_angles.csv')
right_hip_video_angle_list=pd.DataFrame(right_hip_video_angle_list)
print(right_hip_video_angle_list.shape)
right_hip_video_angle_list.to_csv('Angles2\\kirt\\right_hip_angles.csv')

left_hip_video_angle_list=pd.DataFrame(left_hip_video_angle_list)
print(left_hip_video_angle_list.shape)
left_hip_video_angle_list.to_csv('Angles2\\kirt\\left_hip_angles.csv')

left_knee_video_angle_list=pd.DataFrame(left_knee_video_angle_list)
print(left_knee_video_angle_list.shape)
left_knee_video_angle_list.to_csv('Angles2\\kirt\\left_knee_angles.csv')

right_elbow_video_angle_list=pd.DataFrame(left_elbow_video_angle_list)
print(right_elbow_video_angle_list.shape)
right_elbow_video_angle_list.to_csv('Angles2\\kirt\\right_elbow_angles.csv')

right_trunk_video_angle_list=pd.DataFrame(right_trunk_video_angle_list)
print(right_trunk_video_angle_list.shape)
right_trunk_video_angle_list.to_csv('Angles2\\kirt\\right_trunk_angles.csv')

left_trunk_video_angle_list=pd.DataFrame(left_trunk_video_angle_list)
print(left_trunk_video_angle_list.shape)
left_trunk_video_angle_list.to_csv('Angles2\\kirt\\left_trunk_angles.csv')

right_shoulder_video_angle_list=pd.DataFrame(left_shoulder_video_angle_list)
print(right_shoulder_video_angle_list.shape)
right_shoulder_video_angle_list.to_csv('Angles2\\kirt\\right_shoulder_angles.csv')


#================================================================================================

