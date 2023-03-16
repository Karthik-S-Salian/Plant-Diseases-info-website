import "./style.css"
import Categories from "./Categories";
import Plants from "./Plants";
import data from "../data/united"
import React from 'react';

function MainContent(){
    const [userSelection,setUserSelection]=React.useState({
        "categoryList":Object.keys(data),
        "selectedCategory":"all",
      })
    
      const [reducedDataObject,setReducedDataObject]=React.useState({})
    
      React.useEffect(()=>{
        let reducedObject={}
        for (const plantData of Object.entries(data))
        {
          reducedObject[plantData[0]]={
            image:data[plantData[0]]["image"],
            plants:Object.keys(data[plantData[0]]).filter(key=>key!=="image").map(key=>{
              return {
                image:data[plantData[0]][key].image,
                name:key
              }
            })
          }
        }
    
        setReducedDataObject(reducedObject)
    
      },[])
    
    return (
        <section>
            <Categories
            data={reducedDataObject}
            selected={userSelection.selectedCategory}
            handleSelection={setUserSelection}
            /> 

            <Plants
            data={reducedDataObject}
            categorySelected={userSelection.selectedCategory}
            handleSelection={setUserSelection}
            />

        </section>
    )
}

export default MainContent;