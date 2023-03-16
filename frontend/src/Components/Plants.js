import PlantCard from "./PlantCard";
import "./style.css"

function Plants(props){
    
    let cardsArray=[]
    if (props.categorySelected==="all"){
        
        Object.entries(props.data).forEach(keyValue=>{
            const [key,value]=keyValue
            value.plants.forEach((plant,index)=>{
                cardsArray.push((
                    <PlantCard
                        image={plant.image}
                        key={plant.name}
                        name={plant.name}
                        handleClick={props.handleSelection}
                        category={key}
                    />
                ))
            })
        })
    }else{
        props.data[props.categorySelected].plants.forEach(plant=>{
            cardsArray.push((
                <PlantCard
                    image={plant.image}
                    key={plant.name}
                    name={plant.name}
                    handleClick={props.handleSelection}
                    category={props.categorySelected}
                />
            ))
        })
        
    }

    return (
        <div id="plant-cards-container">
            <strong>Available Plants Data</strong>
            <div id="plants-list">
                {cardsArray}
            </div>
        </div>
    )
}

export default Plants;