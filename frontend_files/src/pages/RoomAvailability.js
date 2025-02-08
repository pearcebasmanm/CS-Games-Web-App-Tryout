import React, { useState } from "react";

const RoomAvailability = () => {
  const [room, setRoom] = useState("");
  const [month, setMonth] = useState("");
  const [year, setYear] = useState("");
  const [result, setResult] = useState("");
  function handleSubmit(e) {
    e.preventDefault();
    fetch(
      `http://127.0.0.1:5000/api/check-availability?room_number=${room}&year=${year}&month=${month}`,
      {
        methods: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      },
    )
      .then((response) => response.json())
      .then((response) => setResult(response))
      .catch((error) => console.log(error));
  }
  function handleRoomChange(e) {
    setRoom(e.target.value);
  }
  function handleYearChange(e) {
    setYear(e.target.value);
  }
  function handleMonthChange(e) {
    setMonth(e.target.value);
  }
  return (
    <div>
      <h1>Display what dates are available for a room here:</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          name="room_number"
          placeholder="Room: 101"
          value={room}
          onInput={handleRoomChange}
        />
        <input
          type="number"
          name="year"
          placeholder="Year: 2025"
          value={year}
          onInput={handleYearChange}
        />
        <input
          type="number"
          name="month"
          placeholder="Month: 02"
          value={month}
          onInput={handleMonthChange}
        />
        <button type="submit">Submit</button>
      </form>
      <p>{result}</p>
    </div>
  );
};

export default RoomAvailability;
