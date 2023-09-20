# <span style="color: #ff5733;">UberLand Rideshare | [Preview Site Here](https://uber-hackathon-preview.omanagario.repl.co/)</span>

## <span style="color: #3366ff;">What is UberLand Rideshare?</span>
- <span style="color: #3366ff;">UberLand Rideshare is a community-driven ride-hailing platform that allows users to share rides, reaching their destinations in other users' cars!</span>

## <span style="color: #3366ff;">What does UberLand Rideshare aim to solve?</span>
- <span style="color: #3366ff;">Traffic congestion and travel times: By allowing users to hitch a ride with a driver anywhere, anytime, we eliminate the need for riders to wait for a street taxi.</span>
- <span style="color: #3366ff;">Efficiency and emissions: We use an algorithm to calculate the shortest distance from one place to another, improving efficiency by shortening each trip and reducing emissions, thus minimizing negative environmental impact.</span>
- <span style="color: #3366ff;">Inclusivity: UberLand Rideshare also aims to provide inclusivity by allowing wheelchair-bound riders to find a driver that allows them to travel to their destination safely and hassle-free.</span>


## <span style="color: #3366ff;">How Does UberLand Rideshare Run?</span>
<span style="color: #3366ff;">We've leveraged Python for data handling and hosting, HTML for website design, and CSS for an appealing user interface. These 3 languages work together seamlessly to provide a fast and seamless experience while browsing the website.</span>

## <span style="color: #3366ff;">Some features of UberLand Rideshare website</span>
1. **<span style="color: #ff5733;">Security Enhancements</span>**:
   - <span style="color: #3366ff;">We have made use of the SHA-256 algorithm to encrypt the users' passwords.</span>

2. **<span style="color: #ff5733;">SqLite Database</span>**:
   - <span style="color: #3366ff;">Instead of using JSON to store our user's information, we have made use of flask-sqlalchemy to safely and efficiently store data, allowing the site to function better.</span>

3. **<span style="color: #ff5733;">Flask Module</span>**:
   - <span style="color: #3366ff;">We have made use of Flask to host our website and allow users to register/log in to an account using flask-login.</span>

## <span style="color: #3366ff;">Challenges We Faced</span>
1. **<span style="color: #ff5733;">Time Constraint</span>**:
   - <span style="color: #3366ff;">Given limited time, we streamlined the website by removing redundant functions.</span>

2. **<span style="color: #ff5733;">Communication</span>**:
   - <span style="color: #3366ff;">Communication was occasionally challenging due to busy schedules. However, we overcame this by dividing tasks among team members, allowing contributions even when teammates were unavailable.</span>

## <span style="color: #3366ff;">Future Enhancements for UberLand Rideshare</span>
1. **<span style="color: #ff5733;">User Experience</span>**:
   - <span style="color: #3366ff;">Enhance user interaction with features like haptic response. Allow drivers to set coupon codes for riders to enjoy discounts.</span>

2. **<span style="color: #ff5733;">Website Functionality</span>**:
   - <span style="color: #3366ff;">Add features such as mapping and real-time ride updates when drivers accept requests. Can also add a remember me button so that user does not have to log in.</span>

3. **<span style="color: #ff5733;">Inclusivity of others</span>**:
   - <span style="color: #3366ff;">Allowing riders to request a wheelchair-friendly ride, discounts for low-income citizens</span>

## <span style="color: #3366ff;">Steps to Run the Site</span>
1. <span style="color: #3366ff;">Download the code.</span>
2. <span style="color: #3366ff;">Install the required modules listed in `requirements.txt` (ensure you use the specified versions for each module).</span>
3. <span style="color: #3366ff;">In `main.py`, configure the IP address and port for the website located at the bottom of the file</span>
4. <span style="color: #3366ff;">Run `main.py`.</span>
4. <span style="color: #3366ff;">Note: We have included some test drivers in `database.db` to test the ride hailing service.</span>

## <span style="color: #3366ff;">Troubleshooting</span>
1. <span style="color: #3366ff;">Flask not running</span>
 - <span style="color: #3366ff;">Try re-installing the modules via `requirements.txt` and try again.</span>
2. <span style="color: #3366ff;">Restarting the database</span>
 - <span style="color: #3366ff;">Un-comment line 59 in `main.py`</span>
 - ```
   #********MAKING THE DATABASE********#
   with app.app_context():
   #db.drop_all() #resets database !!!! UNCOMMENT THIS LINE !!!!
   db.create_all()
   ```

> **<span style="color: #ff5733;">Proudly made possible by</span>**: <span style="color: #3366ff;">Joxi, Hanjiong, and Yi Li of the SG Merlion team (Uber Hackathon 2023 APAC DIVISION)</span>
