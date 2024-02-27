// components/Loading.js
import React from "react";

const Loading = () => {
  return (
    <div className="absolute flex items-center justify-center h-screen bg-dark bg-opacity-60 backdrop-blur-xl w-full z-20">
      <div className="  animate-spin rounded-full border-t-4 border-blue-500 border-solid h-16 w-16"></div>
    </div>
  );
};

export default Loading;
