import { Route, Routes } from "react-router-dom";
import React from "react";

const Layout = React.lazy(() => import("../../pages/Layout/Layout"));
// const Header = React.lazy(() => import("../Header/Header"));
const Home = React.lazy(() => import("../Home/Home"));
const Login = React.lazy(() => import("../../pages/Login/Login"));

const AppRouters = () => {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      {/* <Route element={<Header />}> */}
      <Route element={<Layout />}>
        <Route path="/home" element={<Home />} />
      </Route>
      {/* </Route> */}
    </Routes>
  );
};

export default AppRouters;
