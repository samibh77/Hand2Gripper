# Hand2Gripper – Computer Vision Based Medical Gripper

## 📌 Project Overview
Hand2Gripper is a simulation and control project that bridges **computer vision** and **mechatronics** to create a medical-assistive gripper.  
The system detects and tracks **hand movements in real-time** using a camera, then transfers these movements to a **mechanical gripper**.  
The gripper is actuated using **servomotors**, controlled via **PyFirmata** over UART communication.
This idea is inspired by **robotic systems designed for complex surgical operations** in the medical field, adapted here into a simulation framework to demonstrate how computer vision can drive medical-assistive devices.


This project demonstrates how **AI + Computer Vision + Embedded Systems** can be combined to develop assistive technologies for healthcare and rehabilitation.

---

## ⚙️ Features
- ✅ Real-time hand tracking using **OpenCV & Mediapipe**  
- ✅ Mapping hand gestures into **gripper movements**   
- ✅ Servo motor control through **Arduino** and **PyFirmata**  
- ✅ UART communication between camera system (Python) and microcontroller 
- ✅ 3D-designed mechanical gripper (SolidWorks CAD files included)  

---

## 🛠️ System Architecture
1. **Computer Vision (Python)**  
   - Detects and follows the user’s hand movements  
   - Processes gestures and extracts position/angle data  

2. **Communication Layer**  
   - Sends commands from Python to Arduino via UART  
   - Uses **PyFirmata** for easy interfacing  

3. **Servo Motor Control**  
   - Receives movement commands  
   - Maps signals to servo motor angles  
   - Drives the gripper according to detected gestures  

4. **Mechanical Design**  
   - Gripper modeled and simulated in **SolidWorks**  
   

