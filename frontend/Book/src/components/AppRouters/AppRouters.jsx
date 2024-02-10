import { Route, Routes } from "react-router-dom";
import React from "react";

const Home = React.lazy(() => import("../Home/Home"));
const Login = React.lazy(() => import("../../pages/Login/Login"));
const Books = React.lazy(() => import("../Books/Books"));
const CartPage = React.lazy(() => import("../CartPage/CartPage"));

const AppRouters = () => {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/home" element={<Home />} />
        <Route path="/books" element={<Books />} />
        <Route path="/cart" element={<CartPage />} />
      </Routes>
    </div>
  );
};

export default AppRouters;
