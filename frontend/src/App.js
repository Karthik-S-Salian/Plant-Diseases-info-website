import Home from './Components/Home';
import DiseasePage from './Components/DiseasePage';

import { Route,Routes ,Navigate} from 'react-router-dom';



function App() {

  return (
    <div>
      
    <Routes>
      <Route exact path="/" element={<Home/>} />
      <Route exact path="/plant-diseases" element={<DiseasePage/>} />  
      <Route path="*" element={<Navigate replace to="/" />} />  
    </Routes>
      
    </div>
  );

}

export default App;
