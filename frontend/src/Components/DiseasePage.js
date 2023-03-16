import "./style.css"
import Disease from "./Disease";
import { useSearchParams} from "react-router-dom";
import data from "../data/united"


function DiseasePage(){
    const [searchParams, setSearchParams] = useSearchParams();
    const category=searchParams.get("category")
    const plantName=searchParams.get("plant")
    
    let linkArray=[]
    let diseaseArray=[]
    let index=0;
    for (const [key, value] of Object.entries(data[category][plantName]["diseases"])){
        linkArray.push((
            <li><a href={`#disease${index}`}>{key}</a></li>
        ))
        diseaseArray.push((<Disease
            key={key}
            name={key}
            details={value}
            index={index}
        />))
        index+=1;
      }

    return (
        <div>
            <section>
                <h2>{category}</h2>
                <h2>{plantName}</h2>
            </section>
            <section id="table-of-content">
                <ol>
                    {linkArray}
                </ol>
            </section>
            
            {diseaseArray}

        </div>
    );
}

export default DiseasePage;