import React from "react";
import { Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import RoomOccupants from "./pages/RoomOccupants";
import RoomAvailability from "./pages/RoomAvailability";
import RoomBooking from "./pages/RoomBooking";
import NotFound from "./pages/NotFound";

function App() {
  return (
    <div>
      <nav>
        <Link to="/">Home</Link> | <Link to="/occupants">Check Room Occupants</Link> | <Link to="/availability">Check Room Avilability</Link> | <Link to="/booking">Book a Room </Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/occupants" element={<RoomOccupants />} />
        <Route path="/availability" element={<RoomAvailability />} />
        <Route path="/booking" element={<RoomBooking />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </div>
  );
}

export default App;
