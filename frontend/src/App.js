import Navbar from "./components/Navbar"
import ListView from "./components/ListView"
import Footer from "./components/Footer"
import "./css/main.css"

function App() {
  return (
    <div className="App">
      <div>
        <Navbar/>
        <ListView/>
      </div>
      
      <Footer/>
    </div>
  );
}

export default App;
