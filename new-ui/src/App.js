import React, { useState } from 'react';
import moment from 'moment';
import 'react-big-calendar/lib/css/react-big-calendar.css';
import { Calendar, momentLocalizer } from 'react-big-calendar';
import { OverlayTrigger, Tooltip } from 'react-bootstrap';

const localizer = momentLocalizer(moment);

const examData = [
  {
    title: 'Exam 1',
    start: new Date(2023, 4, 17, 9, 0), // Date(year, monthIndex, day, hours, minutes)
    end: new Date(2023, 4, 17, 11, 0),
    location: 'Exam Hall 1',
    course: 'Mathematics 101',
  },
  {
    title: 'Exam 2',
    start: new Date(2023, 4, 18, 14, 0),
    end: new Date(2023, 4, 18, 16, 0),
    location: 'Exam Hall 2',
    course: 'Physics 201',
  },
  // Add more exam events as needed
];

const App = () => {
  const [tooltipContent, setTooltipContent] = useState(false);

  const handleEventClick = (event) => {
    const { title, location, start, end, course } = event;
    

    const tooltipContent = (
      <Tooltip id="exam-tooltip">
        <strong>{title}</strong>
        <br />
        Course: {course}
        <br />
        Location: {location}
        <br />
        Time: {moment(start).format('h:mm A')} - {moment(end).format('h:mm A')}
      </Tooltip>
    );

    setTooltipContent(tooltipContent);
    console.log(tooltipContent);
  };

  const handleEventHide = () => {
    setTooltipContent(false);
  };

  return (
    <div style={{ height: '100vh', padding: '20px' }}>
      <Calendar
        localizer={localizer}
        events={examData}
        defaultView="week"
        views={['week']}
        min={moment().startOf('day').add(8, 'hours').toDate()}
        max={moment().startOf('day').add(20, 'hours').toDate()}
        step={60}
        timeslots={1}
        defaultDate={new Date()}
        showMultiDayTimes
        selectable
        onSelectEvent={handleEventClick}
        onSelectSlot={handleEventHide}
        eventPropGetter={() => ({ className: 'exam-block' })}
      />

      <OverlayTrigger placement="top" overlay={tooltipContent}>
        <div id="exam-tooltip-container" />
      </OverlayTrigger>
    </div>
  );
};

export default App;
