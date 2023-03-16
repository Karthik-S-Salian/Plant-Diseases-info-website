import "./style.css"
import DiseaseProperties from "./DiseaseProperties";

function Disease(props){

      const properties=Object.entries(props.details).map((keyValue,index)=>{
        const [key, value] =keyValue

        return (<DiseaseProperties
            key={key}
            property={key}
            details={value}
        />)
      })
    return (
        <section id={`disease${props.index}`}>
            <h3>{props.name}</h3>
            {properties}
        </section>
    );
}

export default Disease;