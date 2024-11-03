import Navbar from "./components/Navbar"
import ListView from "./components/ListView"
import Footer from "./components/Footer"
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
          </Routes>

        </div>
        
        <Footer/>
      </div>    
    </BrowserRouter>
  );
}

export default App;
