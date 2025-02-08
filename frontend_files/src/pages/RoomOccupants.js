import React, { useState } from "react";

const RoomOccupants = () => {
  const [date, setDate] = useState("");
  const [room, setRoom] = useState("");
  const [result, setResult] = useState("");
  function handleSubmit(e) {
    e.preventDefault();
    fetch(
      `http://127.0.0.1:5000/api/check-occupants?room_number=${room}&date=${date}`,
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
  function handleDateChange(e) {
    setDate(e.target.value);
  }
  function handleRoomChange(e) {
    setRoom(e.target.value);
  }
  return (
    <div>
      <h1>Check your Room Occupants here:</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          name="room_number"
          placeholder="Room: 101"
          value={room}
          onInput={handleRoomChange}
        />
        <input
          type="text"
          name="date"
          placeholder="Date: 2025-02-02"
          value={date}
          onInput={handleDateChange}
        />
        <button type="submit">Submit</button>
      </form>
      <p>{result}</p>
    </div>
  );
};

export default RoomOccupants;
