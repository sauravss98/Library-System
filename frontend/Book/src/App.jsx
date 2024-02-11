// import logo from "./logo.svg";
import "./App.css";
// import Header from "./components/Header/Header";
import AppRouters from "./components/AppRouters/AppRouters";
import Header from "./components/Header/Header";

function App() {
  // let isAuthenticated = localStorage.getItem("authentication");
  // console.log(isAuthenticated.is_authenticated);
  let isAuthenticated;
  let isAuthenticatedString = localStorage.getItem("authentication");
  if (isAuthenticatedString) {
    isAuthenticated = JSON.parse(isAuthenticatedString);
  }

  return (
    <div>
      {isAuthenticated.is_authenticated ? <Header /> : null}
      <AppRouters />
    </div>
  );
}

export default App;
