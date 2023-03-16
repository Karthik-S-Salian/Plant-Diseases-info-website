import "./style.css"
import defaultImage from "../images/field.jpg"
import { createSearchParams,Link } from "react-router-dom"

function PlantCard(props){
    
    return (
        <Link to={{
            pathname: "/plant-diseases",
            search: `?${createSearchParams({
                category:props.category,
                plant: props.name
            })}`
          }}>
            <div className={'plantCard-container'}>
                <img src={props.image?require(`../images/${props.image}`):defaultImage} alt={props.name} />
                <div>{props.name}</div>
                
            </div>
        </Link>
    )
}

export default PlantCard;