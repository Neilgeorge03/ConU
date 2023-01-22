import styles from './App.module.scss';
import PictureComp from './pictureComp';

function App() {
    return (
        <div className={styles.App}>
            <h1>Visualization of layoffs since the start of COVID-19</h1>
            <h2>Bubble Chart of Top 50 Companies that had layoffs and Industries that had layoffs</h2>
            {/* <img
                src={require('./img/Companies with less than 500 layoffs.png')}
                style={{ width: 500 }}
            /> */}
            <img src={require('./img/IndustryBubbleChart.png')} style={{ width: 1024 }} />
            <img src={require('./img/PackedBubbleChart.png')} style={{ width: 1024 }} />
            <h2>Companies that have more than 1500 layoffs and others merged together</h2>
           <img
                src={require("./img/Companies with more than 1500 layoffs.png")}
                style={{ width: 1024 }}
                />
            <h2>Companies that have between 500 and 1500 layoffs, below that are merged together</h2>
            <img
                src={require("./img/Companies with 500 to 1500 layoffs.png")}
                style={{ width: 1024 }}
                />
            <h2>Companies that layed off less than 500 people</h2>
            <img
                src={require("./img/Companies with less than 500 layoffs.png")}
                style={{ width: 1024 }}
                />
            <h2>Actors that have worked together in the top 1000 movies from 2006 to 2016</h2>
            <img
                src={require("./img/Relationships.png")}
                style={{ width: 1024 }}
                />
            <h2>Actors who've acted together in more than 2 movies from the previous dataset</h2>
            <img
                src={require("./img/Relationships_more_than_2.png")}
                style={{ width: 1024 }}
                />
            <h2>Actors who've acted together in more than 4 movies from the previous dataset</h2>
            <img
                src={require("./img/Relationships_more_than_4.png")}
                style={{ width: 1024 }}
                />
            <h2>Actors who've acted together in more than 6 movies from the previous dataset</h2>
            <img
                src={require("./img/Relationships_more_than_6.png")}
                style={{ width: 1024 }}
                />
\        </div>
    );
}

export default App;
