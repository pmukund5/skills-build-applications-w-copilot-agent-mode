import React, { useEffect, useState } from 'react';

function Leaderboard() {
  const [entries, setEntries] = useState([]);

  useEffect(() => {
    fetch('https://solid-broccoli-r47q77wv7479h5jqg-8000.app.github.dev/api/leaderboard/')
      .then(res => res.json())
      .then(data => setEntries(data));
  }, []);

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Leaderboard</h2>
      <div className="card">
        <div className="card-body">
          <table className="table table-striped">
            <thead>
              <tr>
                <th>User</th>
                <th>Points</th>
              </tr>
            </thead>
            <tbody>
              {entries.map(entry => (
                <tr key={entry._id}>
                  <td>{typeof entry.user === 'object' ? entry.user.username : entry.user}</td>
                  <td>{entry.points}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Leaderboard;
