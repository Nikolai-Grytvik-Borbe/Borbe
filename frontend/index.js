function homepage() {
    ReactDOM.render(<h1>Hello There</h1>, document.getElementById("title"))
    ReactDOM.render(<p>A website is appearing</p>, document.getElementById("subtext"))
    ReactDOM.render([<li>Banana</li>, <li>Apple</li>, <li>Oranges</li>, <li>Kiwis</li>], document.getElementById("list"))
}

homepage()