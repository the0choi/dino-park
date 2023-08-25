# Dino Park - Gamified Productivity Timer App

## Table of Contents
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Key Features](#key-features)
- [Usage](#usage)
- [Credits](#credits)
- [Contributors](#contributors)

## Introduction

Dino Park is a web application that gamifies the popular Pomodoro technique to enhance productivity. Users can create their virtual "Dino Park" by hatching dinosaur eggs during focused work sessions. As the user completes each session, a dino egg hatches, and a new dino is added to their park. The website aims to provide a fun and engaging way to stay focused and track productivity.

## Technologies Used

- Django
- PostgreSQL
- HTML
- CSS (Tailwind CSS)
- JavaScript
- Photoshop
- Git
- Heroku

## Key Features

- **Productivity Timer:** 
Users can set focused work sessions using a countdown timer, and upon completion, a dino egg hatches. The dino is a virtual representation of your focused time.

- **Virtual Dino Park:** 
Users' overall productivity across the day is visually depicted by the growth of their virtual park as more dino eggs are hatched over time.

- **Dynamic Data Display:** 
The website uses Plotly to create a dynamic graph that showcases the user's focus time trends across their last created 7 parks.

- **Responsive Design:** 
Tailwind CSS ensures a responsive and mobile-friendly user interface, providing an optimal experience on different devices.

- **User Authentication:** 
Users can sign up, log in, and log out securely to access their personalised Dino Park.

## Technical Features

- Built through Django, using Python as the backend programming language
- It is connected to PostgreSQL for its database. Database stores data on users, parks, dinos, and animation actions
- Code is structured with MVT design
- Demonstrates CRUD functionality across the park, dino and animation models
- Tailwind was chosen to be used for CSS for the flexibility with the website's styling, as well as for the responsive design and UI it offers
- Pushed to Github via Git
- Website deployed to Heroku

## ER Diagram
- To add..

## Screenshots
- To add..

## Usage

**Sign Up/Login:** 
Users can create an account or log in to access their Dino Park.

**Add Park:**
Create a park for a selected date to add to your collection. Note: only 1 park can be made for a particular date, and dinos can only be hatched for today's date.

**All Parks:** 
An overview of all of the user's virtual parks are showcased, displaying the date, total focused time spent each day and a link to each park. Additionally, a simple graph visualisation displays focus time trends over the past 7 parks, helping users track their producitivity over the week.

**Park Overview:** 
Users can view their Dino Park's overall productivity, including total focus time and the number of hatched dinos. Users can also set a timer here for their work sessions and use the countdown shown in the tab title while viewing other websites. Parks can also be removed here.

**Dino Details:** 
Clicking on a dino reveals more information about it. Edit their name, dino colour and even interact with your dino freely!

## Credits

- **Dino Sprite Pack**: [Dino Family by DemChing](https://demching.itch.io/dino-family)

- **Fonts**: 
  - [Broken Console](https://www.cdnfonts.com/broken-console.font)

## Contributors

- Theodore Choi ([@the0choi](https://github.com/the0choi))
- Mohammed Hani ([@motech99](https://github.com/motech99))
