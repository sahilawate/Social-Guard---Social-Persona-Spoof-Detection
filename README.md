# SocialGuard - Social Persona Spoof Detection
Social Guard is a web-based tool designed to detect spoofed or fake social media profiles using heuristic analysis and real-time data extraction. In an age where identity fraud and impersonation are on the rise, Social Guard empowers users to verify the authenticity of profiles on social media.

# Problem Statement 
The rise of social media impersonation is creating serious risks for everyday users. Fake accounts are often used to scam people, spread misinformation or damage someone’s online identity.
Currently, there's no easy or reliable way for users to know if someone is copying their profile and if specific profile is trustworthy or not.
There’s a clear need for an automated, user-friendly system that can quickly detect and alert users about potential spoofing profiles and thus avoid scams.

# Approach and Solution
To solve the issue of fake or spoofed social media profiles, we propose "SocialTrust –Social Persona Spoof Detection" a simple and effective web-based tool designed to help users identify if a particular profile might be impersonating someone and if it is safe or not.
The tool works by analyzing different aspects of a profile, such as:
Username patterns
Bio similarity
Number of followers vs engagement
Profile picture analysis 

# Features
1. Lightweight frontend with Flask backend.
2. Rule-based engine flags spoof patterns in profiles.
3. Generates a Trust Score.
4. Explains each suspicious indicator.
5. Responsive Interface

# Tech Stack
1. Frontend:
HTML5
CSS3 
JavaScript

2. Backend:
Python Flask (Web framework for routing and API endpoints)
Instaloader (for profile data extraction)

3. Data Processing & Analysis:
Python scripts implementing heuristic trust scoring and profile analysis logic.

# Screenshots (UI)

![home](https://github.com/user-attachments/assets/c9c870cf-e93d-4974-b8d4-4a19965fa114)

![detector](https://github.com/user-attachments/assets/6c1952cc-0ca1-4ce9-a964-e2300831cfd7)

![positive](https://github.com/user-attachments/assets/6a95d369-c8ff-400e-a994-9104928bb31c)

![negative](https://github.com/user-attachments/assets/14d89367-b21d-4047-bc32-93641da00a2e)

# Run Instructions
1. Install the required dependencies
2. Run Flask Application (Website)
3. Enter URL to be checked in input field
4. Hit Analyze button
5. Result will get loaded based on Analysis of provided profile
