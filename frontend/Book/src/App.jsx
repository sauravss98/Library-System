// import logo from "./logo.svg";
import "./App.css";
// import Header from "./components/Header/Header";
import "bootstrap";
import "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter } from "react-router-dom";
import AppRouters from "./components/AppRouters/AppRouters";

function App() {
  return (
    <BrowserRouter>
      <AppRouters />
    </BrowserRouter>
  );
}

export default App;
