import React from "react";
import { useNavigate } from "react-router-dom";
import BannerImg from "../../../assets/banner.png";
import "./Banner.scss";
const Banner = () => {
  const navigate = useNavigate();
  return (
    <div className="hero-banner">
      <div className="content-container">
        <div className="content">
          <div className="text-content">
            <h1>OUR MOTIVE</h1>
            <p>
              Lorem ipsum dolor sit amet consectetur, adipisicing elit. Enim eos
              maiores quo eveniet rerum cupiditate, vitae, labore recusandae
              fuga officiis esse et reprehenderit alias voluptate, neque animi
              tempora quaerat rem.
            </p>
            <div className="ctas">
              {/* cta means "Call to Action" */}
              <div
                className="banner-cta"
                onClick={() => navigate("/geographical")}
              >
                View Map
              </div>
              <div className="banner-cta v2" onClick={() => navigate("/about")}>
                Learn More
              </div>
            </div>
          </div>
          <img className="banner-img" src={BannerImg} alt="" />
        </div>
        <div className="buttons">
          <div className="ctas">
            {/* cta means "Call to Action" */}
            <div
              className="banner-cta"
              onClick={() => navigate("/geographical")}
            >
              Geographical Distribution
            </div>
            <div className="banner-cta v2" onClick={() => navigate("/about")}>
              Graphical Distribution
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Banner;
