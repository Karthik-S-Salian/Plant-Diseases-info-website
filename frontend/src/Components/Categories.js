import "./style.css"
import CategoryCard from "./CategoryCard"

function Categories(props){
    console.log(props)
    let cardsArray=Object.keys(props.data).map(key=>{
        return (
            <CategoryCard
                image={props.data[key].image}
                key={key}
                name={key}
                selected={(key===props.selected)}
                handleClick={props.handleSelection}
            />
        )
    })

    cardsArray.unshift((
        <CategoryCard
                image={"all-categories.jpg"}
                key="all"
                name="all"
                selected={("all"===props.selected)}
                handleClick={props.handleSelection}
            />
    ))

    

    return (
        <div id="categories-container">
            <strong id="categories-heading">Categories</strong>
            <div id="categories-list">
                {cardsArray}
            </div>

        </div>
    )
}

export default Categories;