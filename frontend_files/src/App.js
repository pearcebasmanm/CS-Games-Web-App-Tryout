import React from "react";
import { Routes, Route, Link } from "react-router-dom";
import Layout from "./Layout";
import Home from "./pages/Home";
import RoomOccupants from "./pages/RoomOccupants";
import RoomAvailability from "./pages/RoomAvailability";
import RoomBooking from "./pages/RoomBooking";
import NotFound from "./pages/NotFound";

function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/occupants" element={<RoomOccupants />} />
        <Route path="/availability" element={<RoomAvailability />} />
        <Route path="/booking" element={<RoomBooking />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Layout>
  );
}

export default App;
