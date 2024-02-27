import React, { useEffect } from "react";

const Layout = ({ children, classname = "" }) => {
  return (
    <div className={`w-full h-full my-5 px-5  ${classname} `}>{children}</div>
  );
};

export default Layout;
