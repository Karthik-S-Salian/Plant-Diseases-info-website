import './App.css';
import Home from './Components/Home';
import DiseasePage from './Components/DiseasePage';

import { Route,Routes } from 'react-router-dom';



function App() {

  return (
    <div className="App">
      
    <Routes>
      <Route exact path="/" element={<Home/>} />
      <Route exact path="/plant-diseases" element={<DiseasePage/>} />    
    </Routes>
      
    </div>
  );

}

export default App;
