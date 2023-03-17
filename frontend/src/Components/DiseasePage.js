import "./style.css"
import Disease from "./Disease";
import { useSearchParams,Link} from "react-router-dom";
import data from "../data/united"
import { useEffect } from "react";


function DiseasePage(){
    const [searchParams, setSearchParams] = useSearchParams();
    const category=searchParams.get("category")
    const plantName=searchParams.get("plant")

    useEffect(() => {
        window.scrollTo(0, 0);
      }, [searchParams]);
    
    let linkArray=[]
    let diseaseArray=[]
    let index=0;
    for (const [key, value] of Object.entries(data[category][plantName]["diseases"])){
        linkArray.push((
            <li key={key}><a href={`#disease${index}`}>{key}</a></li>
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
        <div className="disease-page">
            <header>
                <h2>{category}</h2>
                <h2>{plantName}</h2>
            </header>
            <section id="table-of-content">
                <fieldset>
                    <legend>Table of Content</legend>
                    <ol>
                        {linkArray}
                    </ol>
                </fieldset>
            </section>
            
            {diseaseArray}
                
            <Link to="/">
                <section id="backButton">BACK TO HOME</section>
            </Link>  

        </div>
    );
}

export default DiseasePage;