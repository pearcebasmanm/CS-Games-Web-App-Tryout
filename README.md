# CS-Games-Web-App-Tryout
This is the web app tryout for CS Games!

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

---

## 📥 1. Clone the Repository
You can use the following in a command line:
```sh
git clone <your-github-repo-url>
cd <your-repo-name>
```
You can also clone it use any git client.

---

## 🛠 2. Set Up the Back-End (Flask)

### Navigate to the `backend_files` folder, and then the `server` folder.

### Create a Virtual Environment
```sh
python -m venv venv
```
Activate the virtual environment:
- **Mac/Linux:**
  ```sh
  source venv/bin/activate
  ```
- **Windows:**
  ```sh
  .\venv\Scripts\activate
  ```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Navigate Back to backend_files and Run the Flask Server
```sh
cd ../
python server.py
```
Flask should now be running on **http://127.0.0.1:5000**, or **http://localhost:5000**.

---

## 🎨 3. Set Up the Front-End (React)

### Navigate to the `frontend_files` Folder

### Install Dependencies
```sh
npm install
```

### Run the React App
```sh
npm start
```
React should now be running on **http://localhost:3000**.

---

From here, you should be able to start the challenge!

## 🚀 Challenge Briefing

In this challenge, you will be working on an incomplete version of a **Hotel Room Booking Web Application**. Your goal is to complete as many of the tasks provided in each track as possible, focusing on the ones you feel you are best at (it is unlikely you will have time to finish everything, so use your time wisely). There are 2 tracks to choose from: front-end and back-end. Each has three major tasks to complete. All tasks have the same weight (though some may appear harder than others), and if you complete tasks from both tracks, we will consider your relative skill level in both.

The app comes pre-furnished with a Home page, 3 non-functional room booking related pages, and a default "page not found". They all come with a simple styling, in case you do not want to work on the front-end track.

## 🚀 Front-End Track

This track involves showing us your design and page organization skills! There are no strict requirements for what it needs to look like, but try and show off your creativity, and make sure to align your design with the website's function.

You may either directly work with React, HTML and CSS, or you may choose to instead design the website interfaces with Figma, Adobe or Canva software. **If you are only working on the front-end track, it is HIGHLY recommended to use Figma/Adobe/Canva. If you use any of these, please make sure to leave links to each of your created Figma pages in the file located in the "figma_folder" directory. Any resources you for that platform should be able to be stored/accessed in from that folder.**

### Task List

- [ ] **Create Custom Theming for the Website**  
  This task involves implementing a consistent theme across all existing pages, as well as any new pages that are added. The goal is to ensure a cohesive look and feel that aligns with the brand.

- [ ] **Create and Design a Page Showing the Types of Rooms and Services**  
  A page needs to be designed that clearly displays the various types of rooms and services available. This page should be user-friendly, making it easy for potential visitors to understand the options and select what they need.

- [ ] **Create and Design an About Us Page**  
  The About Us page should provide essential information about the company, mission, and team. This page should have some information on it relating to the Hotel business in some way.

## 🚀 Back-End Track

This track involves showing us your functionality and implementation skills! You will work with the existing (but non functional) pages related to the hotel rooms, and give them the ability to do what is described in the task list.

Before you start, take a look at "server.py" in the backend_files folder to know what API routes are available to you (you can make more, but we have provided some for you).
There is also sample data in "data.py", that you can use to test your code.
We highly recommend you document your code if you have the chance, as this will greatly improve our ability to grade you effectively (but we understand if you don't have time).

### Task List

- [ ] **Create Logic for Room Look-Up Page**  
  The logic for a room-look-up page will display information about the occupants of each room. Users should be able to easily search for a room and view relevant details, such as who is occupying it and for how long.
  **On this page, you want to be able to select a room and a date, and get all relevant details about the occupants on that date. If the room is empty, display this somehow.**
  The functionality should be displayed on the front-end through the RoomOccupant.js file. The functionality can be implemented in the occupants_logic.py file in the back-end.

- [ ] **Create Logic to Book a Room and Assign a Customer**  
  A booking system will be developed to assign a customer to a specific room for a defined period. This includes processing the reservation, storing the relevant data, and ensuring that rooms are properly allocated based on availability.
   **On this page, you want to be able to select a room, and a date. If the room is unoccpuied at said date, you must allow the user to enter an occupant's information. Once the user submits the data, that occupant must be saved into "data.py". Do not allow a room to be booked if it is occupied at the entered date.**
  The functionality should be displayed on the front-end through the RoomBooking.js file. The functionality can be implemented in the booking_logic.py file in the back-end.

- [ ] **Create Logic for a Calendar View for Room Availability**  
  A calendar view should be implemented for each room, showing availability in a visually accessible way. By clicking on a specific room, users should be able to see a detailed calendar with availability dates, which will allow for easy booking.
     **On this page, you want to be able to select a room, a month, and a year. You must then display a calendar of that month (you may choose how that looks), where it is clear which days of the month are free, and which are occupied.**
  The functionality should be displayed on the front-end through the RoomAvailability.js file. The functionality can be implemented in the availability_logic.py file in the back-end.

## 🚀 Submission

Once you are done, please access this form : **https://docs.google.com/forms/d/1jco9B35LVZal76p5E65_itAqYCUdtqMNyr3v2PzLeu4**. You should then fill out all the information and submit the form. Once this is done, you are no longer allowed to modify your github repository, so make sure you are finished when doing this!