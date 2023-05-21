import React, { useState, useEffect } from 'react';
import moment from 'moment';
import 'react-big-calendar/lib/css/react-big-calendar.css';
import { Calendar, momentLocalizer } from 'react-big-calendar';
import Modal from 'react-modal';

const localizer = momentLocalizer(moment);

const examData = [
  {
    id: 1,
    crn: 12345,
    title: 'Exam 1',
    start: new Date(2023, 4, 17, 9, 0),
    end: new Date(2023, 4, 17, 11, 0),
    location: 'Exam Hall 1',
    course: 'Mathematics 101',
  },
  {
    id: 2,
    crn: 54321,
    title: 'Exam 2',
    start: new Date(2023, 4, 18, 14, 0),
    end: new Date(2023, 4, 18, 16, 0),
    location: 'Exam Hall 2',
    course: 'Physics 201',
  },
  // Add more exam events as needed
];

Modal.setAppElement('#root');

const App = () => {
  const [selectedExam, setSelectedExam] = useState(null);
  const [showExamDetails, setShowExamDetails] = useState(false);
   // const [modalPosition, setModalPosition] = useState({ top: 0, left: 0 });

  // useEffect(() => {
  //   const handleResize = () => {
  //     if (showExamDetails) {
  //       const eventElement = document.querySelector(`.rbc-event[data-event-id="${selectedExam.id}"]`);

  //       if (eventElement) {
  //         const eventRect = eventElement.getBoundingClientRect();

  //         setModalPosition({ top: eventRect.top, left: eventRect.right });
  //       }
  //     }
  //   };

  //   window.addEventListener('resize', handleResize);

  //   return () => {
  //     window.removeEventListener('resize', handleResize);
  //   };
  // }, [showExamDetails, selectedExam]);

  const handleEventClick = (event) => {
    setSelectedExam(event);
    setShowExamDetails(true);
    console.log(event)
  };

  const closeModal = () => {
    setSelectedExam(null);
    setShowExamDetails(false)
  };

  return (
    <div style={{ height: '100vh', padding: '20px' }}>
        {selectedExam && 
          <Modal
            isOpen={showExamDetails}
            onRequestClose={closeModal}
            contentLabel="Exam Details"
            className="modal"
            overlayClassName="overlay"
            style = {{
              overlay: {
                top: 0,
                left: 500
              }
            }}
          >
            <h2>Exam Details</h2>
            <p>
              <strong>Exam:</strong> {selectedExam.title}
            </p>
            <p>
              <strong>Course:</strong> {selectedExam.course}
            </p>
            <p>
              <strong>CRN:</strong> {selectedExam.crn}
            </p>
            <p>
              <strong>Location:</strong> {selectedExam.location}
            </p>
            <p>
              <strong>Start Time:</strong> {moment(selectedExam.start).format('h:mm A')}
            </p>
            <p>
              <strong>End Time:</strong> {moment(selectedExam.end).format('h:mm A')}
            </p>
            <button onClick={closeModal}>Close</button>
          </Modal>
        }   

        <Calendar
          title="Finals"
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
          eventPropGetter={() => ({ className: 'exam-block' })}
        />
  </div>
  );
};

export default App
