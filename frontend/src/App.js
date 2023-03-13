import './App.css';
import Header from './Components/Header';
import MainContent from './Components/MainContent';
import Footer from './Components/Footer';
import data from "./data/united"
import React from 'react';


function App() {

  const [userSelection,setUserSelection]=React.useState({
    "categoryList":Object.keys(data),
    "selectedCategory":"all",
    "plantSelected":""
  })
  const [reducedDataObject,setReducedDataObject]=React.useState({})

  React.useEffect(()=>{
    let reducedObject={}
    for (const plantData of Object.entries(data))
    {
      reducedObject[plantData[0]]={
        image:data[plantData[0]]["image"],
        plants:Object.keys(data[plantData[0]]).filter(key=>key!=="image").forEach(key=>{
          return {
            image:data[plantData[0]][key].image
          }
        })
      }
    }

    setReducedDataObject(reducedObject)

  },[])
  
  

  return (
    <div className="App">
      <Header/>
      <MainContent
      data={reducedDataObject}
      handleSelection={setUserSelection}
      selection={userSelection}
      />
      <Footer/>
    </div>
  );
}

export default App;
