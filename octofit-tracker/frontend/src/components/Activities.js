import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://solid-broccoli-r47q77wv7479h5jqg-8000.app.github.dev/api/activities/')
      .then(res => res.json())
      .then(data => setActivities(data));
  }, []);

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Activities</h2>
      <div className="card">
        <div className="card-body">
          <table className="table table-striped">
            <thead>
              <tr>
                <th>Type</th>
                <th>Duration (min)</th>
              </tr>
            </thead>
            <tbody>
              {activities.map(activity => (
                <tr key={activity._id}>
                  <td>{activity.activity_type}</td>
                  <td>{activity.duration}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Activities;
