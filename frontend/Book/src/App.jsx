// import logo from "./logo.svg";
import "./App.css";
// import Header from "./components/Header/Header";
import AppRouters from "./components/AppRouters/AppRouters";
import Header from "./components/Header/Header";

function App() {
  let isAuthenticated = false;
  let isAuthenticatedString = localStorage.getItem("authentication");
  if (isAuthenticatedString !== null) {
    isAuthenticated = JSON.parse(isAuthenticatedString);
  } else {
    isAuthenticated = false;
  }

  return (
    <div>
      {isAuthenticated.is_authenticated ? <Header /> : null}
      <AppRouters />
    </div>
  );
}

export default App;
