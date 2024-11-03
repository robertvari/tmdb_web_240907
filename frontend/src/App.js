import Navbar from "./components/Navbar"
import ListView from "./components/ListView"
import Footer from "./components/Footer"
import More from "./components/More"
import Login from "./components/Login"
import Registration from "./components/Registration"
import MovieDetails from "./components/MovieDetails"
import "./css/main.css"
import { BrowserRouter, Route, Routes } from "react-router-dom"

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <div>
          <Navbar/>

          <Routes>
            <Route path="/" element={<ListView/>}/>
            <Route path="/tvshows" element={<ListView/>}/>
            <Route path="/people" element={<ListView/>}/>
            <Route path="/more" element={<More/>}/>
            <Route path="/login" element={<Login/>}/>
            <Route path="/registration" element={<Registration/>}/>

            <Route path="/movies/:slug" element={<MovieDetails/>}/>
          </Routes>

        </div>
        
        <Footer/>
      </div>    
    </BrowserRouter>
  );
}

export default App;
