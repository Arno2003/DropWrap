import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./Navbar.scss";
const Navbar = () => {
  // Making the Header Sticky after scrolling a little bit:->
  const [scrolled, setScrolled] = useState(false);

  const handleScroll = () => {
    const offset = window.scrollY;
    // console.log(offset);

    if (offset > 200) {
      setScrolled(true);
    } else {
      setScrolled(false);
    }
  };

  useEffect(() => {
    //The useEffect Hook does a specific task for the first time after loading.
    window.addEventListener("scroll", handleScroll);
    //This will detect when the user scrolls and call the "handelScroll" function
  }, []);

  const navigate = useNavigate();
  return (
    <>
      <header className={`main-header ${scrolled ? "sticky-header" : ""}`}>
        <div className="header-content">
          {/* <ul className="left">
            <li onClick={() => navigate("/")}>Home</li>
            <li onClick={() => navigate("/about")}>About</li>
            <li onClick={() => navigate("/unavailable")}>Categories</li>
          </ul> */}

          <div className="right">
            <li onClick={() => navigate("/about")}>About</li>
            <li onClick={() => navigate("/unavailable")}>Contact</li>
          </div>
        </div>
      </header>
    </>
  );
};

export default Navbar;
