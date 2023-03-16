import "./style.css"

function DiseaseProperties(props){
    const content = props.details["content"].map((ele,index)=>{
        return (
            <li key={index}>{ele}</li>
        );
    })
    
    return (
        <>
            <h4>{props.property}</h4>
            {props.details["img"] && <img src={props.details["img"]['src']} alt={props.details["img"]['alt']}></img>}
            <ul>
                {content}
            </ul>
        </>
    );
}

export default DiseaseProperties;