import "./style.css"
import defaultImage from "../images/all-categories-2.jpg"

function CategoryCard(props){
    console.log("CategoryCard",props.name,props.selected)
    const backgroundStyle={
        backgroundImage :`url(${props.image?require(`../images/${props.image}`):defaultImage})`
    }
    
    function handleClick(){
        console.log("clicked",typeof props.handleClick)
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