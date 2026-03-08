# AI Gesture Volume Control
This project uses Computer Vision and Hand Tracking to control your computer's system volume through hand gestures. By measuring the distance between your thumb and index finger in real-time via a webcam, the system dynamically adjusts the volume output.

> Features
Real-time Hand Tracking: Uses MediaPipe to detect and track 21 hand landmarks at high frame rates.

Gesture-Based Control: Calculates the Euclidean distance between the thumb (Landmark 4) and index finger (Landmark 8) to map physical movement to volume levels.

Visual Feedback: Overlays a live HUD (Heads-Up Display) on the webcam feed, labeling fingertips and displaying the current volume percentage.

macOS Integration: Uses osascript via Python's subprocess module to bridge the AI model with system-level audio controls.

> Tech Stack
OpenCV: For video capturing and image processing.

MediaPipe: For the machine learning pipeline and hand landmark detection.

Python Subprocess: To execute system-level commands.

> Project Structure
main.py: The entry point that handles the webcam feed and coordinates the hand-tracking logic.

volume_control.py: Contains the logic for calculating finger distance and executing the system volume change.
