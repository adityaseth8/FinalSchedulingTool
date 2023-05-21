# Project Title: ScheduleFlow
## Members: Brian Li & Aditya Seth

### Project Description: Re-design the UC Davis Finals Scheduling system to decrease the number of time blocks throughout a day and introduce a “dead-day” during finals week to promote equitable student learning and exam performance. 

- Tools: Python (BeautifulSoup, Requests, Pandas), ReactJS

## Methodology:
- Part 1: Data Extraction
  - Needed data for list of all courses offered in a singular quarter at UC Davis, and their respective class sizes, instructor name, and lecture time/dates. 
  - Needed data for list of all classrooms on campus and their respective class sizes.
  - I was able to successfully write python code from scratch to scrape the classroom sizes, but I encountered a major issue while attempting to scrape data from the Office of the University Registrar. The webpage consists entirely of multiple table forms, and I faced difficulties in using a POST request to retrieve the data via the scraper.
    - Temporarily solution: Given the primary focus of the project was on developing the algorithm, we decided to make compromises in the data acquisition process by obtaining a subset of the courses data for Winter 2023 (specifically, all ECS courses) by scraping the data from sisweb.ucdavis.edu (student information system on the web).
  - We pre-processed the data by removing unnecessary columns, eliminating rows with null CRN values, and combining rows pertaining to the same class (i.e ECS 120 A01, ECS 120 A02).
  - Saved data in csv format. To implement this at a larger scale, we can automate the csv files being pushed to a database like Mongodb everytime the scraper is run.

- Part 2: Scheduling Algorithm
  - We created an scheduling algorithm that will create a schedule for finals course with one study day during finals week (Monday or Wednesday), where students are given more time to study and prepare for finals. The algorithm will also remove finals that start at 8AM and 8PM by creating five time blocks in which each day of finals week that final exams can occur. With Python, we also created the scheduling algorithm that will generate a JSON file, assigning courses with an final exam day and time block. 

- Part 3: User Interface
  - That JSON file was then processed through a front-end program designed with React and other front-end technologies to show markers on the buildings with the assigned courses with finals.
	
- Part 4: Complexities:
  - We were new to web scraping, so scraping for the course data and seating availability posed as a hindrance to overcome. Precisely and accurately implementing a scheduling algorithm that used all the necessary and proper data structures was a great hurdle.


