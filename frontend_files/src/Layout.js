import React from "react";
import { Link } from "react-router-dom";
import "./styles/global.css";

const Layout = ({ children }) => {
  return (
    <div className="flex flex-col min-h-screen">
      {/* Navbar */}
      <nav className="navbar bg-black text-white p-4">
        <h2 className="text-xl">Hotel Booking</h2>
        <div className="flex space-x-4">
          <Link to="/" className="text-white hover:text-yellow-500">Home</Link>
          <Link to="/occupants" className="text-white hover:text-yellow-500">Occupants</Link>
          <Link to="/availability" className="text-white hover:text-yellow-500">Availability</Link>
          <Link to="/booking" className="text-white hover:text-yellow-500">Booking</Link>
        </div>
      </nav>

      {/* Main content area */}
      <div className="flex-grow container px-6 py-12">
        {children}
      </div>
    </div>
  );
};

export default Layout;
