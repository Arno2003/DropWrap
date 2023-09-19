import React from "react";
import { FaLocationArrow, FaMobileAlt, FaEnvelope } from "react-icons/fa";
import { useNavigate } from "react-router-dom";
import "./Footer.scss";
const Footer = () => {
  const navigate = useNavigate();
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="col">
          <div className="title">About</div>
          <div className="text">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quas
            mollitia deleniti molestias quia tenetur odio reprehenderit vel
            fugiat alias! Modi ipsam voluptate sapiente, debitis aliquid facilis
            cumque eaque assumenda voluptatem iu
          </div>
        </div>
        <div className="col">
          <div className="title">Contact</div>
          <div className="c-item">
            <FaLocationArrow />
            <div className="text">25 Demo Lane, Demo, Demo, Demo, 123456</div>
          </div>
          <div className="c-item">
            <FaMobileAlt />
            <div className="text">Phone: 012 345 6789</div>
          </div>
          <div className="c-item">
            <FaEnvelope />
            <div className="text">Email: mystore01@gmail.com</div>
          </div>
        </div>
        <div className="col">
          <div className="title">Features</div>
          <span className="text" onClick={() => navigate("/category/1")}>
            Geographical Distribution
          </span>
          <span className="text" onClick={() => navigate("/category/3")}>
            Graphical Desitribution
          </span>
        </div>
        <div className="col">
          <div className="title">Pages</div>
          <span className="text" onClick={() => navigate("/")}>
            Home
          </span>
          <span className="text" onClick={() => navigate("/about")}>
            About
          </span>
          <span className="text" onClick={() => navigate("/unavailable")}>
            Privacy Policy
          </span>
          <span className="text" onClick={() => navigate("/unavailable")}>
            Terms & Conditions
          </span>
          <span className="text" onClick={() => navigate("/unavailable")}>
            Contact Us
          </span>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
