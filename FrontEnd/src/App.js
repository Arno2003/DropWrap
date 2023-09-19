import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./Components/Home/Home";
import Navbar from "./Components/Navbar/Navbar";
import About from "./Components/About/About";
import Contact from "./Components/Contact/Contact";
import Geographical from "./Components/Geographical/Geographical";
import Graphical from "./Components/Graphical/Graphical";
import Footer from "./Components/Footer/Footer";
import "./App.css";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/geographical" element={<Geographical />} />
          <Route path="/graphical" element={<Graphical />} />
        </Routes>
        <Footer />
      </BrowserRouter>
    </div>
  );
}

export default App;
