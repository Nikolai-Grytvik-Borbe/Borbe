const app = (
    <div>
        <a href="https://www.youtube.com/watch?v=OAUtiqYDhEc">
            <img className="photo" src="media/logo.png" alt="LOGO"></img>
        </a>
        <center><h1 className="title">TODO</h1></center>
        <hr />
        <h2>Borbe Nettside</h2>
        <h3>Har ingen liste, så her en noen funfacts om norge:</h3>
        <ul className="list">
            <li>Norge har den lengste tunellen</li>
            <li>Norge introduserte lakse sushi til Japan</li>
            <li>Den øverste oberst for den norske kongegarden er en skotsk pingvin</li>
        </ul>
    </div>
)

ReactDOM.render(app, document.getElementById("root"))
