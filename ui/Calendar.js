import React from 'react';

const Calendar = () => {
  const daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];
  const timeBlocks = Array.from(Array(24).keys());
  const courses = [
    { id: 1, day: 'Monday', startTime: 9, endTime: 10, title: 'Course A' },
    { id: 2, day: 'Tuesday', startTime: 13.5, endTime: 15, title: 'Course B' },
    { id: 3, day: 'Wednesday', startTime: 10, endTime: 12, title: 'Course C' },
  ];

  const isDeadDay = (day) => day === 'Wednesday';

  return (
    <div>
      <table>
        <thead>
          <tr>
            <th>Time</th>
            {daysOfWeek.map((day) => (
              <th key={day} className={isDeadDay(day) ? 'dead-day' : ''}>
                {day}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {timeBlocks.map((block) => (
            <tr key={block}>
              <td>{block % 12 === 0 ? 12 : block % 12}</td>
              {daysOfWeek.map((day) => (
                <td key={day} className={isDeadDay(day) ? 'dead-day' : ''}>
                  {courses.map((course) =>
                    course.day === day &&
                    course.startTime <= block &&
                    course.endTime > block ? (
                      <div key={course.id}>{course.title}</div>
                    ) : null
                  )}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Calendar;
