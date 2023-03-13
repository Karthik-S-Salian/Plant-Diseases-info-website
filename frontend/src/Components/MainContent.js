import "./style.css"
import Categories from "./Categories";
import Plants from "./Plants";

function MainContent(props){
    console.log("main",props.handleSelection)
    return (
        <section>
            <Categories
            data={props.data}
            selected={props.selection.selectedCategory}
            handleSelection={props.handleSelection}
            />

            <Plants
            data={props.data}
            selected={props.selection.selectedCategory}
            handleSelection={props.handleSelection}
            />

        </section>
    )
}

export default MainContent;