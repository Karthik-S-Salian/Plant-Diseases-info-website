import "./style.css"
import defaultImage from "../images/field.jpg"

function CategoryCard(props){
    
    const backgroundStyle={
        backgroundImage :`url(${props.image?require(`../images/${props.image}`):defaultImage})`
    }
    
    function handleClick(){
        props.handleClick(data=>{
            return {
                ...data,
                "selectedCategory":props.name
            }
        })
    }
    return (
        <div className={`categoryCard-container ${props.selected?"selected":""}`} 
        style={backgroundStyle} 
        onClick={handleClick}
        >
            <span className="category-name">{props.name}</span>
            
        </div>
    )
}

export default CategoryCard;